from tensorflow.keras import Model
from tensorflow.keras.layers import Dense


class SingleLayerModel(Model):
    def __init__(self):
        super(SingleLayerModel, self).__init__()
        self.d1 = Dense(3, activation='relu')
        self.d2 = Dense(1, activation='linear')

    def call(self, inputs, training=None, mask=None):
        x = self.d1(inputs)
        return self.d2(x)

    def get_config(self):
        pass


class MultiLayerModel(Model):
    def __init__(self):
        super(MultiLayerModel, self).__init__()
        self.d1 = Dense(128, activation='relu')
        self.d2 = Dense(64, activation='relu')
        self.d3 = Dense(1, activation='linear')

    def call(self, inputs, training=None, mask=None):
        x = self.d1(inputs)
        x = self.d2(x)
        return self.d3(x)

    def get_config(self):
        pass
