import time
from typing import List
import numpy as np


def bubble_sort(items: list):
    list_len = len(items)
    for i in range(list_len):
        is_sorted = True
        for j in range(list_len - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j+1] = items[j+1], items[j]
                is_sorted = False
            if items[j] < items [j + 1]:
                is_sorted = False
                continue
            elif is_sorted:
                break
    
    return items

def insertion_sort(items: list):
    for i in range(1, len(items)):
        key_item = items[i]
        j = i - 1
        while j >= 0 and items[j] > key_item:
            items[j+1] = items[j]
            j -= 1
        items[j+1] = key_item

    return items

def time_run(start: float, end:float):
    return f"--- Total time ran: {end - start} ---"




if __name__=="__main__":
    items = np.random.choice(20000, 20000)
    items.tolist()

    start = time.time()
    bubbleSort_done = bubble_sort(items)
    end = time.time()
    
    _bubbleTime = time_run(start, end)
    
    start = time.time()
    insertedSort_done = insertion_sort(items)
    _insertedTime = time_run(start, end)

    print(
        f"""
        {insertion_sort.__name__}\n
        {_insertedTime}
        List \'first five\': {insertedSort_done[:5]}\n
        ------------------------
        {bubble_sort.__name__}\n
        {_bubbleTime}
        List \'first five\': {bubbleSort_done[:5]}
        """)