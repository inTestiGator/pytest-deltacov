import re
import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup

def file_formatter(path_to_file):
    with open(path_to_file) as fp:
        soup = BeautifulSoup(fp, "xml")

    return soup


def xml_parser(soup):
    lr = soup.find('coverage')
    line_rate = lr.get("line-rate")

    for file in soup.find_all('class'):
        lines_covered = []
        lines_uncovered = []

        filename = file.get("filename")

        for lines in file.find_all('lines'):
            for line in lines.find_all('line'):
                if line.get("hits") == "1":
                    lines_covered.append(line.get("number"))
                else:
                    lines_uncovered.append(line.get("number"))


def main():
    soup = file_formatter("coverage.xml")
    xml_parser(soup)

if __name__ == '__main__':
    main()
