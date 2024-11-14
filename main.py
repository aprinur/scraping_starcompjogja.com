from source_code.util import get_html, click_button, get_current_page_source, save_to_file, show_info
from source_code.soup import Soup
from source_code.__init__ import URL
import time


def get_product_info():
    url = 'https://starcompjogja.com/product/gigabyte-vga-geforce-gtx-1050-ti-oc-4g'
    soup = get_html(url)
    product = [soup.scrape_product_info()]
    save_result = save_to_file(product, 'Single product')
    if save_result:
        show_info('Scraping success')
    else:
        show_info('Scraping failed')
    # print(product)


def get_product_url():
    url = 'https://starcompjogja.com/category/processor'
    soup = get_html(url)
    soup.scrape_product_url()


def get_category_url():
    url = URL
    soup = get_html(url)
    soup.scrape_category_url()


def get_final_page():
    url = 'https://starcompjogja.com/category/memory?page=8'
    soup = get_html(url)
    print(soup.check_final_page())


def get_page_url():
    url = 'https://starcompjogja.com/category/processor'
    soup = get_html(url)
    url = soup.scrape_page_url()
    print(url[:-1]) if url is not None else print('Category has only 1 page')


def main():
    url = URL  # Main url
    soup = get_html(url)
    category_urls = soup.scrape_category_url()  # Scrape category url
    all_product = []

    for category_url in category_urls[:5]:  # Opening first five category, remove '[:5]' to scrape all category

        print(f'Opening category {category_url}')
        product_page = get_html(category_url)
        time.sleep(2)
        product_urls = product_page.scrape_product_url()  # Scrape product url
        page_urls = product_page.scrape_page_url()

        for product_url in product_urls:

            print(f'Scraping product {product_url}')
            soup = get_html(product_url)
            time.sleep(3)
            product = soup.scrape_product_info()  # Scrape product information
            all_product.append(product)

        if page_urls is None:  # If page_urls is empty

            print(f'Category {category_url} has only 1 page')
            continue
        else:  # If page_urls is not empty

            for page_url in page_urls[:-1]:  # Opening page 2 until second last page
                print(f'Opening page {page_url}')
                product_page2 = get_html(page_url)
                time.sleep(1)
                product_urls2 = product_page2.scrape_product_url()  # scrape product url from page 2

                for product_url2 in product_urls2:  # Opening each page url
                    print(f'Scraping product {product_url2}')
                    soup = get_html(product_url2)
                    time.sleep(2)
                    product_info = soup.scrape_product_info()  # Scrape product information
                    all_product.append(product_info)

    save_result = save_to_file(all_product, 'Pc_components_&_peripheral_from_first_five_category_in_starcompjogja.com')
    if save_result:
        show_info('Scraping success')
    else:
        show_info('Scraping failed')


if __name__ == "__main__":
    get_product_info()