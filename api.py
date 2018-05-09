from flask import Flask, render_template, request
import quandl


quandl.ApiConfig.api_key = "zC992yeEkw5VTye5PFJY"

app = Flask(__name__) # Set up 

#This function takes in a pandas dataframe and returns
#Two lists, one of the stock prices and of the dates
def listify(pandas_dataframe):
    datalist = list(pandas_dataframe)
    prices = []
    dates = []
    for i in datalist:
        d = i[0]
        d_formatted = d.isoformat() #this converts dates from datetime.datetime to string - usable on JavaScript
        dates.append(d_formatted)
        prices.append(i[1])
    return dates, prices



# Sets up a route at the / end point liste
@app.route('/')
def render_data():
    
    if request.args['stock'] == 'oil' or request.args['stock'] == None:
        data = quandl.get("EIA/PET_RWTC_D", returns='numpy')
        dates, prices = listify(data)

        # The lines below were used to plot ./static/stockchart.png
        # using the stock price data in a pandas Data Frame format 
        # plot = data.plot()
        # fig = plot.get_figure()
        # fig.savefig("./static/stockchart.png")
        # This is the only endpoint that shows both method of plotting the timeseries
        return render_template('index.html', dates=dates, prices=prices, oil=True)


    elif request.args['stock'] == 'coal':
        data = quandl.get("EIA/AEO_2016_REF_NO_CPP_SUP_PRD_NA_NA_CL_NA_OTWEST_MILLTON_A", returns='numpy')
        dates, prices = listify(data)

        return render_template('index.html', dates=dates, prices=prices)
    
    elif request.args['stock'] == 'gas':
        data = quandl.get("EIA/AEO_2016_REF_NO_CPP_PRCE_NA_COMM_NA_NG_NA_PCF_Y13DLRPMCF_A", returns='numpy')
        dates, prices = listify(data)

        return render_template('index.html', dates=dates, prices=prices)
    

# Notes for improvement: can use data.describe to get basic stats of dataset
# from Quandl API
# Implementing an intuitive customized query interface with start/end date
# or number of rows would only require to add a parameter to quandl.get() 