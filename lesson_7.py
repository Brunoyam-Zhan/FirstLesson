# a = [11, 7, 3, 5, 8, 1]
# for j in range(len(a)):
#     for i in range(len(a)-1):
#         if a[i] > a[i+1]:
#             a[i], a[i+1] = a[i+1], a[i]
#
# print(a)

# import requests
# r = requests.get("https://www.youtube.com/")
# print(r.text)

# Процессы и потоки. Параллельное и псевдно параллельное программированиие


# import time
# from threading import Thread
#
# class MyThread(Thread):
#     def start(self):
#         print("start")
#
# def start_rocket(id):
#     time.sleep(3)
#     print(f"Ракета с id {id} запущена!\n")
#
#
# threads_list = []
# for i in range(5):
#     thread_obj = Thread(target=start_rocket, args=(i,), daemon=True)
#     threads_list.append(thread_obj)
#
#
# for i in threads_list:
#     i.start()
#
# for i in threads_list:
#     i.join()

# from multiprocessing import Process
# import os
# from time import sleep
#
# def func(start, end, timeout):
#     while start < end:
#         print(f"Process {os.getpid()}: {start}")
#         start += 1
#         sleep(timeout)
#
# if __name__ == '__main__':
#     process1 = Process(target=func, args=(3, 10, 1))
#     process2 = Process(target=func, args=(5, 20, 0.5))
#     process1.start()
#     process2.start()
#
#     print("END")

# counter = 0
# lock = Lock()
#
# def func():
#     lock.acquire()
#     global counter
#     f = counter
#     counter = f + 1
#     lock.release()


# t1 = datetime.now()
#
# t2 = datetime.now()
#
# s = t2 - t1
#
# print(s.microseconds)



import requests
import asyncio
import aiohttp
from _datetime import datetime

resource_list = ["https://github.com/", "https://www.youtube.com/", "https://spring.io/",
                 "https://www.apple.com/ru/", "https://vk.com/", "https://www.ilovepdf.com/ru/jpg_to_pdf"
                 ]


sync_t1 = datetime.now()
for resource in resource_list:
    r = requests.get(resource)
    print(len(r.text))
sync_t2 = datetime.now()
sync_delta = sync_t2 - sync_t1
print(f"Sync Time{sync_delta.microseconds}")

async def get_data(url):
    print(f"Start {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            print(len(data))

t1 = datetime.now()
jobs = [get_data(url) for url in resource_list]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(jobs))
t2 = datetime.now()

delta = t2 - t1
print(f"Async Time{delta.microseconds}")
















