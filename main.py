from campaign_list import link_list
from context_processor_many_cookies import check_link_cookies


# Define the list of required cookies
list_of_required_cookies = [
    'admitad_uid',
    'admitad_aid',
    'tagtag_aid',
    'deduplication_cookie',
    '_source',
    'deduplication_source',
    '_aid',
]


if __name__ == '__main__':
    check_link_cookies(link_list, list_of_required_cookies)
