import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

mac = pd.read_csv("mac_address.csv")
def IotDeviceName(index,mac):
    iot_names = mac["IoT_Devices"].values
    for j,i in enumerate(iot_names):
        if(j==index):
            return i
    return
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    
    # int_features = [int(x) for x in request.form.values()]
    int_features = []
    for j,i in enumerate(request.form.values()):
        if(j==0):
            s = str(i)
            string = ''.join(str(ord(c)) for c in s)
            sum = 0
            for k in string:
                sum+=int(k)
            int_features.append(sum)
        else:
            int_features.append(i)
    # if(type(int_features[0]) != int):
    #     s = int_features[0]
	# string = ''.join(str(ord(c)) for c in s)
    # sum = 0
    # for j in string:
    #     sum+=int(j)
    # int_features[0] = sum
    
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction[0]

    return render_template('index.html', prediction_text = 'IoT Device is : {}'.format(IotDeviceName(output,mac)))


if __name__ == "__main__":
    app.run(debug=True)
