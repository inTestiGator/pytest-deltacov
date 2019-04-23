import re
import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup

def file_formatter(path_to_file):
    with open(path_to_file) as fp:
        soup = BeautifulSoup(fp, "xml")

    return soup


def xml_parser(soup):
    line_rate = soup.find(attrs={'coverage':"line-rate"})
    print(line_rate)

    #for each file covered:
        # store lines covered in one list
        # store lines not covered in other


def main():
    soup = file_formatter("coverage.xml")
    xml_parser(soup)

if __name__ == '__main__':
    main()
