import time
from selenium import webdriver
import pytest
import json
from endpoint.EndPointFactory import EndPoint


@pytest.fixture(scope='session')
def config():
    with open('config.json') as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def test_setup(config):
    global driver
    if config['browser'] == 'chrome':
        driver = webdriver.Chrome(r'C:\Users\mindfire\PycharmProjects\HybridALL\drivers\chromedriver.exe')
    elif config['browser'] == 'ie':
        driver = webdriver.Ie(r'C:\Users\mindfire\PycharmProjects\HybridALL\drivers\IEDriverServer.exe')
    else:
        raise Exception(f'"{config["browser"]}" is not a supported browser')

    driver.implicitly_wait(config['wait_time'])
    driver.maximize_window()
    driver.get(EndPoint.BASE_URI_UI)

    yield
    time.sleep(4)
    driver.quit()


def test_countries(test_setup):
    driver.find_element_by_xpath("//span[contains(text(),'angular-starter')]").click()
    driver.find_element_by_xpath("//h5[contains(text(),'Countries')]").click()
    driver.find_element_by_xpath("//input[@id='searchField']").send_keys("america")
    driver.find_element_by_xpath("//i[@class='fas fa-search']").click()
    driver.find_element_by_xpath("//div[contains(text(),'United States of America')]").click()
    print("\n", driver.current_url)
    data = driver.find_element_by_tag_name("input").get_attribute("value")
    assert data == "america"


def test_cities(test_setup):
    driver.find_element_by_xpath("//span[contains(text(),'angular-starter')]").click()
    driver.find_element_by_xpath("//h5[contains(text(),'Cities')]").click()
    driver.find_element_by_xpath("//div[contains(text(),'Tirana')]").click()
    print("\n", driver.current_url)
    data = driver.find_element_by_tag_name("input").get_attribute("value")
    assert data == ""


def test_movies(test_setup):
    driver.find_element_by_xpath("//span[contains(text(),'angular-starter')]").click()
    driver.find_element_by_xpath("//div[3]//a[1]//div[1]//div[1]//div[1]//div[1]//h5[1]").click()
    driver.find_element_by_xpath("//input[@id='searchField']").send_keys("africa")
    driver.find_element_by_xpath("//i[@class='fas fa-search']").click()
    driver.find_element_by_xpath("//div[contains(text(),'Africa Screams')]").click()
    print("\n", driver.current_url)
    data = driver.find_element_by_tag_name("input").get_attribute("value")
    assert data == "africa"


def test_shows(test_setup):
    driver.find_element_by_xpath("//span[contains(text(),'angular-starter')]").click()
    driver.find_element_by_xpath("//div[4]//a[1]//div[1]//div[1]//div[1]//div[1]//h5[1]").click()
    driver.find_element_by_xpath("//input[@id='searchField']").send_keys("bonanza")
    driver.find_element_by_xpath("//i[@class='fas fa-search']").click()
    driver.find_element_by_xpath("//div[contains(text(),'Bonanza')]").click()
    print("\n", driver.current_url)
    data = driver.find_element_by_tag_name("input").get_attribute("value")
    assert data == "bonanza"


def test_continent(test_setup):
    driver.find_element_by_xpath("//span[contains(text(),'angular-starter')]").click()
    driver.find_element_by_xpath("//h5[contains(text(),'Continent')]").click()
    driver.find_element_by_xpath("//input[@id='searchField']").send_keys("asia")
    driver.find_element_by_xpath("//i[@class='fas fa-search']").click()
    driver.find_element_by_xpath("//div[contains(text(),'Asia')]").click()
    print("\n", driver.current_url)
    data = driver.find_element_by_tag_name("input").get_attribute("value")
    assert data == "asia"
