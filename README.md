# Starcompjogja.com Web Scraper

This is a simple web scraper that pulls product details from Starcompjogja.com and saves them as an Excel and CSV file in your Downloads folder.

## How It Works

* Scrapes product info from different categories on Starcompjogja.com.
* Collects details like name, price, stock, SKU, images, and marketplace links.
* Saves everything neatly in an Excel (.xlsx) and CSV (.csv) file.

## Requirements

Before running the scraper, make sure you have:

* Python 3.8 or newer
* Required dependencies (installed via `requirements.txt`)
* A stable internet connection

## Installation

1. **Download the Project**
   Download the project as zip file and extract
2. **Set Up a Virtual Environment**
   Navigate to the project
   
   ```sh
   cd path\to\the\project
   ```
   
   Creating virtual environment
   
   ```sh
   python -m venv .venv
   ```
3. **Activate the Virtual Environment**
   
   ```sh
   .venv\Scripts\activate
   ```
4. **Install Dependencies**
   
   ```sh
   pip install -r requirements.txt
   ```

## How to Use

1. **Run the Scraper**
   ```sh
   python main.py
   ```
2. **Enter Your Preferences**
   * Number of subcategories to scrape
   * Number of products per category
   * Number of pages to scrape
   * Title and description for the spreadsheet
3. **Find Your Results**
   * The data will be saved as an Excel or CSV file in your Downloads folder.

## Tips

* Keep your internet connection stable while running the scraper.
* If something goes wrong, double-check your inputs and try again.



