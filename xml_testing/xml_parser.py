""" This program parses through an XML file created by codecov and retrieves
    the total coverage along with the lines covered and uncovered for each file tested"""

# pylint: disable=import-error
from bs4 import BeautifulSoup


def file_formatter(path_to_file):
    """ Reads in coverage file and returns a parsable soup"""
    with open(path_to_file) as filepath:
        soup = BeautifulSoup(filepath, "xml")

    return soup


def xml_parser(soup):
    """ Scrapes and XML file for relevant data """

    # Finds the percent coverage for all tested files
    linerate = soup.find("coverage")
    # pylint: disable=unused-variable
    line_rate = linerate.get("line-rate")  # noqa: F841

    # Finds the lines which are covered and uncovered for each tested file
    for file in soup.find_all("class"):
        # pylint: disable=unused-variable
        lines_covered = []
        lines_uncovered = []

        filename = file.get("filename")  # noqa: F841

        # Parses through the lines to determine whether they're covered or uncovered
        for lines in file.find_all("lines"):
            for line in lines.find_all("line"):
                if line.get("hits") == "1":
                    lines_covered.append(line.get("number"))
                else:
                    lines_uncovered.append(line.get("number"))


def main():
    """ This method changes the coverage file to a readable soup and feeds it
        through a parser in order to pull out relevant data """

    soup = file_formatter("coverage.xml")
    xml_parser(soup)


if __name__ == "__main__":
    main()
