import json
import os
import requests
from urllib import parse

from bs4 import BeautifulSoup
import aiofiles
import httpx
import asyncio

from consts import create_detail_data_scheme
from utils import get_ym_formats, get_remain_days_of_month


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
        "min_using_fee": "0",
        "max_using_fee": "1000000",
        "sort": "recent",
        "now_page": f"{page}"
    }
    res = requests.post(url, json=data, headers=headers)
    return res


async def schedule(rid: int, year: int, month: int):
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
        "year": str(year),
        "month": str(month).zfill(2),
    }
    async with httpx.AsyncClient() as client:
        res = await client.post(url, headers=headers, data=data)
    return res


async def detail(rid: int):
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
    async with httpx.AsyncClient() as client:
        res = await client.get(url, headers=headers)
    return res


async def aggregate_schedules(rid:int, months:int=3) -> dict:
    """
    이번달을 포함 <months> 개월간 예약 상태를 count
    """

    yms = get_ym_formats(months)
    tasks = [schedule(rid, year, month) for year, month in yms]
    schedules = await asyncio.gather(*tasks)
    
    res = {"rid": rid, "available":0, "disable":0, "booking":0}
    for ym, sched in zip(yms, schedules):
        remain_total = get_remain_days_of_month(year=int(ym[0]), month=int(ym[1])) 
        disable = 0
        booking = 0
        try:
            schedule_list = sched.json()["schedule_list"]
        except json.decoder.JSONDecodeError:
            res["available"] += remain_total
            continue

        for day in schedule_list:
            if day["status"] == 'booking':
                booking += 1
            elif day["status"] == 'disable':
                disable += 1
        res["available"] += remain_total - (disable + booking)
        res["disable"] += disable
        res["booking"] += booking
    return res


async def parse_detail(rid: int) -> dict:
    res = await detail(rid)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    if soup.find('div', class_='guide_message'):
        return {}
    
    result = create_detail_data_scheme()

    # 이미지 다운로드
    try:
        await download_room_images(soup, output_path=f'data/room_images/{rid}')
    except httpx.ReadTimeout as e:
        print(f'{rid}!! httpx.ReadTimeout {download_room_images}')

    # 메타 정보
    result["rid"] = rid
    result["title"] = soup.title.text.strip()
    result["og_image"] = soup.find('meta', {'property': 'og:image'})['content']

    main_content = soup.find('section', {'class': 'content'})
    room_infos = main_content.find_all('div', {'class': 'room_info'})

    if not room_infos:
        return result
    
    # 방 정보
    room_info0 = room_infos[0]
    result["room_name"] = room_info0.find('div', {'class': 'title'}).strong.text.strip()
    result["address"] = room_info0.find('p', {'class': 'add_text'}).text.strip()
    result["badges"] = [badge.text.strip() for badge in room_info0.select('.group .badge')]

    for room_info in room_infos[1:]:
        section_title = room_info.find(class_='title').text.strip()
        if section_title == "공간 기본 정보":
            res = {}
            li_tags = room_info.select('ul.place_detail li')
            for li_tag in li_tags:
                res[li_tag.find('span').text.strip()] = li_tag.find('strong').text.strip()
            result["default_info"] = res
            result["default_keywords"] = [keyword.text.strip() for keyword in room_info.select(".keyword_area > span")]
        elif section_title == "기본 옵션":
            result["default_options"] = [option.text.strip() for option in room_info.select("ul.option > li > p")]
        elif section_title == "그 밖의 옵션":
            result["etc_options"] = [option.text.strip() for option in room_info.select("ul.option > li > p")]
        elif section_title == "교통 & 위치":
            result["location_text"] = room_info.find_all(class_='title_text')[-1].text.strip()
            result["location_keywords"] = [keyword.text.strip() for keyword in room_info.select(".keyword_area > span")]
        elif section_title == "계약 정보":
            res = {}
            table = room_info.find('table')
            header = [th.text.strip() for th in table.find_all('th')]
            tds = []
            for td in table.select('tbody > td'):
                tds.append(td.text.strip())
            for i, column_name in enumerate(header):
                res[column_name] = tds[i]
            result["price_info"] = res
        elif section_title[:5] == "이용 후기":
            reviews = []
            li_tags = room_info.select(".review_list > li")
            for li_tag in li_tags:
                review = {}
                review['score'] = li_tag.find(class_='score')['style'].split(': ')[1].split('%')[0]
                review['reviewer'] = li_tag.find(class_='review_item').text.strip()
                review['date'] = li_tag.find_all(class_='review_item')[1].text.strip()
                review['content'] = li_tag.find(class_='review_text').text.strip()
                reviews.append(review)
            result["reviews"] = reviews
    return result


async def download_room_images(soup, output_path):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # Find all divs with class 'swiper-slide' containing image URLs
    image_divs = soup.find_all('div', class_='swiper-slide')

    # Counter for image numbering
    image_count = 1

    
    async with httpx.AsyncClient() as client:
        # Download each image
        for div in image_divs:
            # Extract image URL
            image_url = div.find('img')['src']
            
            # Download the image
            res = await client.get(image_url)
            if res.status_code == 200:
                # Write the image to a file
                async with aiofiles.open(os.path.join(output_path, f'image_{image_count}.jpg'), 'wb') as f:
                    await f.write(res.read())
                image_count += 1
