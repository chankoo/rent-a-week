from scrapers.scraper_33m2 import search, search_list, schedule

def test_search():
    res = search()
    assert res.status_code == 200
    assert isinstance(res.json(), dict)

def test_search_list():
    res = search_list(keyword='강남', page=1)
    assert res.status_code == 200
    assert isinstance(res.text, str)

def test_schedule():
    res = schedule(rid=21342, year='2024', month='12')
    assert res.status_code == 200
    assert isinstance(res.json(), dict)