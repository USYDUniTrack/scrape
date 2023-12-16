from sys import argv
from urllib.request import urlopen

from bs4 import BeautifulSoup
from icecream import ic

from constants import *
from unit_parser import UnitParser

# ic.configureOutput(includeContext=True)


def main():
    parser = UnitParser(argv[1])
    parser.parse_page()
    ic(parser.data)


if __name__ == "__main__":
    main()
