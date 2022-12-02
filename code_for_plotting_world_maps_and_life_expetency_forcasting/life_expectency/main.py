import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

import tensorflow as tf

from sktime.forecasting.arima import ARIMA
from sklearn.model_selection import train_test_split

def load_data(root_dir):

    df = pd.read_csv(root_dir + 'life-expectancy.csv')
    df = df.dropna()

    years = []
    values = []
    countries = []

    min_year = 1e9
    max_year = 0

    for country in list(np.unique(df['Country'])):

        countries.append(country)

        df_country = df.loc[(df['Country'] == country)]

        years.append(np.asarray(df_country['Year'], dtype=np.int32))
        values.append(np.asarray(df_country['Life expectancy'], dtype=np.float32))
    
        if years[-1][0] < min_year:
            min_year = years[-1][0]
        
        if years[-1][-1] > max_year:
            max_year = years[-1][-1]
    
    return values, years, min_year, max_year, countries

def build_forcaster():

    model = tf.keras.models.Sequential()

    model.add(tf.keras.layers.Input(shape=(None,1), ragged=True))
    model.add(tf.keras.layers.LSTM(units=3))
    model.add(tf.keras.layers.Dense(units=1))

    # input_layer = tf.keras.layers.Input((None,1), ragged=True)
    # # reshape_layer = tf.keras.layers.Reshape(target_shape=(None,1))(input_layer)

    # lstm = tf.keras.layers.LSTM(units=3)(input_layer)

    # output_layer = tf.keras.layers.Dense(units=1)(lstm)

    # model = tf.keras.models.Model(inputs=input_layer, outputs=output_layer)

    model.compile(optimizer='Adam', loss='MSE')

    return model

def normalize(values):

    means, stds = [], []

    for i in range(len(values)):

        mean = np.mean(values[i])
        std = np.std(values[i])

        values[i] = (values[i] - mean) / (std * 1.0)

        means.append(mean)
        stds.append(std)
    
    return values, means, stds

if __name__ == "__main__":

    root_dir = '/home/afawaz/phd/datasets/Aids/'
    values, years, min_year, max_year, countries = load_data(root_dir=root_dir)
    
    # print(len(values))

    # for i in range(len(values)):

    #     plt.plot(years[i], values[i])
    
    # plt.show()

    model = build_forcaster()

    values, means, stds = normalize(values)
    to_predict = []

    for i in range(len(years)):

        to_predict.append(values[i][-1])
        values[i] = np.expand_dims(values[i][:-1], axis=-1)

    # hist = model.fit(tf.ragged.constant(values), np.asarray(to_predict), batch_size=32, epochs=500)

    # plt.plot(hist.history['loss'])
    # plt.savefig('loss.pdf')
    # plt.cla()
    # plt.clf()

    # model.save('model.hdf5')

    model = tf.keras.models.load_model('model.hdf5')

    # random_countries = np.random.randint(low=0, high=256, size=5)

    random_countries = [72,78]

    plt.figure(figsize=(20,10))
    l_predicted = 20

    for i in random_countries:

        x = values[i]

        for j in range(l_predicted):

            pred = model.predict(np.expand_dims(x, 0))

            x = list(x[:,0])
            x.append(pred[0][0])

            x = np.asarray(x).reshape((-1,1))
        
        np.save(arr=values[i]*stds[i]+means[i], file='TS_'+str(i)+'.npy')
        np.save(arr=x*stds[i]+means[i], file='predicted_'+str(i)+'.npy')
        np.save(arr=years[i][:-1], file='years_'+str(i)+'.npy')
        np.save(arr=countries[i], file='country_'+str(i)+'.npy')
    

        plt.plot(years[i][:-1], values[i]*stds[i] + means[i], label=countries[i]+'-Past Events', lw=3)
        plt.plot(np.arange(l_predicted)+years[i][-1],x[-l_predicted:]*stds[i] + means[i], label=countries[i]+'-Predicted Future', lw=3)

    plt.legend()

    plt.xlabel('Years', fontsize=20)
    plt.ylabel('Life Expectancy', fontsize=20)
    plt.savefig('results.pdf')