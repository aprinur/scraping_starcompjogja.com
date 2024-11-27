import pandas as pd
from .soup import Soup
import requests
import datetime
import pandas
import re
from plyer import notification
from .data_req import Product_spec
from openpyxl import load_workbook
from openpyxl.styles import Alignment, Font


def get_html(url):
    r = requests.get(url)
    return Soup(r.text)


def save_to_file(product: list, filename: str, tittle: str, description: str):
    try:
        date = datetime.datetime.now().strftime('%d_%B_%Y')
        product_dict = [i.__dict__ for i in product]
        df = pandas.DataFrame(product_dict).map(remove_illegal_characters)
        name = f'{filename}_{date}.xlsx'

        with pandas.ExcelWriter(name, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet_1', startrow=3)
            workbook = writer.book
            worksheet = writer.sheets['Sheet_1']

            worksheet.merge_cells('A1:D1')
            worksheet.merge_cells('A2:E2')
            worksheet['A1'] = tittle
            worksheet['A2'] = description

            worksheet['A1'].font = Font(name='Times New Roman', size=16, bold=True)
            worksheet['A1'].alignment = Alignment(horizontal='center', vertical='center')
            worksheet['A2'].alignment = Alignment(horizontal='left', vertical='center')

        df.to_csv(rf'D:\Github\aprinur\scraping_starcompjogja.com\{filename}_{date}.csv', index=False)

        return True
    except Exception as e:
        print(f'Error saving file: {e}')
        return False


def remove_illegal_characters(text):
    if isinstance(text, str):
        return re.sub(r'[\x00-\x1F\x7F]', '', text)

    return text


def show_info(message):
    notification.notify(
        title='Scraping Status',
        message=message,
        app_icon=None,
        timeout=3
    )


def user_input():
    sub_category = int(input('How much sub category you want to scrape? : '))
    item = int(input('How much product you want to scrape? : '))
    page = int(input('How much page you want to scrape? : '))
    tittle = input('Input tittle of your spreadsheet: ')
    desc = input('Input description of your spreadsheet: ')
    print(f'This program will scrape first {item} products from the first {sub_category} sub-categories and first {page} pages of the site')

    return sub_category, item, page, tittle, desc