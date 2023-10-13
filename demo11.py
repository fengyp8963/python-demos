from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.maximize_window()


def search_by_keyword(keyword: str) -> None:
    driver.find_element(
        by=By.CSS_SELECTOR,
        value='#indexpage > a'
    ).click()

    driver.find_element(
        by=By.CSS_SELECTOR,
        value='body > div > div.contenter-fp > div > div:nth-child(2) > div > input'
    ).send_keys(keyword)

    driver.find_element(
        by=By.CSS_SELECTOR,
        value='body > div > div.contenter-fp > div > div:nth-child(2) > div > a'
    ).click()

    return


def login() -> None:
    USERNAME = 'fengyp'
    PASSWORD = 'sssydt2022'

    driver.get('http://pvms.sssydt.com:3100/')

    driver.find_element(
        by=By.CSS_SELECTOR,
        value='#form_item_account'
    ).send_keys(USERNAME)

    driver.find_element(
        by=By.CSS_SELECTOR,
        value='#form_item_password'
    ).send_keys(PASSWORD)

    driver.find_element(
        by=By.CSS_SELECTOR,
        value='form > div:last-child button'
    ).click()

    return


if __name__ == "__main__":
    login()
