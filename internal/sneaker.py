from dataclasses import dataclass


@dataclass
class Sneaker:
    name: str
    date: str
    image: str

    def __repr__(self) -> str:
        return f'Sneakers name: {self.name}, release: {self.date}, img: {self.image}'
