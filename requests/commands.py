import threading
from datetime import timedelta
import httpx
import redis
con = redis.Redis(host="localhost", port=6379, decode_responses=True)


# def oqim1():
#     url = "https://kun.uz"
#     response = httpx.get(url)
#     name = url.rsplit("/")[-1]
#     base = response.text
#     con.set(f"{name}",base,timedelta(seconds=60))
#
#
#
# def oqim2():
#     url = "https://daryo.uz"
#     response = httpx.get(url)
#     name = url.rsplit("/")[-1]
#     base = response.text
#     con.set(f"{name}",base,timedelta(seconds=60))
#
#
# def oqim3():
#     url = "https://qalampir.uz"
#     response = httpx.get(url)
#     name = url.rsplit("/")[-1]
#     base = response.text
#     con.set(f"{name}",base,timedelta(seconds=60))
#
#
# def oqim4():
#     url = "https://jsonplaceholder.typicode.com"
#     response = httpx.get(url)
#     name = url.rsplit("/")[-1]
#     base = response.text
#     con.set(f"{name}",base,timedelta(seconds=60))
#
#
# def oqim5():
#     url = "https://github.com/"
#     response = httpx.get(url)
#     name = url.rsplit("/")[-1]
#     base = response.text
#     con.set(f"{name}",base,timedelta(seconds=60))
#
#
#
#
# if __name__ == '__main__':
#
#     thread1 = threading.Thread(target=oqim1)
#     thread2 = threading.Thread(target=oqim2)
#     thread3 = threading.Thread(target=oqim3)
#     thread4 = threading.Thread(target=oqim4)
#     thread5 = threading.Thread(target=oqim5)
#
#     thread1.start()
#     thread2.start()
#     thread3.start()
#     thread4.start()
#     thread5.start()
#
#     thread1.join()
#     thread2.join()
#     thread3.join()
#     thread4.join()
#     thread5.join()

# print(con.get("kun.uz"))
