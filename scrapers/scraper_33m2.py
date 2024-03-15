import os
import requests
from urllib import parse
from bs4 import BeautifulSoup

DETAIL_STR_KEYS = [
    "title",
    "og_image",
    "room_name",
    "address",
    "introduction",
    "room_count",
    "area",
    "location",
    "min_contract_period",
    "rental_fee",
    "management_fee",
    "cleaning_fee",
    "deposit"
]
DETAIL_LST_KEYS = ["basic_options", "additional_options"]

def create_detail_data_scheme():
    scheme = {key: "" for key in DETAIL_STR_KEYS}
    scheme.update({key: [] for key in DETAIL_LST_KEYS})
    return scheme

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


def detail(rid: int):
    url = f"https://33m2.co.kr/room/detail/{rid}"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ko-KR,ko;q=0.9",
        "Cache-Control": "no-cache",
        "Cookie": "JSESSIONID=A24E6E175B661CE3E93B3BFD8EEDDFCC; webuuid=web-ee65b266-1063-4c5f-8b99-f0242dfda64c; _ga=GA1.1.2071080023.1710422730; _fbp=fb.2.1710422730522.113407075; ab180ClientId=7bb600b3-76c6-41d0-9cb5-e52a55f52e64; _ga_9DDC4XR357=GS1.1.1710422730.1.1.1710427413.54.0.0; airbridge_session=%7B%22id%22%3A%2228c16fa2-7c3b-4436-b489-4c39201a5a2d%22%2C%22timeout%22%3A1800000%2C%22start%22%3A1710422731034%2C%22end%22%3A1710427414160%7D; AWSALB=LwBDXcc4KQMAoqywN47Cn4F4cP/y+kET0dpRoXX7jpB0YqdPGe4XnOg2Ua40ja8BhRmoVSnjvoMcrXxOGcBI8kT1uNmt8UW/PMEreHkdVJLxv8VT/YwSZmeHHJFJ; AWSALBCORS=LwBDXcc4KQMAoqywN47Cn4F4cP/y+kET0dpRoXX7jpB0YqdPGe4XnOg2Ua40ja8BhRmoVSnjvoMcrXxOGcBI8kT1uNmt8UW/PMEreHkdVJLxv8VT/YwSZmeHHJFJ",
        "Pragma": "no-cache",
        "Sec-Ch-Ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"macOS"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    res = requests.get(url, headers=headers)
    return res



def parse_detail(rid: int) -> dict:
    res = detail(rid)
    soup = BeautifulSoup(res.text, 'html.parser')
    result = create_detail_data_scheme()

    # 이미지 다운로드
    download_room_images(soup, output_path=f'data/room_images/{rid}')

    # 타이틀 추출
    result["title"] = soup.title.text.strip()

    # 메타 데이터 추출
    result["og_image"] = soup.find('meta', {'property': 'og:image'})['content']

    # 주요 정보
    main_content = soup.find('section', {'class': 'content'})
    room_info = main_content.find('div', {'class': 'room_info'})

    if room_info:
        # 방 정보
        result["room_name"] = room_info.find('div', {'class': 'title'}).strong.text.strip()
        result["address"] = room_info.find('p', {'class': 'add_text'}).text.strip()
        introduction_raw = room_info.find('div', {'class': 'title_text'})
        if introduction_raw:
            result["introduction"] = introduction_raw.text.strip()

    # 기본 정보
    basic_info = room_info.find('div', {'class': 'place_box'}) if room_info else None

    if basic_info:
        result["room_count"] = basic_info.find('ul', {'class': 'place_list'}).li.p.text
        result["area"] = basic_info.find('ul', {'class': 'place_detail'}).find('span').next_sibling.strip()

    if room_info:
        # 옵션
        options_raw = room_info.find('div', {'class': 'room_info'}, string='기본 옵션')
        options = options_raw.find_next('ul', {'class': 'option'}) if options_raw else []
        if options:
            result["basic_options"] = [option.p.text.strip() for option in options.find_all('li')]

        # 그 밖의 옵션
        other_options_raw = room_info.find('div', {'class': 'room_info'}, string='그 밖의 옵션')
        other_options = other_options_raw.find_next('ul', {'class': 'option etc'}) if other_options_raw else []
        if other_options:
            result["additional_options"] = [option.p.text.strip() for option in other_options.find_all('li')]

        # 교통 & 위치
        location_info = room_info.find('div', {'class': 'room_info'}, string='교통 & 위치')
        if location_info:
            result["location"] = location_info.find('div', {'class': 'title_text'}).text.strip()

        # 계약 정보
        contract_info = room_info.find('div', {'class': 'room_info'}, string='계약 정보')
        if contract_info:
            result["min_contract_period"] = contract_info.find('p', {'class': 'icon_info'}).strong.text

        if contract_info:
            # 보증금, 임대료, 관리비, 청소비 정보
            table = contract_info.find('table', {'class': 'tbl_style'})
            rows = table.find_all('tbody')[0].find_all('td') if table else []
            if rows:
                result["rental_fee"], result["management_fee"], result["cleaning_fee"], result["deposit"] = [row.text.strip() for row in rows]
    return result



def download_room_images(soup, output_path):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # Find all divs with class 'swiper-slide' containing image URLs
    image_divs = soup.find_all('div', class_='swiper-slide')
    
    # Counter for image numbering
    image_count = 1
    
    # Download each image
    for div in image_divs:
        # Extract image URL
        image_url = div.find('img')['src']
        
        # Download the image
        response = requests.get(image_url)
        if response.status_code == 200:
            # Write the image to a file
            with open(os.path.join(output_path, f'image_{image_count}.jpg'), 'wb') as f:
                f.write(response.content)
            image_count += 1
