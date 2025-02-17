import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(autouse=True, scope="function")
def browser_test_setup():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.timeout = 10
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'  # позволяет продолжать выполнение, как только DOM загружен, а не дожидаться полной загрузки всех ресурсов.
    # driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options
    browser.open("https://demoqa.com/automation-practice-form")
    # browser.driver.execute_script("$('#fixedban').remove()")
    # browser.driver.execute_script("$('footer').remove()")
    yield
    browser.quit()
