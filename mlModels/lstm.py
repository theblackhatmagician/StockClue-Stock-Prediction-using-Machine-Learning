import numpy as np
import tensorflow as tf
import sklearn.preprocessing
from datetime import timedelta 

def lstmpredict(series):
    d = []
    graph = []

    for i in series:
        d.append(i['close'])
        graph.append({'time' : i['time'], 'close' : i['close']})

    d = d[150:]
    graph = graph[150:]
    predicttime = 1626061500
    df_close = d
    scaler = sklearn.preprocessing.StandardScaler()
    df_close = scaler.fit_transform(np.array(df_close).reshape(-1,1))

    test_data = df_close
    test_x = []
    test_x.append(test_data[0:100,0])
    test_x = np.array(test_x)
    test_x = test_x.reshape(test_x.shape[0],test_x.shape[1],1)

    model = tf.keras.models.load_model(r'C:\Users\prana\Desktop\stockclue\mlModels\lstm.h5')
    test_predict = model.predict(test_x)
    test_rs = scaler.inverse_transform(test_predict)

    predictgraph = {'time' : predicttime, 'close' : test_rs[0][0]}

    return graph, predictgraph

    return [0, 0]