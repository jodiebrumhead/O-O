"""Timing sorting algorithms on different 1D data structures"""

#import modules
from timeit import default_timer as timer
import random
import numpy as np
import pandas as pd

"""Create lists, arrays and series to compare"""
def create(n):
    ls = []
    for i in range(n):
        num = random.random()
        ls.append(num)
    arr=np.random.random(n)
    ser=pd.Series(np.random.random(n))
    return ls, arr, ser

"""A find mimimum function created by me"""
def findmin(obj):
    minN = 10000 # this being the key
    for i in obj:
        if (i<minN):
            minN=i
    return minN
#could create find max in similar manner
#beware of -values?

"""A sort function created by me"""
#'for index in range(len((arr))' different to 'for i in arr'
# is it best to find index at same stage as finding min?
# i.e. var = and pos =
# test with duplicate values!
def sort(obj):
    new = []
    while len(obj)>0:
        b = findmin(obj)
        new.append(b)
        if type(obj) is list:
            obj.remove(b) #removes first item of value b
        if type(obj) is np.ndarray:
            index = np.argwhere(obj==b)
            obj = np.delete(obj, [index]) #must equal something else as np array immutable
        if type(obj) is pd.core.series.Series:
            pos = obj[obj == b].index[0]
            obj = obj.drop(labels=pos)
        else:
            break
    return new

if __name__ == '__main__':
# Use create function to create random 10 values in different data structures
    ls, arr, ser = create(10)
    datastruc10 = [ls, arr, ser]

"""#Create dataframe and add data
"""
# create empty dataframe with index for different 1d data structures
times = pd.DataFrame(index=['python list', 'numpy array', 'pandas series'])

m = []
time = []
for i in datastruc10:
    s = timer()
    m.append(findmin(i))
    e = timer()
    time.append(e - s)
#Create list of code strings? anyway to automate this?

times['listobj'] = datastruc10
times['mymin'] = m
times['mytime'] = time


# Use in-built functions relevant for different data structures and time
# could function this?
start = timer()
ls_min = min(ls)
end = timer()
ls_findmin = (end - start)
start = timer()
arr_min = np.amin(arr)
end = timer()
arr_findmin = (end - start)
start = timer()
ser_min = ser.min()
end = timer()
ser_findmin = (end - start)

times['minfunc'] = [ls_min, arr_min, ser_min]
times['minfunctime'] = [ls_findmin, arr_findmin, ser_findmin]

#Output dataframe to csv

times.to_csv(r'times.csv')
