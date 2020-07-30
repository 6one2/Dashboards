# from worldbankapp import app
from flask import Flask, render_template, url_for
import json, plotly
from datawrangling.getchart import return_figures

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/worldbank')
def worldbank():
    figs = return_figures()
    
    #plot_ids for the htlm id tag
    ids = [f"figure-{x}" for x in range(len(figs))]
    
    #Convert the plotly figures to JSON for javascript in html template
    figuresJSON = json.dumps(
        figs,
        cls=plotly.utils.PlotlyJSONEncoder
    )
    
    return render_template('worldbank.html', ids=ids, figuresJSON=figuresJSON)


app.run(port=5000, debug=True)
