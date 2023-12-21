from flask import Flask, render_template
import plotly
import plotly.express as px
import pandas as pd
import json

app = Flask(__name__)

index = -1
main_data = pd.read_csv('final.csv', sep=';').to_dict('records')

@app.route('/latest_data', methods=['GET'])
def latest_data():
    data = get_latest_row()
    # print(data, "test")
    return data

@app.route('/latest_plot_data', methods=['GET'])
def latest_plot_data():
    plot_data = get_latest_plot_data()
    # print(data, "test")
    return plot_data

def get_latest_plot_data():
    latest_sent_data = get_latest_row()
    # print(latest_sent_data)
    latest_time = latest_sent_data["Log Time"]
    latest_time_split = latest_sent_data["Log Time"].split(":")
    latest_time_split_three_hour_ago = latest_time_split
    latest_time_split_three_hour_ago[3] = str(int(latest_time_split_three_hour_ago[3])-1)
    one_hour_ago_time = ':'.join(latest_time_split_three_hour_ago)
    res = list(filter(lambda x: one_hour_ago_time <= x.get("Log Time") <= latest_time , main_data ))
    res = [{k: ":".join(v.split(":")[3:5]) if k == "Log Time" else v for k, v in d.items()} for d in res]
    return res

def get_latest_row():
    global index
    index+=1
    return main_data[index]

@app.route('/')
def index_page():
    global index
    data = get_latest_row()
    return render_template('index.html', data = data) 

if __name__ == '__main__':
    # with app.app_context():
	app.run(debug=True)
