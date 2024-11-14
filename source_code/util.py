from selenium import webdriver
from selenium.webdriver.common.by import By
from .soup import Soup
import requests
import datetime
import pandas
import re
from plyer import notification

driver = webdriver.Chrome()


def get_html(url):
    r = requests.get(url)
    return Soup(r.text)


def click_button(url, class_name):
    driver.get(url)
    driver.find_element(By.XPATH, class_name).click()


def get_current_page_source():
    return driver.page_source


def save_to_file(product, filename):
    try:
        date = datetime.datetime.now().strftime('%d_%B_%Y')
        df = pandas.DataFrame(product).map(remove_illegal_characters)
        df.to_excel(f'{filename}_{date}.xlsx', index=False)
        df.to_csv(fr'D:\Github\aprinur\Web_Scraping\starcompjogja\{filename}_{date}.csv', index=False)
        return True
    except Exception as e:
        print(f'Error saving file {e}')
        return false


def remove_illegal_characters(text):
    if isinstance(text, str):
        return re.sub(r'[\x00-\x1F\x7F]', '', text)

    return text


def show_info(message):
    notification.notify(
        title='Scraping Status',
        message=message,
        app_icon=None,
        timeout=30
    )