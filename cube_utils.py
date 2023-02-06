import numpy as np 

scr_to_enc = {
    'U' : 0,
    'U2' : 1, 
    'U\'' : 2, 
    'F' : 3,
    'F2' : 4,
    'F\'' : 5,
    'D' : 6,
    'D2' : 7,
    'D\'' : 8,
    'L' : 9,
    'L2' : 10, 
    'L\'' : 11,
    'R' : 12,
    'R2' : 13, 
    'R\'' : 14, 
    'B' : 15,
    'B2' : 16, 
    'B\'' : 17
}

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

def getSolveTime(solve):
    return solve[0][1]

def getSolveScramble(solve):
    return solve[0][1] # to be implemented

def getScrambleAndTime(session):
    length = len(session)

    scrambles = np.array(list(map(getSolveScramble, session)))
    print(scrambles)
    times = np.array(list(map(getSolveTime, session))) / 1000

def generate_data_all(data, sessions):
    data_points = []

    for session in sessions: 
        session 
        getScrambleAndTime(session)
        break 

    data_points = np.array(data_points)
    return data_points