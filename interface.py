from flask import Flask,request,render_template,jsonify
from utils import StockPrediction
import config

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_stock',methods = ['GET','POST'])
def predict_stock():

    if request.method == "POST":
         
        data = request.form
        print('Data:',data)

        Open = data['Open']
        High =  data['High']
        Low =  data['Low']
        Volume =  data['Volume']
        year =  data['year']
        month = data['month']
        day   = data['day']

        obj = StockPrediction(Open,High,Low,Volume,year,month,day)
        pred_price = obj.get_predicted_price()
        return jsonify({'Result':f'predicted stock price {pred_price} rs only'})
        return render_template ('index.html',result = pred_price.round())
     
    elif request.method == "GET":

        data = request.args.get
        print("Data - ",data)
        Open = data('Open')
        High =  data('High')
        Low =  data('Low')
        Volume =  data('Volume')
        year =  data('year')
        month = data('month')
        day   = data('day')

        obj = StockPrediction(Open,High,Low,Volume,year,month,day)
        pred_price = obj.get_predicted_price()
        return render_template ('index.html',result = pred_price)
     



if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = config.PORT_NUMBER,debug  = True)