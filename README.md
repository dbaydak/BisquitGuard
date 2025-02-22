# BisquitGuard: Automate Cookie Consent

BisquitGuard is a Python-Selenium script that automates the process of checking for the existence of specific cookies in your web browser. This can be helpful for testing, debugging, or monitoring web applications that rely on cookies for functionality or user tracking.

## Table of Contents

-   [Description](#description)
-   [Installation](#installation)
-   [Usage](#usage)
-   [Command-line arguments](#command-line-arguments)
-   [Specific requirements](#specific-requirements-for-campaign_listpy-file)
-   [Limitations](#limitations)
-   [Contributing](#contributing)
-   [License](#license)
-   [FAQ](#faq)

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

## Installation

BisquitGuard requires Python 3.7 or higher. To install BisquitGuard and its dependencies, follow these steps:

1.  Clone the repository:
    ```bash
    git clone [https://github.com/dbaydak/BisquitGuard.git](https://github.com/dbaydak/BisquitGuard.git)
    ```

2.  Navigate to the project directory:
    ```bash
    cd BisquitGuard
    ```

3.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use BisquitGuard, navigate to the project directory and run the script with the desired website URL:

```bash
python bisquitguard.py --url [https://www.example.com](https://www.example.com)
```

## Command-line arguments:

--url: The URL of the website to visit. (Required)
--driver: Path to the webdriver executable (e.g., chromedriver, geckodriver). Defaults to chromedriver. If chromedriver is in your system's PATH, you can omit this.
--accept-all: If present, attempts to click "Accept All" or similar buttons.
--reject-all: If present, attempts to click "Reject All" or similar buttons.
--custom-selectors: Path to a JSON file containing custom CSS selectors for cookie banner elements. This allows for fine-tuning BisquitGuard's behavior for websites with unique cookie banner structures.

## Specific requirements for `campaign_list.py` file

This is a dictionary. Data is to be added as follows:

* **Key** - campaign login
* **Value** - affiliate link. Deeplinks can be used as well

## Limitations

Some limits might occur on some websites (e.g. financial campaigns in Brazil: _santandera_pt_2_). 
The tool might get stuck. If it happens, the tool needs to be stopped and the link should be deleted from the list.
Also, it is noted that some pages might take up to 20-30 seconds to be processed (UAE: _inhousesa_SA_). No actions are required.

## Contributing

Contributions are welcome! If you'd like to contribute to BisquitGuard, please follow these guidelines:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them with clear and concise messages. 4. Submit a pull request.   

## License

This project is licensed under the MIT License - see the LICENSE file for details.   

## FAQ

Q: Which browsers are supported?

A: BisquitGuard uses Selenium, which supports various browsers. You'll need to download the appropriate webdriver for your browser of choice (e.g., ChromeDriver for Chrome, GeckoDriver for Firefox).

Q: I'm getting an error about the webdriver. What should I do?

A: Ensure that you have the correct webdriver installed and that it's compatible with your browser version. Also, make sure the webdriver is in your system's PATH, or provide the path explicitly using the --driver argument.

Q: Can I use BisquitGuard with multiple websites?

A: Yes, you can run the script multiple times with different URLs.

Q: The cookie banner on a specific site isn't being handled correctly. What can I do?

A: Try using the --custom-selectors option. Inspect the website's HTML to find the CSS selectors for the "Accept" and "Reject" buttons (or other relevant elements) and create a custom_selectors.json file as described in the Configuration section.

Q: How do I find the correct CSS selectors for the cookie banner elements?

A: Most modern browsers have developer tools that allow you to inspect the HTML of a webpage. Right-click on the element you want to target (e.g., the "Accept" button) and select "Inspect" or "Inspect Element." This will open the developer tools and highlight the corresponding HTML code. You can then find the CSS selector for that element.  Look for attributes like id, class, or other unique identifiers.  You can also use the browser's "Copy selector" feature in the developer tools.