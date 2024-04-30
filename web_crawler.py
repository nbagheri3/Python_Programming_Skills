#!/usr/bin/python3
import argparse
import time
import requests
from bs4 import BeautifulSoup

# Function to scrape conference data from a given page
def get_conference_data(conference, page_number):
    URL = "http://www.wikicfp.com/cfp/call"
    params = {'conference': conference, 'page': page_number}
    response = requests.get(URL, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        return []

    bs = BeautifulSoup(response.text, features="lxml")
    rows = bs.body.find_all('tr', attrs={'bgcolor': ['#f6f6f6', '#e6e6e6']})
    conference_data = []

    # Loop through rows, extracting relevant information and appending to conference_data
    for row_idx in range(0, len(rows), 2):
        acronym, name, _ = [col_tag.text.strip() for col_tag in rows[row_idx].find_all('td')]
        date, location, deadline = [col_tag.text.strip() for col_tag in rows[row_idx + 1].find_all('td')]
        conference_data.append((acronym, name, location, conference))

    return conference_data

# Main function to orchestrate the scraping process
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--no_of_pages', type=int, help='Number of pages to scrape')
    parser.add_argument('--output', type=str, help='Output file path')
    args = parser.parse_args()

    # Check if required arguments are provided
    if not args.no_of_pages or not args.output:
        parser.error("Please provide both --no_of_pages and --output arguments.")

    conferences = ["Big Data", "Machine Learning", "Artificial Intelligence"]
    output_file = open(args.output, 'w')
    output_file.write("{}\t{}\t{}\t{}\n".format("acronym", "name", "location", "conference_category"))

    for conference in conferences:
        for page_number in range(1, args.no_of_pages + 1):
            conference_data = get_conference_data(conference, page_number)
            for data in conference_data:
                output_file.write("{}\t{}\t{}\t{}\n".format(*data))
            print("Finished Crawling Conference: {} PageNumber: {}".format(conference, page_number))
            time.sleep(0.05)

    output_file.close()

if __name__ == "__main__":
    main()
