from bs4 import BeautifulSoup
from .data_req import Product_spec


class Soup(BeautifulSoup):
    def __init__(self, html):
        super().__init__(html, 'html.parser', multi_valued_attributes=None)

    def scrape_product_info(self):
        """ Method to scrape product information"""
        article = self.find('article', class_='ps-lg-3')
        title = article.find('h4').get_text()
        sku_text = article.find('div', class_='rating-wrap my-3').find('span', class_='label-rating text-muted').get_text().strip()
        sku = sku_text.removeprefix('SKU : ') if len(sku_text) > 6 else None
        stock_availability = article.find('span', class_='label-rating text-success').text if article.find('span', class_='label-rating text-success') else article.find('span', class_='label-rating text-warning').get_text()
        price = article.find('var', class_='price h3').get_text().removeprefix('IDR ')
        spec = self.find('article', id='tab_specs').get_text().replace('\r\n', ' ').replace('\n', ' ').replace('\x0b', '')

        link_shopee = article.find('span', class_='badge bg-warning p-2 ml-2 float-right link-mp').find('a')['href'] if article.find('span', class_='badge bg-warning p-2 ml-2 float-right link-mp') else 'None'
        link_tokopedia = article.find('span', class_='badge bg-success p-2 ml-2 float-right link-mp').find('a')['href'] if article.find('span', class_='badge bg-success p-2 ml-2 float-right link-mp') else 'None'
        link_bukalapak = article.find('span', class_='badge bg-danger p-2 ml-2 float-right link-mp').find('a')['href'] if article.find('span', class_='badge bg-danger p-2 ml-2 float-right link-mp') else 'None'
        whatsapp = self.find('div', class_='chatwhatsapp').find('a')['href'].removesuffix(
            ' Starcompjogja.com, bisa dibantu?')
        image_url = [url['href'] for url in self.find('div', class_='thumbs-wrap').find_all('a')] if self.find('div', class_='thumbs-wrap') else None

        return Product_spec(
            Name=title,
            Price=price,
            Stock=stock_availability,
            Sku=sku,
            Image_url=image_url,
            Shopee_link=link_shopee,
            Tokopedia_link=link_tokopedia,
            Bukalapak_link=link_bukalapak,
            Whatsapp=whatsapp,
            Description=spec
        )

    def scrape_product_url(self):
        """ Method to scrape product url after choose category """
        return [url['href'] for url in self.find_all('a', class_='title text-truncate')]

    def scrape_category_url(self):
        """Method to scrape category url from main page"""
        return [url['href'] for url in self.find('ul', class_='navbar-nav me-auto').find_all('a', class_='dropdown-item')]

    def check_final_page(self):
        """ Method to check final page"""
        page = self.find('ul', class_='pagination')

        if not page:
            return False

        if not page.find('li', attrs={'aria-disabled': "true", 'aria-label': "Next »"}):
            return False

    def scrape_page_url(self):
        """ Method to scrape all pages from each category"""
        return [url['href'] for url in self.find('div', class_='d-none flex-sm-fill d-sm-flex align-items-sm-center justify-content-sm-between').find_all('a', class_='page-link')] if self.find('div', class_='d-none flex-sm-fill d-sm-flex align-items-sm-center justify-content-sm-between') else None



