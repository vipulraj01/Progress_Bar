import time
for i in range(10):
    time.sleep(.1)
from tqdm import tqdm # tqdm is a library in python which is used for creating Progress Meters or Progress Bars
import time
for i in tqdm(range(10)):
    time.sleep(.1)

