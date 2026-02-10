# Assignment 2, Question 7
# Joseph Krosel

# MIGHT NOT BE DONE, DOUBLE CHECK

import requests
from bs4 import BeautifulSoup

# taking information from the website
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; DataScienceScraper/1.0)"
}

data_science_website_information = requests.get("https://en.wikipedia.org/wiki/Data_science",headers = headers).text
                                                                #html5lib
soup_data_science_website = BeautifulSoup(data_science_website_information, "html.parser")

# Title
stats_title_of_website = soup_data_science_website.find("title")
print(stats_title_of_website.text)


# Main section of website
main_part_of_website = soup_data_science_website.find("div", id="mw-content-text")

first_paragraph = None
for paragraph in main_part_of_website.find_all("p", recursive=True):
    text = paragraph.get_text(strip=True)
    text = text.replace(" ", "")
    if len(text) >= 50:
        first_paragraph = paragraph
        break