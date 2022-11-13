import numpy as np
import pandas as pd 
import json 
import matplotlib.pyplot as plt 


def getSolveTime(solve):
    return solve[0][1]

def getAverageOf(average_of):
    # Opening JSON file
    f = open('cstimer_4x4.txt')

    # returns JSON object as 
    # a dictionary
    data = json.load(f)


    print(type(data['session1']))

    session = data['session1']

    length = len(session)

    avg_times = []

    for i in range(0, length-average_of):
        cur_five = session[i:i+average_of].copy()
        cur_five.sort()

        # print("here", len(cur_five[1:-1]))

        mid_3 = cur_five[1:-1]

        # print("mid 3", mid_3)

        times = list(map(getSolveTime, mid_3))

        avg_times.append(np.average(np.array(times).astype(int) / 1000))


    plt.figure()
    plt.plot(list(range(len(avg_times))), avg_times)
    plt.show()


getAverageOf(5)
getAverageOf(12)
  