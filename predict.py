
from flask import Flask
from flask import request
from flask import jsonify

import pickle
model_path='model.bin'
with open(model_path,'rb') as f_in:
    model,dv=pickle.load(f_in)

app=Flask('predict')

@app.route('/predict',methods=['post'])
def predict():
    customer=request.get_json()
    x=dv.transform([customer])
    y_pred=model.predict(x)
    result={
        'prediction_number': float(y_pred)    
    }
    
    return jsonify(result)
    
    

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=9696)