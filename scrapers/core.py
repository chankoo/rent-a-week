import httpx
from fake_useragent import UserAgent


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


async def request_get(
    url: str,
    headers: dict = None,
    **kwargs,
) -> httpx.Response:
    if headers is None:
        headers = {}
    headers["User-Agent"] = UserAgentManager().get_user_agent()

    async with httpx.AsyncClient() as client:
        res = await client.get(url, headers=headers, **kwargs)

        if res.status_code == 403:
            UserAgentManager().refresh_user_agent()
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

    async with httpx.AsyncClient() as client:
        res = await client.post(url, headers=headers, data=data, **kwargs)

        if res.status_code == 403:
            UserAgentManager().refresh_user_agent()
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
