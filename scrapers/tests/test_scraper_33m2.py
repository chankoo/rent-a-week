import pytest
import datetime

from scrapers.scraper_33m2 import search, search_list, schedule, detail, parse_detail, create_detail_data_scheme, aggregate_schedules
from scrapers.consts import create_detail_data_scheme
from scrapers.utils import get_remain_days_of_month

def test_search():
    res = search()
    assert res.status_code == 200
    assert isinstance(res.json(), dict)

def test_search_list():
    res = search_list(keyword='강남', page=1)
    assert res.status_code == 200
    assert isinstance(res.text, str)

@pytest.mark.asyncio
async def test_schedule():
    res = await schedule(rid=21342, year=2024, month=12)
    assert res.status_code == 200
    assert isinstance(res.json(), dict)
    assert isinstance(res.json()["schedule_list"], list)

@pytest.mark.asyncio
async def test_detail():
    res = await detail(rid=21342)
    assert res.status_code == 200
    assert isinstance(res.text, str)

@pytest.mark.asyncio
async def test_parse_detail():
    res = await parse_detail(rid=21342)
    assert isinstance(res, dict)
    assert res.keys() == create_detail_data_scheme().keys()

def test_get_remain_days_of_month():
    d240317 = datetime.datetime.strptime('2024-03-17', '%Y-%m-%d')
    d240401 = datetime.datetime.strptime('2024-04-01', '%Y-%m-%d')
    d240201 = datetime.datetime.strptime('2024-02-01', '%Y-%m-%d')
    assert 15 == get_remain_days_of_month(d240317.year, d240317.month)
    assert 30 == get_remain_days_of_month(d240401.year, d240401.month)
    assert 29 == get_remain_days_of_month(d240201.year, d240201.month)


@pytest.mark.asyncio
async def test_aggregate_schedules():
    res = await aggregate_schedules(21342, months=3)
    assert isinstance(res, dict)
    assert len(res.keys()) == 4
    assert sum(res.values()) > 59
