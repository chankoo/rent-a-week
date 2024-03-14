from scrapers.scraper_33m2 import search, search_list, schedule, detail, parse_detail, create_detail_data_scheme

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

def test_detail():
    res = detail(rid=21342)
    assert res.status_code == 200
    assert isinstance(res.text, str)

def test_parse_detail():
    res = parse_detail(rid=21342)
    assert isinstance(res, dict)
    assert res.keys() == create_detail_data_scheme().keys()