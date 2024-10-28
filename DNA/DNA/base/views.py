from django.shortcuts import render
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
global scaler
def home(request):
    return render(request, 'index.html')

def getPredictions(x):
    x=int(x[5:])
    model = pickle.load(open('naive_bayes.pkl', 'rb'))
    prediction = model.predict(np.array([[x]]))
    return (prediction)

def result(request):
    x = str(request.GET['DOID'])
    result = getPredictions(x)
    return render(request, 'result.html', {'result': result[0]})
    #return render(request, 'result.html', {'result': result})

