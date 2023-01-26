import numpy as np
import pandas as pd 
import json 
import matplotlib.pyplot as plt 


def getSolveTime(solve):
    return solve[0][1]

def getTotalNumSolves(session):
    print("Total Solves: {}".format(len(session)))
    return len(session)

def getSubOf(session, subOf):

    length = len(session)

    times = np.array(list(map(getSolveTime, session))) / 1000 
    # times = session 

    num_solves_sub_of = np.sum(times < subOf)
    percentage_sub_of = round((num_solves_sub_of / length) * 100, 2)
    
    print("Sub-{}: {}% , Num of Solves: {}".format(subOf, percentage_sub_of, num_solves_sub_of))

def getListOfTimes(session):
    return np.array(list(map(getSolveTime, session)))

def generateHist(session):
    plt.figure()
    plt.hist(getListOfTimes(session) / 1000 )
    plt.show()

def generateBoxPlot(session):
    plt.figure()
    plt.boxplot(getListOfTimes(session) / 1000 )
    plt.show()

def generateStats(session):
    times = (getListOfTimes(session) / 1000)

    min, quantile_25, median, quantial_75, max = np.quantile(times, [0, 0.25, 0.5, 0.75, 1]).round(2)
    avg = np.average(times).round(2)

    print("Min: {}, 25th Percentile: {}, Median: {}, 75th Percentile: {}, Max: {}".format(min, quantile_25, median, quantial_75, max))
    print("Average: {}".format(avg))

    # print(times)

# print
# Total Solves: ##
# Sub-20: %% , Num of Solves: ##
# Sub-15: %% , Num of Solves: ##

f = open('cstimer_20230123_112143.txt')
data = json.load(f)
session = data['session1']
# session = np.array(list(map(getSolveTime, session))) / 1000 
session = session[1500:]
getTotalNumSolves(session)
getSubOf(session, 20)
getSubOf(session, 15)
getSubOf(session, 14)
getSubOf(session, 13)
getSubOf(session, 12)
getSubOf(session, 11)
getSubOf(session, 10)
# generateHist(session)
# generateBoxPlot(session)
generateStats(session)
