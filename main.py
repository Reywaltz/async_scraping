import asyncio
import os
from internal import solelinks
from internal.sneaker_links import Sneaker_Links
from internal.solelinks import Solelinks

from requests_html import AsyncHTMLSession

asession = AsyncHTMLSession()

async def solelinks():
    
    Solelinks_parser = Solelinks("https://vagu.space", "solelinks", asession)
    a = await Solelinks_parser.get_data()
    print(a)
    # await task
    


async def main():
    if not os.path.exists('./img'):
        os.mkdir('img')

    # sneaker_links_parser = Sneaker_Links("https://sneakerlinks.com", "test")
    # sneaker_links_parser.get_data()

    asession = AsyncHTMLSession()

    Solelinks_parser = Solelinks("https://vagu.space", "solelinks", asession)
    # await Solelinks_parser.get_data()
    # await task
    asession.run(Solelinks_parser.get_page)

asession.run(solelinks)

# asyncio.get_event_loop().run_until_complete(solelinks())


# asession = AsyncHTMLSession()


# async def get_qq():
#     r = await asession.get('https://vagu.space/')
#     await r.html.arender()
#     print(r.html.raw_html)


# async def get_toutiao():
#     r = await asession.get('https://www.toutiao.com/')
#     x = await r.html.arender()
#     print(x.html.raw_html)

# Result = asession.run(get_qq)
