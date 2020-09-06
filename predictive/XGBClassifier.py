import pandas as pd
import keras
from sklearn import preprocessing
import numpy as np
from sklearn.metrics import confusion_matrix, recall_score, precision_score

class ModelLSTM:
    def __init__(self):
        path_to_models = r"G:\NN\config\Predictive Maintenance\model.joblib"
        self.model = keras.models.load_model("model_lstm.h5")

    def gen_sequence(self, id_df, seq_length, seq_cols):
        """ Only sequences that meet the window-length are considered, no padding is used. This means for testing
        we need to drop those which are below the window-length. An alternative would be to pad sequences so that
        we can use shorter ones """
        data_array = id_df[seq_cols].values
        num_elements = data_array.shape[0]
        for start, stop in zip(range(0, num_elements - seq_length), range(seq_length, num_elements)):
            yield data_array[start:stop, :]

    def gen_labels(self, id_df, seq_length, label):
        data_array = id_df[label].values
        num_elements = data_array.shape[0]
        return data_array[seq_length:num_elements, :]

    def preprocessing(self, path):
        data = pd.read_csv('path', sep=" ", header=None)
        data.drop(data.columns[[26, 27]], axis=1, inplace=True)
        data.columns = ['id', 'cycle', 'setting1', 'setting2', 'setting3', 's1', 's2', 's3',
                            's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14',
                            's15', 's16', 's17', 's18', 's19', 's20', 's21']
        data = data.sort_values(['id', 'cycle'])
        rul = pd.DataFrame(data.groupby('id')['cycle'].max()).reset_index()
        rul.columns = ['id', 'max']
        data = data.merge(rul, on=['id'], how='left')
        data['RUL'] = data['max'] - data['cycle']
        data.drop('max', axis=1, inplace=True)
        w1 = 30
        w0 = 15
        data['label1'] = np.where(data['RUL'] <= w1, 1, 0)
        data['label2'] = data['label1']
        data.loc[data['RUL'] <= w0, 'label2'] = 2
        data['cycle_norm'] = data['cycle']
        cols_normalize = data.columns.difference(['id', 'cycle', 'RUL', 'label1', 'label2'])
        min_max_scaler = preprocessing.MinMaxScaler()
        norm_train_df = pd.DataFrame(min_max_scaler.fit_transform(data[cols_normalize]),
                                     columns=cols_normalize,
                                     index=data.index)
        join_df = data[data.columns.difference(cols_normalize)].join(norm_train_df)
        data = join_df.reindex(columns=data.columns)
        sequence_length = 50
        # pick the feature columns
        sensor_cols = ['s' + str(i) for i in range(1, 22)]
        sequence_cols = ['setting1', 'setting2', 'setting3', 'cycle_norm']
        sequence_cols.extend(sensor_cols)
        seq_gen = (list(self.gen_sequence(data[data['id'] == id], sequence_length, sequence_cols))
                   for id in data['id'].unique())
        seq_array = np.concatenate(list(seq_gen)).astype(np.float32)

        label_gen = [self.gen_labels(data[data['id'] == id], sequence_length, ['label1'])
                     for id in data['id'].unique()]
        label_array = np.concatenate(label_gen).astype(np.float32)


        return seq_array, label_array

    def predict(self, input_data):
        data, label = self.preprocessing(input_data)
        y_pred = self.model.predict_classes(verbose=1, batch_size=200)
        y_true = label
        cm = confusion_matrix(y_true, y_pred)
        precision = precision_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)
        return cm, precision, recall


model = ModelLSTM()
model.predict('PM_test.txt')

