import numpy as np
import pandas as pd 
import json 
import matplotlib.pyplot as plt 
import time 

def getSolveTime(solve):
    return solve[0][1]

def getListOfTimes(session):
    return np.array(list(map(getSolveTime, session)))

def find_all_sessions(data, exclude_sessions):
    run = True 
    i = 1

    list_of_sessions = []
    while (run):
        if (i not in exclude_sessions):

            session = f'session{i}'
            try:
                data[session]
            except:
                break
            
            list_of_sessions.append(f'session{i}')        
        i += 1
    return list_of_sessions