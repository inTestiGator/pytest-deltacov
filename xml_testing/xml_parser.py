""" This program parses through an XML file created by codecov and retrieves
    the total coverage along with the lines covered and uncovered for each file tested"""

from bs4 import BeautifulSoup

def file_formatter(path_to_file):
    """ Reads in coverage file and returns a parsable soup"""
    with open(path_to_file) as fp:
        soup = BeautifulSoup(fp, "xml")

    return soup


def xml_parser(soup):
    """ Scrapes and XML file for relevant data """

    # Finds the percent coverage for all tested files
    lr = soup.find('coverage')
    line_rate = lr.get("line-rate")

    # Finds the lines which are covered and uncovered for each tested file
    for file in soup.find_all('class'):
        lines_covered = []
        lines_uncovered = []

        filename = file.get("filename")

        # Parses through the lines to determine whether they're covered or uncovered
        for lines in file.find_all('lines'):
            for line in lines.find_all('line'):
                if line.get("hits") == "1":
                    lines_covered.append(line.get("number"))
                else:
                    lines_uncovered.append(line.get("number"))


def main():
    """ This method changes the coverage file to a readable soup and feeds it
        through a parser in order to pull out relevant data """
        
    soup = file_formatter("coverage.xml")
    xml_parser(soup)

if __name__ == '__main__':
    main()
