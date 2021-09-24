from flask import Flask,render_template,request
import joblib
from sklearn.linear_model import LinearRegression

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')


@app.route('/prediction1',methods=['POST','GET'])
def prediction1():
    a=[]
    if request.method=="POST":
        pc=request.form['pc']
        open = request.form['open']
        high = request.form['high']
        low = request.form['low']
        last = request.form['last']
        close = request.form['close']
        date = request.form['date']
        datee = date.replace("-" ,"")
        a.extend([pc,open,high,low,last,close,datee])
        model1 = joblib.load('dtmodel1.pkl')
        y_pred= model1.predict([a])
        return render_template('prediction.html',msg="a",op=y_pred)
    return render_template('prediction.html')




if __name__ == '__main__':
    app.run(debug=True)
