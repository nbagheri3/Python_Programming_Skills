# ----------------------------------------------------------------------
# Name:        scrape.py
# Purpose:     Homework 8 - practice web scraping
#
# Author(s): Nahal Bagheri and Dasom Lee
# ----------------------------------------------------------------------
"""
Compiling information from multiple web pages and save it in csv file

The program will take in a name of the csv file as a CL argument
The program will start by opening and reading the SJSU faculty index
That page links to other web pages containing information about faculty
The information extracted will include the last name, the first name,
email, phone number and education information of each faculty or staff.
"""

import urllib.request
import urllib.error
import bs4
import re
import sys
import os

# Enter your constants here
BASE = 'https://sjsu.edu/people/'

def read_url(url):
    """
    Open the given url and return the corresponding soup object.
    :param url:(string) - the address of the web page to be read
    :return: (Beautiful Soup object) corresponding Beautiful Soup
    object or None if an error is encountered.
    """
    try:
        with urllib.request.urlopen(url) as url_file:
            url_bytes = url_file.read()
    except urllib.error.URLError as url_err:
        print(f'Error opening url: {url}\n{url_err}')
    except Exception as other_err: # safer on the web
        print(f'Other error with url: {url}\n{other_err}')
    else:
        soup = bs4.BeautifulSoup(url_bytes,'html.parser')
        return soup


def get_people_links(url):
    """
    Read the given url and return the relevant referenced links.
    :param url:(string) - the address of the faculty index page
    :return: (list of strings) - the relevant people links
    """
    people_pattern = r'/people/[a-zA-Z]+\.'
    abs_links = [urllib.parse.urljoin(url, anchor.get('href', None))
                      for anchor in read_url(url)('a') if re.match(
            people_pattern, anchor.get('href', None), re.IGNORECASE)]
    return abs_links


def extract_name(soup):
    """
    Extract the first and last name from the soup object
    :param soup: (Beautiful Soup object) representing the faculty/staff
    web page
    :return: a tuple of strings representing the first and last names
    """
    header_tag = soup('h1')
    if header_tag:
        name = header_tag[0].get_text()

        if ',' in name :
            if len(name.split()) == 2:
                first_name = name.split(', ')[0].strip()
                last_name = name.split(', ')[1].strip()

            if len(name.split()) > 2:
                first_name = name.split(', ')[0].strip()
                last_name = name.split(', ')[-1].strip()

        elif len(name.split()) == 2:
            first_name = name.split()[1].strip()
            last_name = name.split()[0].strip()

        elif len(name.split()) > 2:
            first_name = name.split()[0].strip()
            last_name = name.split()[-1].strip()

        else:
            return None

        return first_name, last_name


def extract_email(soup):
    """
    Extract the email address from the soup object.
    :param soup: (BeautifulSoup object) representing a person's web page
    :return: (string) the email address or empty string if it cannot
    be found
    """
    email_pattern = re.compile(r'@\S+\.\S+')
    all_matches = soup.find_all(string=email_pattern)
    if all_matches:
        return all_matches[0].strip()
    else:
        return ""


def extract_phone(soup):
    """
    Extract the phone number from the soup object.
    :param soup: (BeautifulSoup object) representing a person's web page
    :return: (string) the phone number or empty string if it cannot
    be found
    """
    pattern = r'([(]?\d{3}[)]?[-./]?[\s]?\d{3}[\s.-]*\d{4})'
    telephone_element = re.compile(r'Telephone', re.IGNORECASE)
    phone_number = ''
    for phone in soup.find_all(string=telephone_element):
        phone_number = phone.find_next().get_text().strip()
        matches = re.findall(pattern, phone_number)
        if matches:
            return matches[0]
    return ""


def extract_education(soup):
    """
      Extract the education information from the soup object.
      :param soup: (BeautifulSoup object) representing a person's web
      page
      :return: (string) the education information or empty string if it
      cannot be found
      """
    finding_education = soup.find('h2', string='Education')
    if finding_education:
        next_element = finding_education.find_next()
        if next_element.name == 'ul':
            return next_element.find_next().get_text().\
                    replace(',', '-').replace('\n', ' ').strip()
        else:
            return next_element.get_text().replace(',', '-')\
                .replace('\n', ' ').strip()
    return ""


def get_info(url):
    """
    Extract the information from a single faculty/staff web page
    :param url: (string) the address of the faculty/staff web page
    :return: a comma separated string containing: the last name,
    first name, email, phone and education
    """
    # 1.  Call read_url to get the soup object
    soup = read_url(url)
    # 2.  Call extract_name, extract_email, extract_phone, and
    #     extract_education to get the relevant information

    if soup is not None:
        names = extract_name(soup)
        if names is not None:
            first_name, last_name = names
            email = extract_email(soup)
            phone_number = extract_phone(soup)
            education = extract_education(soup)

    # 3.  Combine the info in one comma seperated string and return it.
            information = [first_name, last_name, email, phone_number,
                           education]
            return ','.join([info_result.strip() for info_result
                             in information if info_result])


def harvest(url, filename):
    """
    Harvest the information starting from the url specified and write
    that information to the file specified.
    :param url: (string)the main faculty index url
    :param filename: (string) name of the output csv file
    :return: None
    """
    # 1.  Call get_people_links to get the relevant links from the url
    relevant_link = get_people_links(url)
    # 2.  Open the file with a context manager
    with open(filename, 'w', encoding='UTF-8') as url_file:
        # 3.  Write the column headers to the file
        url_file.write(f'Last Name, First Name, Email, Phone Number, '
                       f'Education\n')
    # 4.  Iterate over the links and call get_info on each one.
        for info_url in relevant_link:
            # 5.  Write that information in the file
            if get_info(info_url):
                url_file.write(get_info(info_url) + '\n')


def main():
    # Check the command line argument then call the harvest function
    if len(sys.argv) != 2 :
        print('Error: Invalid number of arguments')
        print('Usage: scrape.py filename')

    elif os.path.splitext(sys.argv[1])[1] != '.csv':
        print('Please specify a csv filename')

    else:
        harvest(BASE, sys.argv[1])


if __name__ == '__main__':
    main()