from selenium.webdriver.common.by import By

class Main_Page_Locators:
    LOCATOR_CONTACTS_BUTTON = (By.LINK_TEXT, 'Контакты')
    LOCATOR_DOWNLOAD_SBIS = (By.LINK_TEXT, 'Скачать СБИС')

class Contacs_Page_Locators:
    LOCATOR_TENSOR_BANNER = (By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a/img')
    LOCATOR_OWN_REGIONE = (By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
    LOCATOR_OWN_CITY = (By.ID, 'city-id-2')
    LOCATOR_KAM4ATKA = (By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span')

class Download_Page_Locators:
    LOCATOR_WINDOWS_VERSION = (By.CLASS_NAME, 'controls-tabButton__overlay')
    LOCATOR_SBIS_PLUGIN = (By.CLASS_NAME, 'controls-TabButton__caption')
    LOCATOR_BLOCKS_INSTALLERS = (By.CLASS_NAME, 'sbis_ru-DownloadNew-block.sbis_ru-DownloadNew-flex')
    LOCATOR_BLOCK_WEB_INSTALLER = (By.CLASS_NAME, 'sbis_ru-DownloadNew-h3')
    LOCATOR_DOWNLOAD_WEB_INSTALLER = (By.CLASS_NAME, 'sbis_ru-DownloadNew-loadLink__link.js-link')
    LOCATOR_FILE_DOWNLOAD_INFO = (By.CLASS_NAME, 'description')