import os
from dataclasses import dataclass

from aiohttp import ClientSession
from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession

from internal.parser import Parser
from internal.sneaker import Sneaker


@dataclass
class Solelinks(Parser):
    URL: str
    img_path: str
    asession: AsyncHTMLSession

    async def get_page(self):
        r = await self.asession.get(self.URL)
        await r.html.arender()
        return r.html.raw_html

    def parse_html(self, html: str) -> tuple[str, str, str]:
        bs = BeautifulSoup(html, 'html5lib')
        releases = bs.find_all('div')

        print(releases)

    async def get_images(self, sneakers: list[Sneaker]):
        async with ClientSession() as session:
            for sneaker in sneakers:
                async with session.get(sneaker.image) as response:
                    if response.status == 200:
                        content_data = await response.content.read()
                        if '/' in sneaker.name:
                            sneaker.name = sneaker.name.replace('/', '_')
                        if not os.path.exists(f'./img/{self.img_path}'):
                            os.mkdir(f'./img/{self.img_path}')
                        with open(f'img/{self.img_path}/{sneaker.name}.png', 'wb') as file:
                            file.write(content_data)

    async def get_data(self) -> str:
        response = await self.get_page()
        # data = self.parse_html(response)
        # res = [Sneaker(*x) for x in data]
        # await self.get_images(res)
        # return f'Sneaker_links res: {res}'

