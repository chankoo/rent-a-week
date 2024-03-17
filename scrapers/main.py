from scraper_33m2 import parse_detail
from extractors import ExcelExtractor
import time
import datetime
from zoneinfo import ZoneInfo
import asyncio

local_tz = ZoneInfo('Asia/Seoul')


async def main():
    s = time.time()
    ee = ExcelExtractor('./data/room_details', datetime.datetime.now().astimezone(local_tz).strftime('%Y-%m-%d %H:%M:%S'))
    
    batch_size = 100
    from_rid = 26500
    while from_rid > 0:
        to_rid = from_rid-batch_size if from_rid > batch_size else 0
        tasks = [parse_detail(rid) for rid in range(from_rid, to_rid, -1)]
        data = await asyncio.gather(*tasks)
        ee.save_as_excel(data)
        from_rid = to_rid
        print(from_rid, time.time()-s)


if __name__ == "__main__":
    asyncio.run(main())
