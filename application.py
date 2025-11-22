from flask import Flask,request,jsonify,render_template
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

application=Flask(__name__)
app=application

# Impoert ridge and Elastic
ridge_model=pickle.load(open(r'C:\Users\jaivenkateg\Desktop\practice\models\Ridge.pkl','rb'))
standard_scalar=pickle.load(open(r'C:\Users\jaivenkateg\Desktop\practice\models\Scalar.pkl','rb'))
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        Temprature=float(request.form.get('Tempearature'))
        Ws=float(request.form.get('Ws'))
        RH=float(request.form.get('RH'))
        Rain=float(request.form.get('Rain'))
        FFMC=float(request.form.get('FFMC'))
        DMC=float(request.form.get('DMC'))
        ISI=float(request.form.get('ISI'))
        Classes=float(request.form.get('Classes'))
        Region=float(request.form.get('Region'))
        new_data=standard_scalar.transform([[Temprature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result=ridge_model.predict(new_data)
        return render_template('home.html',results=result[0])
    else:
      return render_template('home.html')

if __name__=='__main__':
    app.run(host='0.0.0.0')


# It is ready to diploy but I don't have the aws account