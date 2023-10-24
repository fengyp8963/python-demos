from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from time import sleep
from random import random

options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Edge(options=options)
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
    USERNAME = '15936197109'
    PASSWORD = 'zjw123456'

    driver.get('https://cprs.patentstar.com.cn/')

    driver.find_element(
        by=By.CSS_SELECTOR,
        value='body > div > div.header.unselect > div > div > div.box.user-box.fr > a > p > span'
    ).click()

    driver.find_element(
        by=By.CSS_SELECTOR,
        value='#loginname'
    ).send_keys(USERNAME)

    driver.find_element(
        by=By.CSS_SELECTOR,
        value='#password'
    ).send_keys(PASSWORD)

    driver.find_element(
        by=By.CSS_SELECTOR,
        value='#login'
    ).click()

    return


def get_page_count() -> int:
    count = int(
        driver.find_element(
            by=By.CSS_SELECTOR,
            value='body > div.container-fluid > div.contenter > div > div.col-xs-10.colbox > div.searchitems-box > div.searchpage > div.tcdPageCode > a:nth-child(6)'
        ).text
    )

    return count


def download_all_patent() -> None:
    for idx in range(get_page_count() - 1):

        for i in range(1, 6):

            try:
                driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="listcontainer"]/div[%d]/div/div[3]/span/a' % i
                ).click()
            except:
                driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="listcontainer"]/div[%d]/div/div[3]/span/a' % i
                ).click()

            sleep(random())

        sleep(random() * 2)

        driver.find_element(
            by=By.CSS_SELECTOR,
            value='body > div.container-fluid > div.contenter > div > div.col-xs-10.colbox > div.searchitems-box > div.searchpage > div.tcdPageCode > a.nextPage'
        ).click()

    return


if __name__ == "__main__":

    login()

    keyword = [
        '临床救治', '疫苗研发', '疫情检测', '疫情监测', '病毒病原学', '流行病学', '动物模型构建'
    ]

    for kw in keyword:
        search_by_keyword(kw)

        download_all_patent()

        sleep(random() * 3)
