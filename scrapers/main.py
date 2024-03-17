import time
import asyncio

from scraper_33m2 import parse_detail, aggregate_schedules
from extractors import ExcelExtractor
from utils import tz_now


async def details(from_rid:int, batch_size:int):
    s = time.time()
    ee = ExcelExtractor('./data/room_details', tz_now().strftime('%Y-%m-%d %H:%M:%S'))
    
    while from_rid > 0:
        to_rid = from_rid-batch_size if from_rid > batch_size else 0
        tasks = [parse_detail(rid) for rid in range(from_rid, to_rid, -1)]
        data = await asyncio.gather(*tasks, return_exceptions=True)
        data = [row for row in data if row and not isinstance(row, Exception)]
        if data:
            ee.save_as_excel(data)
        from_rid = to_rid
        print(from_rid, time.time()-s)


async def schedules(from_rid:int, batch_size:int, months:int=3):
    s = time.time()
    ee = ExcelExtractor('./data/room_schedules', tz_now().strftime('%Y-%m-%d %H:%M:%S'))
    
    while from_rid > 0:
        to_rid = from_rid-batch_size if from_rid > batch_size else 0
        tasks = [aggregate_schedules(rid, months) for rid in range(from_rid, to_rid, -1)]
        data = await asyncio.gather(*tasks, return_exceptions=True)
        data = [row for row in data if row and not isinstance(row, Exception)]
        if data:
            ee.save_as_excel(data)
        from_rid = to_rid
        print(from_rid, time.time()-s)


async def main():
    await details(from_rid=26500, batch_size=100)
    await schedules(from_rid=26500, batch_size=100)


if __name__ == "__main__":
    asyncio.run(main())
