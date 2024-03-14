import requests
from urllib import parse


# map
def search(data: dict = None):
    url = "https://33m2.co.kr/app/room/search"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ko-KR,ko;q=0.9",
        "Cache-Control": "no-cache",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "JSESSIONID=A24E6E175B661CE3E93B3BFD8EEDDFCC; webuuid=web-ee65b266-1063-4c5f-8b99-f0242dfda64c; _ga=GA1.1.2071080023.1710422730; _fbp=fb.2.1710422730522.113407075; ab180ClientId=7bb600b3-76c6-41d0-9cb5-e52a55f52e64; airbridge_session=%7B%22id%22%3A%2228c16fa2-7c3b-4436-b489-4c39201a5a2d%22%2C%22timeout%22%3A1800000%2C%22start%22%3A1710422731034%2C%22end%22%3A1710423906437%7D; _ga_9DDC4XR357=GS1.1.1710422730.1.1.1710423907.50.0.0; AWSALB=dALqVci3BXbBH9lxrE6bp5y2jABS3QZnrMri2AgL32BxBDXP80w0pd0Ay+geKebHrCehQ6xWvNwttNDkrex7i2ii4GXy6HOG+vCCPT4F0RHRLPlmCIMyRvJd0Xmh; AWSALBCORS=dALqVci3BXbBH9lxrE6bp5y2jABS3QZnrMri2AgL32BxBDXP80w0pd0Ay+geKebHrCehQ6xWvNwttNDkrex7i2ii4GXy6HOG+vCCPT4F0RHRLPlmCIMyRvJd0Xmh",
        "Origin": "https://33m2.co.kr",
        "Pragma": "no-cache",
        "Referer": "https://33m2.co.kr/webpc/search/map",
        "Sec-Ch-Ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"macOS"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    data = data or {
        'theme_type': '',
        'keyword': '',
        'room_cnt': '',
        'property_type': '',
        'animal': 'false',
        'subway': 'false',
        'longterm_discount': 'false',
        'early_discount': 'false',
        'parking_place': 'false',
        'start_date': '',
        'end_date': '',
        'week': '',
        'min_using_fee': '',
        'max_using_fee': '',
        'sort': 'popular',
        'now_page': '1',
        'map_level': '4',
        'by_location': 'true',
        'north_east_lng': '127.08676083883671',
        'north_east_lat': '37.51823939782906',
        'south_west_lng': '127.06669717575778',
        'south_west_lat': '37.49653821514252',
        'itemcount': '1000'
    }
    res = requests.post(url, json=data, headers=headers)
    return res

def search_list(keyword:str = '', page:int = 1, data: dict = None):
    keyword = parse.quote(keyword)
    url = "https://33m2.co.kr/webpc/search/room/list"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ko-KR,ko;q=0.9",
        "Cache-Control": "no-cache",
        "Content-Length": "244",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "JSESSIONID=A24E6E175B661CE3E93B3BFD8EEDDFCC; webuuid=web-ee65b266-1063-4c5f-8b99-f0242dfda64c; _ga=GA1.1.2071080023.1710422730; _fbp=fb.2.1710422730522.113407075; ab180ClientId=7bb600b3-76c6-41d0-9cb5-e52a55f52e64; AWSALB=vrfZPoRB899vrkhxJFkUzdhkMWiZRfRfmgSqeQ33Xi824LUlCjz8OiCEbHNVZn67YL/IOVpk4MV+3N41RAQUwTcQQUPv9LUVfaKr724Thzx+K/NTM778o/TkV2aQ; AWSALBCORS=vrfZPoRB899vrkhxJFkUzdhkMWiZRfRfmgSqeQ33Xi824LUlCjz8OiCEbHNVZn67YL/IOVpk4MV+3N41RAQUwTcQQUPv9LUVfaKr724Thzx+K/NTM778o/TkV2aQ; airbridge_session=%7B%22id%22%3A%2228c16fa2-7c3b-4436-b489-4c39201a5a2d%22%2C%22timeout%22%3A1800000%2C%22start%22%3A1710422731034%2C%22end%22%3A1710424131133%7D; _ga_9DDC4XR357=GS1.1.1710422730.1.1.1710424181.1.0.0",
        "Origin": "https://33m2.co.kr",
        "Pragma": "no-cache",
        "Referer": f"https://33m2.co.kr/webpc/search/keyword?keyword={keyword}&start_date=&end_date=&week=",
        "Sec-Ch-Ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"macOS"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    data = data or {
        "theme_type": "",
        "keyword": keyword,
        "room_cnt": "",
        "property_type": "",
        "animal": "false",
        "subway": "false",
        "longterm_discount": "false",
        "early_discount": "false",
        "parking_place": "false",
        "start_date": "",
        "end_date": "",
        "week": "",
        "min_using_fee": "",
        "max_using_fee": "",
        "sort": "popular",
        "now_page": f"{page}"
    }
    res = requests.post(url, json=data, headers=headers)
    return res


def schedule(rid: int, year: str, month: str):
    url = "https://33m2.co.kr/app/room/schedule"
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'ko-KR,ko;q=0.9',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'JSESSIONID=A24E6E175B661CE3E93B3BFD8EEDDFCC; webuuid=web-ee65b266-1063-4c5f-8b99-f0242dfda64c; _ga=GA1.1.2071080023.1710422730; _fbp=fb.2.1710422730522.113407075; ab180ClientId=7bb600b3-76c6-41d0-9cb5-e52a55f52e64; _ga_9DDC4XR357=GS1.1.1710422730.1.1.1710423182.60.0.0; airbridge_session=%7B%22id%22%3A%2228c16fa2-7c3b-4436-b489-4c39201a5a2d%22%2C%22timeout%22%3A1800000%2C%22start%22%3A1710422731034%2C%22end%22%3A1710423183281%7D; AWSALB=D7UBeQzii9hPLSZtoj/UaweOknMgYls+CLrgnhsfMISwX4GRtmO5cid0Y5oDGxiYhNQPXdTzvPorQgdutqZWdcWu4pZEuDPHUfEVJ/5gXE86UPaG8PjYf25e/8Eu; AWSALBCORS=D7UBeQzii9hPLSZtoj/UaweOknMgYls+CLrgnhsfMISwX4GRtmO5cid0Y5oDGxiYhNQPXdTzvPorQgdutqZWdcWu4pZEuDPHUfEVJ/5gXE86UPaG8PjYf25e/8Eu',
        'Origin': 'https://33m2.co.kr',
        'Pragma': 'no-cache',
        'Referer': f'https://33m2.co.kr/room/detail/{rid}',
        'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"macOS"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    data = {
        "rid": rid,
        "year": year,
        "month": month,
    }
    res = requests.post(url, headers=headers, data=data)
    return res
