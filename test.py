import allure

from functions import SBIS_Main_Page, SBIS_Contacs_Page, SBIS_Download_Page,\
    Tensor_Main_Page, Tensor_About_Page, Chrome_Download_Page

@allure.story('Выполнение задания №1')
def test_tensor_ft(browser):
    first_task = SBIS_Main_Page(browser)
    with allure.step('Переходим на сайт "https://sbis.ru/"'):
        first_task.go_to_site('https://sbis.ru/')
    with allure.step('Кликаем на "Контакты"'):
        first_task.click_on_contacts()
    first_task = SBIS_Contacs_Page(browser)
    with allure.step('Кликаем на баннер "ТЕНЗОР"'):
        first_task.click_on_tensor_banner()
    first_task.driver.switch_to.window(first_task.driver.window_handles[1])
    first_task = Tensor_Main_Page(browser)
    with allure.step('Проверяем наличие элемента "Сила в людях"'):
        first_task.check_block_strongpeople()
    with allure.step('Кликаем на "Подробнее" в этом блоке'):
        link = first_task.click_on_block_strongpeople_about()
        first_task.go_to_site(link)
    first_task = Tensor_About_Page(browser)
    with allure.step('Находим и проверяем размеры картинок в этом блоке'):
        first_task.check_size_images()

@allure.story('Выполнение задания №2')
def test_tensor_st(browser):
    second_task = SBIS_Main_Page(browser)
    with allure.step('Переходим на сайт "https://sbis.ru/"'):
        second_task.go_to_site('https://sbis.ru/')
    with allure.step('Кликаем на "Контакты"'):
        second_task.click_on_contacts()
    second_task = SBIS_Contacs_Page(browser)
    with allure.step('Проверяем регион'):
        second_task.check_region()
    with allure.step('Меняем регион'):
        second_task.change_region()
    with allure.step('Проверяем новый регион'):
        second_task.check_new_region()

@allure.story('Выполнение задания №3')
def test_tensor_th(browser):
    thrid_task = SBIS_Main_Page(browser)
    with allure.step('Переходим на сайт "https://sbis.ru/"'):
        thrid_task.go_to_site('https://sbis.ru/')
    with allure.step('Кликаем на "Скачать СБИС"'):
        thrid_task.find_and_click_on_download_sbis()
    thrid_task = SBIS_Download_Page(browser)
    with allure.step('Выбираем "Плагин СБИС", узнаем размер файла и скачиваем файл'):
        size_file = thrid_task.click_on_sbis_plugin()
    thrid_task = Chrome_Download_Page(browser)
    with allure.step('Проверяем, что файл скачался и сравниваем размеры'):
        thrid_task.into_download_manager(size_file)

@allure.story('Выполнение задания №3')
def test_tensor_th(browser):
    thrid_task = SBIS_Main_Page(browser)
    with allure.step('Переходим на сайт "https://sbis.ru/"'):
        thrid_task.go_to_site('https://sbis.ru/')
    with allure.step('Кликаем на "Скачать СБИС"'):
        thrid_task.find_and_click_on_download_sbis()
    thrid_task = SBIS_Download_Page(browser)
    with allure.step('Выбираем "Плагин СБИС", узнаем размер файла и скачиваем файл'):
        size_file = thrid_task.click_on_sbis_plugin()
    thrid_task = Chrome_Download_Page(browser)
    with allure.step('Проверяем, что файл скачался и сравниваем размеры'):
        thrid_task.go_to_site('chrome://downloads')
        thrid_task.into_download_manager(size_file)