import datetime
import os
import re

import pandas
import requests
from openpyxl.styles import Alignment, Font
from plyer import notification

from .soup import Soup


def get_html(url):
    r = requests.get(url)
    return Soup(r.text)


def save_to_file(product: list, filename: str, tittle: str = 'Starcompjogja.com scraping result', description: str = None):
    try:
        save_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        date = datetime.datetime.now().strftime('%d_%B_%Y')
        excel_path = os.path.join(save_path, f'{filename}_{date}.xlsx')
        csv_path = os.path.join(save_path, f'{filename}_{date}.csv')

        product_dict = [i.__dict__ for i in product]
        df = pandas.DataFrame(product_dict).map(remove_illegal_characters)

        with pandas.ExcelWriter(excel_path, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet_1', startrow=3)

            worksheet = writer.sheets['Sheet_1']

            worksheet.merge_cells('A1:D1')
            worksheet.merge_cells('A2:E2')
            worksheet['A1'] = tittle
            worksheet['A2'] = description

            worksheet['A1'].font = Font(name='Times New Roman', size=16, bold=True)
            worksheet['A1'].alignment = Alignment(horizontal='center', vertical='center')
            worksheet['A2'].alignment = Alignment(horizontal='left', vertical='center')

        df.to_csv(csv_path, index=False)

        return True
    except Exception as e:
        print(f'Error saving file: {e}')
        return False


def show_info(message):
    notification.notify(
        title='Scraping Status',
        message=message,
        app_icon=None,
        timeout=3
    )


def remove_illegal_characters(text):
    if isinstance(text, str):
        return re.sub(r'[\x00-\x1F\x7F]', '', text)

    return text


def user_input():
    while True:
        sub_category = input('Enter amound of subcategory to scrape : ')
        if not sub_category.strip():
            print('Form cannot be empty')
            continue
        if not sub_category.isdigit():
            print('Amount must be a number')
            continue
        sub_category = int(sub_category)
        break
    while True:
        item = input('Enter amount of product to scrape : ')
        if not item.strip():
            print('Form cannot be empty')
            continue
        if not item.isdigit():
            print('Amount must be a number')
            continue
        item = int(item)
        break
    while True:
        page = input('Enter amount of page to scrape : ')
        if not page.strip():
            print('Form cannot be empty')
            continue
        if not page.isdigit():
            print('Amount must be a number')
            continue
        page = int(page)
        break
    while True:
        title = input('Input tittle for spreadsheet: ')
        if not title.strip():
            title = 'Starcompjogja.com scraping result'
            break
        break
    while True:
        desc = input('Input description of your spreadsheet: ')
        if not desc.strip():
            desc = f'This data scraped from the first {item} products from the first {sub_category} sub-categories and first {page} pages of the site'
            break
        break
    print(f'This program will scrape first {item} products from the first {sub_category} sub-categories and first {page} pages of the site')

    return sub_category, item, page, title, desc