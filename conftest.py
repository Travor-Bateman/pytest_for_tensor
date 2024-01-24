import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture(scope="session")
def browser():
    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': 'C:\\Users\\Skywalker\\PycharmProjects\\tensor_tasks',
             'download.prompt_for_download': False,
             'download.directory_upgrade': True,
             'safebrowsing_for_trusted_sources_enabled': False,
             'download.extensions_to_open': 'exe',
             'safebrowsing.enabled': True
             }
    capabilities = DesiredCapabilities().CHROME
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--safebrowsing-disable-download-protection")
    chrome_options.add_argument("safebrowsing-disable-extension-blacklist")
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    capabilities.update(chrome_options.to_capabilities())
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
