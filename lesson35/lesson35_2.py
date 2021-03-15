import asyncio
import aiohttp


async def get_url(url, session):
    file_name = str('111')
    async with session.get(url) as response:
        with open(file_name, 'wb') as fd:
            async for data in response.content.iter_chunked(1024):
                fd.write(data)
    return f'Successfully downloaded {url} to file {file_name}'


async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [get_url(url, session) for url in urls] # возможно подставить несколько url
        return await asyncio.gather(tasks)

if __name__ == '__main__':

    urls = ['https://api.pushshift.io/reddit/comment/search/']
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(main(urls))
