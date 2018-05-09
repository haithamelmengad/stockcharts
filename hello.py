from flask import Flask, render_template
from flask import request
import quandl


quandl.ApiConfig.api_key = "zC992yeEkw5VTye5PFJY"

app = Flask(__name__)



data = quandl.get("EIA/PET_RWTC_D")
# data.describe gives count, mean, etc

@app.route('/')
def render_data(data=data):
    plot = data.plot()
    fig = plot.get_figure()
    fig.savefig(fname="./static","stockchart.png")
    return render_template('index.html', data=data)