import logging

import httpx
from fake_useragent import UserAgent
from tenacity import retry, stop_after_attempt, retry_if_exception_type, after_log

logger = logging.getLogger(__name__)


class UserAgentManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserAgentManager, cls).__new__(cls)
            cls._instance._ua_value = UserAgent().random
        return cls._instance

    def get_user_agent(self):
        """현재 저장된 User-Agent 반환"""
        return self._ua_value

    def refresh_user_agent(self):
        """User-Agent 새로 갱신"""
        self._ua_value = UserAgent().random


class ProxyManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ProxyManager, cls).__new__(cls)
            cls._instance._proxies = []
            cls._instance._current_proxy = None
        return cls._instance

    def get_current_proxy(self):
        """현재 사용 중인 프록시 반환"""
        if self._current_proxy is None:
            self.refresh_current_proxy()
        return self._current_proxy

    def refresh_current_proxy(self):
        """새로운 프록시로 갱신"""
        if not self._proxies:
            self.refresh_proxy_list()
        self._current_proxy = self._proxies[0]
        self._proxies = self._proxies[1:]

    @retry(
        retry=retry_if_exception_type(httpx.TimeoutException),
        stop=stop_after_attempt(3),
        reraise=True,
        after=after_log(logger, logging.ERROR),
    )
    def refresh_proxy_list(self):
        """프록시 목록 갱신"""
        url = "https://proxylist.geonode.com/api/proxy-list?country=KR&limit=100&page=1&sort_by=speed&sort_type=asc"
        res = sync_request_get(url, timeout=25)
        data = res.json()["data"]
        proxies = [
            f"{proxy['protocols'][0]}://{proxy['ip']}:{proxy['port']}" for proxy in data
        ]
        self._proxies = proxies


async def request_get(
    url: str,
    headers: dict = None,
    **kwargs,
) -> httpx.Response:
    if headers is None:
        headers = {}
    headers["User-Agent"] = UserAgentManager().get_user_agent()
    proxy = ProxyManager().get_current_proxy()

    async with httpx.AsyncClient(proxy) as client:
        res = await client.get(url, headers=headers, **kwargs)

        if res.status_code == 403:
            UserAgentManager().refresh_user_agent()
            ProxyManager().refresh_current_proxy()
        if res.status_code != 200:
            res.raise_for_status()
    return res


async def request_post(
    url: str,
    headers: dict = None,
    data: dict = None,
    **kwargs,
) -> httpx.Response:
    if headers is None:
        headers = {}
    headers["User-Agent"] = UserAgentManager().get_user_agent()
    proxy = ProxyManager().get_current_proxy()

    async with httpx.AsyncClient(proxy=proxy) as client:
        res = await client.post(url, headers=headers, data=data, **kwargs)

        if res.status_code == 403:
            UserAgentManager().refresh_user_agent()
            ProxyManager().refresh_current_proxy()
        if res.status_code != 200:
            res.raise_for_status()
    return res


def sync_request_get(
    url: str,
    headers: dict = None,
    **kwargs,
) -> httpx.Response:
    if headers is None:
        headers = {}
    headers["User-Agent"] = UserAgentManager().get_user_agent()

    with httpx.Client() as client:
        res = client.get(url, headers=headers, **kwargs)

        if res.status_code == 403:
            UserAgentManager().refresh_user_agent()
        if res.status_code != 200:
            res.raise_for_status()
    return res


def sync_request_post(
    url: str,
    headers: dict = None,
    data: dict = None,
    **kwargs,
) -> httpx.Response:
    if headers is None:
        headers = {}
    headers["User-Agent"] = UserAgentManager().get_user_agent()

    with httpx.Client() as client:
        res = client.post(url, headers=headers, data=data, **kwargs)

        if res.status_code == 403:
            UserAgentManager().refresh_user_agent()
        if res.status_code != 200:
            res.raise_for_status()
    return res
