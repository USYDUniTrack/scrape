from typing import Self
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

from bs4 import BeautifulSoup
from icecream import ic

from constants import *


class UnitParser:
    def __init__(self, unit_name="comp2017"):
        """
        Creates a UnitParser object.
        Attributes:
            unit_name: str
            url: str
            html: str
            soup: BeautifulSoup
            data: dict
        """
        self.unit_name = unit_name.lower()
        self.url = BASE_URL.format(self.unit_name)
        try:
            page = urlopen(self.url)
        except HTTPError as e:
            print("ERROR while opening url")
            print(e.__dict__)
            return
        except URLError as e:
            print("ERROR while opening url")
            print(e.__dict__)
            return
        self.html = page.read().decode("utf-8")
        self.soup = BeautifulSoup(self.html, "html.parser")
        self.data = {}

    def parse_page(self) -> None:
        """
        Parses the whole unit page for the given unit name on initialisation.
        Adds the following keys to the self.data attribute:
            - unit_title
        """
        self.data["unit_title"] = self.title()

    def title(self) -> str | None:
        """
        Parses the unit page for the title.
        """
        h1 = self.soup.find_all("h1")
        unit_title = None
        for val in h1:
            if (
                val.has_attr("class")
                and " ".join(val["class"]) == "pageTitle b-student-site__section-title"
            ):
                unit_title = val.get_text()
        return unit_title
