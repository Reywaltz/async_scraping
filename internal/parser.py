from abc import ABC
from dataclasses import dataclass


@dataclass(init=False)
class Parser(ABC):
    URL: str

    def get_page(self):
        pass

    def parse_html(self):
        pass

    def get_images(self):
        pass

    @property
    def image_path(self):
        pass
