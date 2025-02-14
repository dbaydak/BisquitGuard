# `BiscuitGuard` MVP

## Description
The tool is intended to check the presence of particular cookies on websites.
Based on [_Selenium WebDriver_](https://www.selenium.dev/documentation/webdriver/).
It collects affiliate links one by one from `campaign_list` file and run `context_processor` script in Chrome browser.
The results are stored in 2 files: `run_results` (contains **all** data) and `error_results` (contains **failures** only).
These files are JSON format. It is done in order to have a possibility to process them later on as well.
Timeload is set to 1.5 seconds (`time.sleep(1.5)`). It should be enough for cookies to get created.
To see the results in real-time, data is reflected in the console (`print()`).
It is preferable to use some VPN service to provide neutral IP.
Required dependencies and software is listed in `requirements` (`pip install`).

The tool returns:
* **Status** - response status code
* **Login** - campaign login
* **Redirect_link** - final redirect link
* **Cookie** - _tagtag_aid_ cookie data
* **admitad_uid** - click id from _tagtag_aid_
* **Attribution** - _deduplication_cookie_ value

### Requirements for `campaign_list.py`

This is a dictionary. Data is to be added as follows:

* **Key** - campaign login
* **Value** - affiliate link. Deeplinks can be used as well

### Limitations

Some limits might occur on some websites (e.g. financial campaigns in Brazil: _santandera_pt_2_). 
The tool might get stuck. If it happens, the tool needs to be stopped and the link should be deleted from the list.
Also, it is noted that some pages might take up to 20-30 seconds to be processed (UAE: _inhousesa_SA_). No actions are required.
