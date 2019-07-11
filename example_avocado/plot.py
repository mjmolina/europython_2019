import pandas as pd
import numpy as np
from pprint import pprint
from datetime import datetime as dt
from bokeh.plotting import figure, output_file, show

def get_dates(raw):
    return [dt(int(d[0]), int(d[1]), int(d[2]))
                for d in (x.split("-") for x in raw)]

def get_average(raw_x, raw_y):
    d = {}
    for x,y in zip(raw_x, raw_y):
        if x not in d:
            d[x] = [y]
        else:
            d[x].append(y)
    avg = {key:np.mean(value) for key,value in d.items()}
    return list(avg.keys()), list(avg.values())

# Total average
raw_data = pd.read_csv("avocado.csv")
raw_df1 = raw_data[raw_data.type == "conventional"]
raw_df2 = raw_data[raw_data.type == "organic"]

df1 = raw_df1.sort_values(by=['Date'], ascending=True)
df2 = raw_df2.sort_values(by=['Date'], ascending=True)

raw_x_df1 = df1["Date"]
x_df1 = get_dates(raw_x_df1)
y_df1 = df1["AveragePrice"]
x_df1_avg, y_df1_avg = get_average(x_df1, y_df1)

raw_x_df2 = df2["Date"]
x_df2 = get_dates(raw_x_df2)
y_df2 = df2["AveragePrice"]
x_df2_avg, y_df2_avg = get_average(x_df2, y_df2)

output_file("avocado.html")
p = figure(title="Avocado prices",
           x_axis_label='Date',
           y_axis_label='Price',
           x_axis_type="datetime",
           plot_width=1200)
p.circle(x_df1, y_df1, legend="Average price (conventional)", color="red", alpha=0.1, line_width=2)
p.circle(x_df2, y_df2, legend="Average price (organic)", color="blue", alpha=0.1,  line_width=2)

p.line(x_df1_avg, y_df1_avg, legend="Average per date (conventional)", color="red", line_width=4)
p.line(x_df2_avg, y_df2_avg, legend="Average per date (organic)", color="blue", line_width=4)
p.legend.click_policy="hide"

show(p)


