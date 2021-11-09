import asyncio
x = ['Welcome']
async def hello(first_print, second_print):
    print(first_print)
    await asyncio.sleep(1)
    print(second_print)

# asyncio.run(hello(first_print, "Good-bye"))
loop = asyncio.get_event_loop()
loop.run_until_complete(hello(x, 'Good-bye'))
# import asyncio
#
# async def crawl_page(url):
#     print('crawling {}'.format(url))
#     sleep_time = int(url.split('_')[-1])
#     await asyncio.sleep(sleep_time)
#     print('OK {}'.format(url))
#
# async def main(urls):
#     for url in urls:
#         await crawl_page(url)
#     asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
