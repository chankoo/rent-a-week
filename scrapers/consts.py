DETAIL_STR_KEYS = [
    "title",
    "og_image",
    "room_name",
    "address",
    "badges",
    "default_info",
    "location_text",
    "price_info",
]
DETAIL_LST_KEYS = [
    "default_keywords",
    "default_options",
    "etc_options",
    "location_keywords",
    "reviews",
]

def create_detail_data_scheme():
    scheme = {key: "" for key in DETAIL_STR_KEYS}
    scheme.update({key: [] for key in DETAIL_LST_KEYS})
    return scheme
