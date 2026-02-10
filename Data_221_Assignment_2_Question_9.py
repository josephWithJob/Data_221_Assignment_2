# Assignment 2, Question 9
# Joseph Krosel

import requests
from bs4 import BeautifulSoup
import csv

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; DataScienceScraper/1.0)"
}

machine_learning_website_information = requests.get("https://en.wikipedia.org/wiki/Machine_learning",headers = headers).text

soup_machine_learning_website = BeautifulSoup(machine_learning_website_information, "html.parser")

# Gets the main section of website
main_part_of_website = soup_machine_learning_website.find("div", id="mw-content-text")


table_data = []
# Checks if content of website is scraped properly
if main_part_of_website:
    # Finds all tables
    all_tables_in_main_section = main_part_of_website.find_all("table")

    # Sorts through tables
    for table in all_tables_in_main_section:
        rows_of_table = table.find_all("tr")

        # End if rows are less than 4
        if len(rows_of_table) < 3:
            continue

        # Take headers from table
        header_cells = rows_of_table[0].find_all("th")
        if header_cells:
            headers = [th.get_text(strip=True) for th in header_cells]
        else:
            first_data_cells = rows_of_table[1].find_all(["td", "th"])
            headers = [f"col{i+1}" for i in range(len(first_data_cells))]

        # Extracting all data
        for row in rows_of_table[1:]:
            cells = row.find_all(["td", "th"])
            row_data = [cell.get_text(strip=True) for cell in cells]

            # Adds padding for missing values through empty strings
            while len(row_data) < len(headers):
                row_data.append("")

            table_data.append(row_data)

        break

# adds info into csv
with open("wiki_table.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(table_data)


