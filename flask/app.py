from flask import Flask,render_template, request
import pickle
import pandas as pd

model = pickle.load(open(r"D:/ML/_______PROJECT________/online paymetn fraud detection/flask/payment.pkl", "rb"))
app = Flask(__name__)
@app.route('/')

def about():
    return render_template('home.html')

@app.route("/home")
def about1():
    return render_template('home.html')

@app.route("/predict")
def home1():
    return render_template('predict.html')


@app.route("/pred",methods=['POST', 'GET'])
def predict():
    x = [float(request.form.get(col)) for col in ['step', 'type', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest']]
    x = [x]  # Make it 2D for model input
    pred = model.predict(x)[0]
    result = "Fraud" if pred == 1 else "Not Fraud"
    return render_template('submit.html', prediction=result)
if __name__ == "__main__":
    app.run(debug=True)