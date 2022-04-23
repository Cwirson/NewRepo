# import json
# import re


# x = '{ "name": "Jhon", "age":30, "city":"New York" }'
# y = json.loads(x)
# print(y["age"])

# z = json.dumps(y)
# print(z)

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)

# if x:
#     print("matched")
# else:
#     print("no match")
    
# x = re.findall("ai", txt)
# print(type(x))

# x = re.search("\s", txt)
# print(x)

# f = open("myfile.txt", "r")
# print(f.read())
# f.close()

# f = open("myfilee.txt", "x")
# f.close()
# f = open("myfilee.txt", "a")
# for x in range(1000):
#     f.write("jebac dis huj zwis \n")
# f.close()
# f = open("myfilee.txt", "r")
# print(f.read())
# f.close()

# from time import sleep
# for x in range(10):
#     print("rzyg")
#     print("sleeping for 1 sec")
#     sleep(1)
# else:
#     print("koniec")

from re import T
import threading
from time import sleep, perf_counter

start = perf_counter()

def sleeping(seconds):
    sleep(seconds)
    print("done")

threads = []

for _ in range(10):
    t = threading.Thread(target=sleeping, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

# t1.start
# t2.start
# t3.start
# t4.start

# t1.join()
# t2.join()
# t3.join()
# t4.join()

finish = perf_counter()
print(f"Finished operation in {round(finish-start, 2)} second(s)")