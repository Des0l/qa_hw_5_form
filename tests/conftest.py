import pytest
from selene import browser, have, be
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
    browser.driver.execute_script("$('.Google-Ad').remove()")
    browser.driver.execute_script("$('#Ad.Plus-970x250-2').remove()")
    yield
    browser.quit()
