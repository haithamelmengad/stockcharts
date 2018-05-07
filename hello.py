from flask import Flask, render_template
from flask import request
import quandl


quandl.ApiConfig.api_key = "zC992yeEkw5VTye5PFJY"

app = Flask(__name__)



data = quandl.get("EIA/PET_RWTC_D", returns="numpy")
# data.describe gives count, mean, etc

@app.route('/')
def render_data(data=data):
    print(data)
    return render_template('index.html', data=data)