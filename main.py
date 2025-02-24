import time

from source_code import URL
from source_code.util import get_html, save_to_file, show_info, user_input


def all_in_one(product_count: int = None, sub_category_count: int = None, page: int = None, filename: str = 'Scraping result', page_title: str = 'Scraping result', description: str = None):
    url = URL  # Main url
    soup = get_html(url)
    sub_category_urls = soup.scrape_category_url()  # Scrape category url
    all_product = []

    for sub_category_url in sub_category_urls[:sub_category_count]:  # opening first page

        print(f'Opening category {sub_category_url}')
        product_page = get_html(sub_category_url)
        time.sleep(1)
        product_urls = product_page.scrape_product_url()  # Scrape url product
        page_urls = product_page.scrape_page_url()

        for product_url in product_urls[:product_count]:
            print(f'Scraping product {product_url}')
            soup = get_html(product_url)
            time.sleep(1)
            product = soup.scrape_product_info()  # Scrape product information
            all_product.append(product)

        if page_urls is None:  # Skip if page_urls is empty

            print(f'Category {sub_category_url} has only 1 page')
            continue
        else:  # If page_urls is not empty, go to next page

            for page_url in page_urls[:-1]:
                if int(page_url[-1]) > page:
                    break
                print(f'Opening page {page_url}')
                product_page2 = get_html(page_url)
                time.sleep(1)
                product_urls2 = product_page2.scrape_product_url()  # scrape url product from page 2

                for product_url2 in product_urls2[:product_count]:  # Opening each page url
                    print(f'Scraping product {product_url2}')
                    soup = get_html(product_url2)
                    time.sleep(1)
                    product_info = soup.scrape_product_info()  # Scrape product information
                    all_product.append(product_info)

    save_result = save_to_file(product=all_product, filename=filename, description=description, tittle=page_title)

    if save_result:
        show_info('Scraping success')
        print('Saving file success ')
    else:
        show_info('Scraping failed')


def main():
    sub_category, item, page,  tittle, desc = user_input()
    all_in_one(product_count=item, sub_category_count=sub_category, page=page, page_title=tittle, description=desc)


if __name__ == "__main__":
    main()


