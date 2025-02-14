from typing import Dict

import os
import time
import urllib.parse
from datetime import datetime
from time import sleep
from json import dump

import requests
import undetected_chromedriver as uc
from undetected_chromedriver import Chrome
from selenium import webdriver


def save_specific_cookies(driver, data: Dict) -> None:
    """
    Saves specified cookies in the data dictionary.

    Args:
        driver: WebDriver instance.
        data: Dictionary to store cookies.
    """
    list_of_required_cookies = [
        'admitad_uid',
        'admitad_aid',
        'tagtag_aid',
        'deduplication_cookie',
        '_source',
        'deduplication_source',
        '_aid',
    ]
    all_cookies = driver.get_cookies()
    for cookie in all_cookies:
        if cookie['name'] in list_of_required_cookies:
            data['cookies'][cookie['name']] = cookie['value']


def save_first_redirect_url(driver, data: Dict) -> None:
    """
    Extracts and saves parameters from the first redirect URL.

    Args:
        driver: WebDriver instance.
        data: Dictionary to store extracted parameters.
    """
    url_parameters_to_extract = [
        'utm_source',
        'admitad_uid',
        'admitad_aid',
        'tagtag_aid',
        'tagtag_uid',
        'source',
    ]
    data['final_url'] = driver.current_url
    # Parse parameters from final_url
    parsed_url = urllib.parse.urlparse(data['final_url'])
    data['query_params'] = urllib.parse.parse_qs(parsed_url.query)
    for param in url_parameters_to_extract:
        if param in data['query_params']:
            data[param] = data['query_params'][param][0]


def check_link_cookies(links: dict[str: str], list_of_required_cookies: list):
    """
    Checks cookies and other data from a list of links and saves the results to JSON files.

    This function iterates through a dictionary of links, opens each link using Selenium WebDriver,
    and collects data about the page, including cookies, status code, and URL parameters. It also
    checks for the presence of specific cookies and logs any missing cookies. The collected data
    is stored in `all_data`, and any errors encountered are stored in `error_data`. Finally, the
    results are saved to two JSON files: 'results/all_results.json' and 'results/error_results.json'.

    Args:
        links (dict): A dictionary where keys are logins and values are the corresponding links.
        list_of_required_cookies (list): A list of cookie names that are expected to be present.
    """
    start_time = time.time()
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1400,1000')
    # options.add_argument('--headless')
    options.page_load_strategy = 'eager'
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    driver.set_script_timeout(20)
    driver.set_page_load_timeout(20)
    error_data = []
    all_data = []

    # https://scrapfly.io/blog/web-scraping-without-blocking-using-undetected-chromedriver/
    # https://www.browserscan.net/bot-detection
    # options = uc.ChromeOptions()
    # driver = uc.Chrome(options=options)

    for login, af_link in links.items():
        initial_link = af_link
        driver.get(af_link)
        response = requests.get(af_link)
        sleep(3)
        data = {
            'Login': login,
            'Status': response.status_code,
            'datetime': str(datetime.now().strftime('%d.%m.%Y-%H:%M:%S')),
            'initial_link': initial_link,
            'final_url': driver.current_url,
            'query_params': '',
            'cookies': {},
        }

        save_specific_cookies(driver, data)
        save_first_redirect_url(driver, data)

        # Check if ALL required cookies are missing
        all_cookies_missing = all(
            cookie_name not in data['cookies'] for cookie_name in
            list_of_required_cookies)
        if all_cookies_missing:
            error_data.append({
                'Login': login,
                'Status': response.status_code,
                'datetime': str(datetime.now().strftime('%d.%m.%Y-%H:%M:%S')),
                'initial_link': initial_link,
                'final_url': driver.current_url,
                'missing_cookies': list_of_required_cookies
                # Add all cookie names to the list
            })

        all_data.append(data)
        print(data)
        print(driver.get_cookies())

    if not os.path.exists('results'):
        os.mkdir('results')
    with open('results/error_results.json', 'w') as error_file:
        dump(error_data, error_file, indent=4)
    with open('results/all_results.json', 'w') as main_file:
        dump(all_data, main_file, indent=4)

    end_time = time.time()
    # Test time measurement and logging
    execution_time = end_time - start_time
    print(execution_time)
    driver.quit()
