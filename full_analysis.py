import numpy as np
import pandas as pd 
import json 
import matplotlib.pyplot as plt 
import time 

f = open('cstimer_20230607_140732.txt')
data = json.load(f)

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

def getSubOf(session, subOf):
    length = len(session)

    times = np.array(list(map(getSolveTime, session))) / 1000 

    num_solves_sub_of = np.sum(times < subOf)
    percentage_sub_of = round((num_solves_sub_of / length) * 100, 2)
    
    return percentage_sub_of, num_solves_sub_of

def generate_data(data, sessions, subOf):
    data_points = []

    for session in sessions: 
        percentage, num = getSubOf(data[session], subOf)
        data_points.append(percentage)

    data_points = np.array(data_points)
    return data_points
    
# def create_plot(data, sessions, subOf):
#     data_points = generate_data(data, sessions, subOf)
#     x = np.arange(1, len(data_points)+1)

#     a, b = np.polyfit(x, data_points, 1)

#     fig = plt.figure()

#     plt.plot(x, data_points, '-o')
#     plt.plot(x, a*x+b, color='orange', linestyle='--', linewidth=2)
#     plt.title(f'Percentage of Sub-{subOf} Solves Over Time')
#     plt.xlabel('Sessions')
#     plt.ylabel('Percentage')

    

#     # plt.show()

#     # fig = plt.figure()

#     # fig.plot(x, data_points, '-o')
#     # fig.plot(x, a*x+b, color='orange', linestyle='--', linewidth=2)
#     # fig.title(f'Percentage of Sub-{subOf} Solves Over Time')
#     # fig.xlabel('Sessions')
#     # fig.ylabel('Percentage')
#     return fig

# def create_all_plots(data, sessions, sub_ofs):

#     HEIGHT = 2
#     WIDTH = 4

#     fig, axs = plt.subplots(WIDTH, HEIGHT)

#     for i in range(WIDTH):
#         for j in range(HEIGHT):
#             idx = i * HEIGHT + j
#             print(idx)
#             axs[i, j] = create_plot(data, sessions, sub_ofs[idx])

#     # fig.tight_layout()
#     plt.show()
    
def create_plot(data, sessions, subOf, plt):
    data_points = generate_data(data, sessions, subOf)
    x = np.arange(1, len(data_points)+1).astype(int)

    a, b = np.polyfit(x, data_points, 1)

    plt.plot(x, data_points, '-o')
    plt.plot(x, a*x+b, color='orange', linestyle='--', linewidth=2)
    plt.set_title(f'Percentage of Sub-{subOf} Solves Over Time')
    plt.set_xlabel('Sessions')
    plt.set_ylabel('Percentage')

def create_all_plots(data, sessions, sub_ofs):

    HEIGHT = 2
    WIDTH = 4

    fig, axs = plt.subplots(WIDTH, HEIGHT)
    # fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=10, hspace=10)
    fig.set_size_inches(10, 10)
    for i in range(WIDTH):
        for j in range(HEIGHT):
            idx = i * HEIGHT + j
            # print(idx)
            create_plot(data, sessions, sub_ofs[idx], axs[i, j])

    fig.tight_layout()
    # plt.show()
    plt.savefig('figure_1.png')

def generate_data_list(data, sessions):
    data_points = []
    for session in sessions:
        session_data = data[session]
        data_points.extend(list(map(getSolveTime, session_data)))

    return data_points 

def create_list_of_averages(data, sessions, avgOf):
    data_points = generate_data_list(data, sessions)
    num_solves = len(data_points)
    data_points = np.array(data_points) / 1000

    # avgOf = 5
    list_of_averages = []
    for i in range(num_solves - avgOf):
        subset = data_points[i:i+avgOf]
        avg = np.average(subset)
        list_of_averages.append(avg)
    return list_of_averages

def create_averages_plot(data, sessions, avgOf):
    list_of_averages = create_list_of_averages(data, sessions, avgOf)

    np.random.choice

    x = np.arange(1, len(list_of_averages)+1).astype(int)

    ind = np.sort(np.random.choice(x, size=(1000,), replace=False))
    x = ind.astype(int)
    # print(x)
    list_of_averages = np.array(list_of_averages)
    list_of_averages = list_of_averages[x]
    a, b = np.polyfit(x, list_of_averages, 1)

    plt.plot(x, list_of_averages, '-o')
    plt.plot(x, a*x+b, color='orange', linestyle='--', linewidth=2)

    plt.show()

    

exclude_sessions = [1]

sub_ofs = [20, 18, 15, 14, 13, 12, 11, 10]

sessions = find_all_sessions(data, exclude_sessions)
create_all_plots(data, sessions, sub_ofs)

# data_points = generate_data_list(data, sessions)
# print(len(data_points))

# create_averages_plot(data, sessions, 5)

