from calendar import EPOCH
import pickle 
import os 
import sys
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.keras.layers import Dropout,Dense,LSTM
import numpy as np 
from pathlib import Path 
#from sklearn.ensemble import RandomForestRegressor
sys.path.append(os.getcwd())
from common.datasets import read_up_dataset
from common.pre_processing import pre_processing
#from data_processing import post_processing

def lstm(
        train_path: str = Path(__file__).parent.parent.parent / "../data/toy_train_up_model_20_8_3.txt", 
        model_save_path: str = Path(__file__).parent / "save_model/toy_up_model.pickle",
        classification_threshold: list = [0,0.05],
        type:str = "reg",
        n:float = 100
        ):
    
    model = tf.keras.Sequential([
        LSTM(80,activation = 'relu', return_sequences=True),
        Dropout(0.2),
        LSTM(100),
        Dropout(0.2),
        Dense(1)
    ])

    model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
              loss='mean_squared_error',
              metrics = ['mape'])

    cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=model_save_path,
                                                 save_weights_only=True,
                                                 save_best_only=True,
                                                 monitor='val_loss')


    train_data_set_x, train_data_set_y = read_up_dataset(train_path, classification_threshold, type) 

    train_data_set_x = train_data_set_x[0:1000]
    train_data_set_y = train_data_set_y[0:1000]

    print(train_data_set_y)
    length = len(train_data_set_x)

    train_data_set_x = pre_processing(train_data_set_x)
    train_data_set_x = np.reshape(train_data_set_x,(train_data_set_x.shape[0],20,7))

    #print(train_data_set_x_1)
    history = model.fit(train_data_set_x, train_data_set_y, batch_size=32, epochs = 50,steps_per_epoch = 25,
                        validation_split=0.2,validation_steps=7, callbacks=[cp_callback])

    model.summary()

    #model_save_path = Path(__file__).parent / "save_model/toy_up_model.h5"
    #model.save(model_save_path)
    

