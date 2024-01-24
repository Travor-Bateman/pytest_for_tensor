from BaseApp import BasePage
from selenium.webdriver.common.by import By
import os

from sbis.sbis_locators import Main_Page_Locators as SBIS_MPL
from sbis.sbis_locators import Contacs_Page_Locators as SBIS_CPL
from sbis.sbis_locators import Download_Page_Locators as SBIS_DPL
from tensor.tensor_locators import Main_Page_Locators as TENSOR_MPL
from tensor.tensor_locators import About_Page_Locators as TENSOR_APL
from chrome.chrome_locators import Chrome_Download_Page_Locators as CHROME_DPL

class SBIS_Main_Page(BasePage):
    url = 'https://sbis.ru/'
    def click_on_contacts(self):
        find_element = self.find_elements(SBIS_MPL.LOCATOR_CONTACTS_BUTTON)
        assert len(find_element) > 0, 'Элемент "Контакты" не найден'
        return self.find_elements(SBIS_MPL.LOCATOR_CONTACTS_BUTTON)[0].click()

    def find_and_click_on_download_sbis(self):
        find_element = self.find_elements(SBIS_MPL.LOCATOR_DOWNLOAD_SBIS)
        assert len(find_element) > 0, 'Элемент "Скачать СБИС" не найден'
        find_element[0].location_once_scrolled_into_view
        return find_element[0].click()

class SBIS_Contacs_Page(BasePage):
    def click_on_tensor_banner(self):
        find_element = self.find_elements(SBIS_CPL.LOCATOR_TENSOR_BANNER, time=2)
        assert len(find_element) > 0, 'Баннер "ТЕНЗОР" не найден'
        return find_element[0].click()

    def check_region(self):
        name_region = self.find_elements(SBIS_CPL.LOCATOR_OWN_REGIONE)
        assert len(name_region) > 0, 'Элемент названия региона не найден'
        assert name_region[0].text == 'Республика Башкортостан', 'Регион не совпал'
        name_city = self.find_elements(SBIS_CPL.LOCATOR_OWN_CITY)
        assert len(name_city) > 0, 'Элемент названия города не найден'
        assert name_city[0].text == 'Уфа', 'Список партнеров не совпал'
        return name_region[0]

    def change_region(self):
        self.find_element(SBIS_CPL.LOCATOR_OWN_REGIONE).click()
        return self.find_element(SBIS_CPL.LOCATOR_KAM4ATKA).click()

    def check_new_region(self):
        new_name = 'Петропавловск-Камчатский'
        new_name_city = self.find_element(SBIS_CPL.LOCATOR_OWN_CITY).text
        if new_name_city != new_name:
            self.wait_text_in_element(SBIS_CPL.LOCATOR_OWN_CITY, new_name, 10)
            new_name_city = self.find_element(SBIS_CPL.LOCATOR_OWN_CITY).text
        assert new_name_city == new_name, 'Не поменялся город'
        new_title = self.driver.current_url
        assert '41-kamchatskij-kraj' in new_title, 'В url не содержится название региона'
        new_url = self.driver.title
        assert 'Камчатский край' in new_url, 'В заголовке сайта не содержится "Камчатский край'

class SBIS_Download_Page(BasePage):

    def click_on_sbis_plugin(self):
        plugsbis = self.find_elements(SBIS_DPL.LOCATOR_SBIS_PLUGIN)
        assert len(plugsbis) > 0, 'Вкладка "СБИС Плагин" не найден'
        for i in range(len(plugsbis)):
            text_on_block = plugsbis[i].text
            if text_on_block == 'СБИС Плагин':
                self.action.move_to_element(plugsbis[i]).perform()
                self.action.click(plugsbis[i]).perform()
                break
        blocks = self.find_elements(SBIS_DPL.LOCATOR_BLOCKS_INSTALLERS)
        assert len(blocks) > 0, 'Блок "Веб установщик" не найден'
        for i in range(len(blocks)):
            text_on_block = blocks[i].find_element(By.CLASS_NAME, 'sbis_ru-DownloadNew-h3').text
            if 'Веб-установщик' in text_on_block:
                click_on_download = blocks[i].find_element(By.CLASS_NAME, 'sbis_ru-DownloadNew-loadLink__link.js-link')
                size_file = float(str(click_on_download.get_attribute('textContent')).partition('(')[2].partition(' ')[2].partition(' ')[0])
                click_on_download.click()
                break
        return size_file


class Tensor_Main_Page(BasePage):

    def check_block_strongpeople(self):
        block = self.find_elements(TENSOR_MPL.LOCATOR_BLOCK_STRONG_PEOPLE, time=10)
        assert len(block) > 0, 'Блок "Сила в людях" не найден'
        return block[0]

    def click_on_block_strongpeople_about(self):
        block = self.find_elements(TENSOR_MPL.LOCATOR_BLOCK_STRONG_PEOPLE, time=10)
        elem = block[0].find_elements(By.CLASS_NAME, 'tensor_ru-link.tensor_ru-Index__link')
        link = elem[0].get_attribute('href')
        return link

class Tensor_About_Page(BasePage):
    def check_size_images(self):
        imgs = self.find_elements(TENSOR_APL.LOCATOR_ABOUT_IMAGES)
        img_name_filter = 'block3'
        width = []
        height = []
        for i in range(len(imgs)):
            name_class = imgs[i].get_attribute('class')
            if img_name_filter in name_class:
                width.append(imgs[i].get_attribute('width'))
                height.append(imgs[i].get_attribute('height'))
        status = 0
        for k in range(1, len(width)):
            if width[0] == width[k] and height[0] == height[k]:
                status = True
            else:
                status = False
                break
        assert status == True, 'Размер картинок не совпал'

class Chrome_Download_Page(BasePage):

    def into_download_manager(self, size_file):
        shadow_root = self.find_elements(CHROME_DPL.LOCATOR_DOWNLOAD_MANAGER, 10)[0].shadow_root
        shadow_root = shadow_root.find_elements(By.ID, 'downloadsList')[0]
        shadow_root = shadow_root.find_elements(By.ID, 'frb0')[0].shadow_root
        shadow_root = shadow_root.find_element(By.ID, 'content')
        click_button_save = shadow_root.find_element(By.ID, 'details')
        status = click_button_save.find_element(By.ID, 'safe')
        while True:
            st = status.get_attribute('innerHTML').partition('>')[0]
            if 'hidden' not in st:
                file_size = os.path.getsize('sbisplugin-setup-web.exe')
                assert float(size_file) == round(file_size / (1024 * 1024), 2), 'Размер файла не совпадает с указанным на сайте'
                break


