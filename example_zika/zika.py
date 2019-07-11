import sys
import random
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from pprint import pprint
from matplotlib.pyplot import pause
from time import sleep


def print_legend(plt):
    fs = 15
    pd = 2
    plt.text(17, 15, '  ', bbox={'facecolor':'gray', 'pad':pd}, fontsize=fs)
    plt.text(18, 15, '< 5', fontsize=fs)

    plt.text(17, 14, '  ', bbox={'facecolor':'green', 'pad':pd}, fontsize=fs)
    plt.text(18, 14, '< 20', fontsize=fs)

    plt.text(17, 13, '  ', bbox={'facecolor':'blue', 'pad':pd}, fontsize=fs)
    plt.text(18, 13, '< 50', fontsize=fs)

    plt.text(17, 12, '  ', bbox={'facecolor':'brown', 'pad':pd}, fontsize=fs)
    plt.text(18, 12, '< 100', fontsize=fs)

    plt.text(17, 11, '  ', bbox={'facecolor':'yellow', 'pad':pd}, fontsize=fs)
    plt.text(18, 11, '< 200', fontsize=fs)

    plt.text(17, 10, '  ', bbox={'facecolor':'red', 'pad':pd}, fontsize=fs)
    plt.text(18, 10, '>= 200', fontsize=fs)


def get_color(cases):
    if cases < 5:
        return "gray"
    elif cases < 20:
        return "green"
    elif cases < 50:
        return "blue"
    elif cases < 100:
        return "brown"
    elif cases < 200:
        return "yellow"
    else:
        return "red"

random.seed(19051988)
#random.seed(30101986)
raw_data = pd.read_csv("zika_brazil_nonzero.csv")
data = {}

# Main dictionary
for idx, row in raw_data.iterrows():
    date = row["report_date"]
    location = row["location"].replace("Brazil-", "")
    try:
        cases = int(row["value"])
    except:
        continue

    if date not in data:
        data[date] = {}

    if location not in data[date]:
        data[date][location] = cases
    else:
        data[date][location] += cases

# Plot
plt.rcParams['text.usetex'] = False
fig = plt.figure()
fig.set_size_inches(18, 10)

graph = nx.Graph()
nodedict = {}
for date, values in data.items():
    # Clear plot
    plt.cla()
    plt.title("Zika Expansion (Brazil) - {}".format(date), fontsize=40)
    print_legend(plt)
    plt.tight_layout()
    graph.clear()

    # Add nodes again
    graph.add_node("Brazil", Position=(25,25))
    for city, cases in values.items():
        if city not in nodedict:
            print("Creating node '{}' with {} cases".format(city, cases))
            pos_x = random.randrange(8, 45)
            pos_y = random.randrange(8, 45)
            nodedict[city] = {"cases": int(cases),
                              "posx": pos_x,
                              "posy": pos_y,
                              "color": get_color(int(cases))}
        else:
            print("Updating node '{}' with {} cases".format(city, cases))
            pos_x = nodedict[city]["posx"]
            pos_y = nodedict[city]["posy"]
            nodedict[city]["cases"] = int(cases)
            nodedict[city]["color"] = get_color(int(cases))

        graph.add_node(city, Position=(pos_x, pos_y))
        graph.add_edge(city, "Brazil")

    # Taking case nodes of nodes that did not have an upgrade
    for city, value in nodedict.items():
        if city not in graph.nodes():
            pos_x = value["posx"]
            pos_y = value["posy"]
            graph.add_node(city, Position=(pos_x, pos_y))
            graph.add_edge(city, "Brazil")

    # Drawing the network for each step
    nx.draw(graph,
            pos=nx.get_node_attributes(graph, 'Position'),
            nodelist=nodedict.keys(),
            node_size=np.array([v["cases"]*50 for v in nodedict.values()]),
            labels={key:"\n\n\n{}".format(key.replace("_", " ")) for key,_ in nodedict.items()},
            node_color=[i["color"] for i in nodedict.values()])
    pause(0.8)
    plt.draw()
