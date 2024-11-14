from dataclasses import dataclass


@dataclass
class Product_spec:
    Name: str
    Price: str
    Stock: str
    Sku: str
    Image_url: list
    Description: str
    Bukalapak_link: str
    Tokopedia_link: str
    Shopee_link: str
    Whatsapp: str
