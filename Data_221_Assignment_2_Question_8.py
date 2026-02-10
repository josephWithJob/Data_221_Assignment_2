# Assignment 2, Question 8
# Joseph Krosel

import requests
from bs4 import BeautifulSoup

# taking information from the website
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; DataScienceScraper/1.0)"
}

data_science_website_information = requests.get("https://en.wikipedia.org/wiki/Data_science",headers = headers).text
soup_data_science_website = BeautifulSoup(data_science_website_information, "html.parser")

# Gets the main section of website
main_part_of_website = soup_data_science_website.find("div", id="mw-content-text")

# Opens 'heading.txt' file to write into
# Sorts through all headers in the main content section of website
# and prints them into the file
with open("headings.txt", 'w') as file:
    h2_headers_of_main_part_of_website = main_part_of_website.find_all("h2")
    for header in h2_headers_of_main_part_of_website:
        if header.text != "References" and header.text != "External Links" and header.text != "See also" and header.text != "Notes":
            print(header.text)
            file.write(f"{header.text}\n")