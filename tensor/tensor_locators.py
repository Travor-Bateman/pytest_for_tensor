from selenium.webdriver.common.by import By

class Main_Page_Locators:
    LOCATOR_BLOCK_STRONG_PEOPLE = (By.CLASS_NAME, 'tensor_ru-Index__block4-bg') #
    LOCATOR_BLOCK_STRONG_PEOPLE_ABOUT = (By.CLASS_NAME, 'tensor_ru-link.tensor_ru-Index__link')
    #LOCATOR_BLOCK_STRONG_PEOPLE_ABOUT = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')

class About_Page_Locators:
    LOCATOR_BLOCK_WORK = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[1]')
    LOCATOR_ABOUT_IMAGES = (By.TAG_NAME, 'img')