import numpy as np
import pandas as pd 
import json 
import matplotlib.pyplot as plt 

from utils import *


f = open('cstimer_20230607_140732.txt')
data = json.load(f)

def generateGraphSingleSession(session):
    data_points = getListOfTimes(session) / 1000

    x = np.arange(1, len(data_points)+1).astype(int)

    a, b = np.polyfit(x, data_points, 1)

    plt.plot(x, data_points, 'o')
    plt.plot(x, a*x+b, color='orange', linestyle='--', linewidth=2)

    plt.ylim((0, 25))
    plt.show()

def generateGraphAllSessions(sessions):
    for session in sessions: 
        generateGraphSingleSession(data[session])

exclude_sessions = [1]
sessions = find_all_sessions(data, exclude_sessions)
generateGraphAllSessions(sessions)