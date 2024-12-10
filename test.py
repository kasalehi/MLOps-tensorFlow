import requests
url="http://127.0.0.1:9696/predict"
customer={ "gender": "male",
 "seniorcitizen": 0,
 "partner": "no",
 "dependents": "no",
 "tenure": 34,
 "phoneservice": "yes",
 "multiplelines": "no",
 "internetservice": "dsl",
 "onlinesecurity": "yes",
 "onlinebackup": "no",
 "deviceprotection": "yes",
 "techsupport": "no",
 "streamingtv": "no",
 "streamingmovies": "no",
 "contract": "one_year",
 "paperlessbilling": "no",
 "paymentmethod": "mailed_check",
 "monthlycharges": 56.95,
 "totalcharges": 1889.5
         }


result=requests.post(url,json=customer).json()
print(result)
