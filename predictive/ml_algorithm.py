import keras
import joblib
import os
import pandas as pd
import numpy as np
from os.path import normpath, join

class ModelLSTM:

    def __init__(self,):

        path_to_models = normpath(join(os.getcwd(), 'predictive/ml_model/model_lstm.h5'))
        path_to_min_max_scaler = normpath(join(os.getcwd(), 'predictive/ml_model/min_max_scaler.pkl'))
        self.model = keras.models.load_model(path_to_models)
        self.min_max_scaler  = joblib.load(path_to_min_max_scaler)

    def preprocessing(self, data):
        #read data
        data = pd.DataFrame(data)
        data = data.iloc[0:100 , :]
        data.drop(data.columns[[26, 27]], axis=1, inplace=True)
        data.columns = ['id', 'cycle', 'setting1', 'setting2', 'setting3', 's1', 's2', 's3',
                            's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14',
                            's15', 's16', 's17', 's18', 's19', 's20', 's21']

        # normalize the data
        data['cycle_norm'] = data['cycle']
        cols_normalize = data.columns.difference(['id', 'cycle'])
        norm_data_df = pd.DataFrame(self.min_max_scaler.transform(data[cols_normalize]),
                                    columns=cols_normalize,
                                    index=data.index)
        data_join_df = data[data.columns.difference(cols_normalize)].join(norm_data_df)
        data = data_join_df.reindex(columns=data.columns)
        data = data.reset_index(drop=True)

        # pick a large window size of 50 cycles
        sequence_length = 50

        # pick the feature columns
        sensor_cols = ['s' + str(i) for i in range(1, 22)]
        sequence_cols = ['setting1', 'setting2', 'setting3', 'cycle_norm']
        sequence_cols.extend(sensor_cols)

        # generator for the sequences
        seq_array = [data[data['id'] == id][sequence_cols].values[-sequence_length:]
                               for id in data['id'].unique() if len(data[data['id'] == id]) >= sequence_length]
        # generate sequences and convert to numpy array

        seq_array_data = np.asarray(seq_array).astype(np.float32)
        return seq_array_data

    def predict(self, data):
        prediction = self.model.predict_classes(data, verbose=1, batch_size=200)
        return prediction

    def compute_prediction(self, input_data):
        try:
            input_data = self.preprocessing(input_data)
            prediction = self.predict(input_data)

        except Exception as e:
            return {"status": "Error", "message": str(e)}

        return prediction