# Web Scraper

This repository contains a Python script for web scraping using the Selenium library. The script allows you to extract data from websites, such as titles and links, by automating the browser interaction.

## Author

- Name: Tomilola Oluwafemi
- Email: tee.o2809@gmail.com
- GitHub: [https://github.com/Tomilola-ng/WEB-SCRAPER](https://github.com/Tomilola-ng/WEB-SCRAPER)

## Requirements

- Python 3.x
- Selenium library (`pip install selenium`)
- Chrome WebDriver (compatible with your Chrome version)

## Usage

1. Clone the repository or download the script file.
2. Make sure you have the Chrome WebDriver installed and its path is added to your system's PATH variable.
3. Install the required Python libraries by running `pip install selenium`.
4. Open the script file in a text editor or Python IDE.
5. Modify the `driver.get("https://www.example.com")` line to navigate to the desired website.
6. Customize the CSS selectors in the `find_elements` calls to target the specific elements you want to scrape.
7. Run the script, and it will open a Chrome browser instance, navigate to the website, and print the titles and links found on the page.
