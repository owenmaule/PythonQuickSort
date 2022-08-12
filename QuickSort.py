from random import *
from datetime import *

def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp


def quick_sort(array, begin, end):
    lo = begin
    hi = end - 1
    pivot = array[end]
    while True:
        while lo < end and array[lo] <= pivot:
            lo += 1
        while hi >= begin and array[hi] > pivot:
            hi -= 1
        if lo >= hi:
            break
        swap(array, lo, hi)
    swap(array, hi + 1, end)
    if hi > begin:
        quick_sort(array, begin, hi)
    if hi + 2 < end:
        quick_sort(array, hi + 2, end)


def qsort(array, begin, end):
    while end > begin:
        lo = begin
        hi = end - 1
        pivot = array[end]
        while True:
            while lo < end and array[lo] <= pivot: lo += 1
            while hi >= begin and array[hi] > pivot: hi -= 1
            if lo >= hi: break
            tmp = array[lo]
            array[lo] = array[hi]
            array[hi] = tmp
        array[end] = array[hi + 1]
        array[hi + 1] = pivot
        if hi + 2 < end: qsort(array, hi + 2, end)
        end = hi


def compare_list(a, b):
    length = len(a)
    if length != len(b):
        return False
    for index in range(length):
        if a[index] != b[index]:
            print("Fail ", index, " ", a[index], " != ", b[index], "\na: ", a, "\nb: ", b)
            return False
#    print(length, " elements match\na: ", a, "\nb: ", b)
    return True


def test(elements, highest, sort):
    data = []
    for element in range(elements):
        data.append(randint(0, highest))
    copy = data.copy()
    sort(data, 0, len(data) - 1)
    copy.sort()
    return compare_list(copy, data)


def test_algo(tests, algo):
    fails = 0
    for i in range(tests):
        if not test(50, 1000, algo):
            fails += 1
    print("Algo ", algo.__name__, "\nFailures ", fails, "/", tests)


def perf_test(subject):
    print("Perf testing", subject.__qualname__)
    start_time = datetime.now()
    subject()
    end_time = datetime.now()
    ms = (end_time - start_time).microseconds
    print("Took ", ms, " ms")
    return ms

quick_ms = perf_test(lambda: test_algo(100, quick_sort))
q_ms = perf_test(lambda: test_algo(100, qsort))
print("Gain ", (1 - q_ms / quick_ms) * 100, "%")
