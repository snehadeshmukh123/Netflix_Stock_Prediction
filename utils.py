import pickle
import numpy as np

class StockPrediction():
    def __init__(self,Open,High,Low,Volume,year,month,day):
        self.Open = Open
        self.High = High
        self.Low = Low
        self.Volume = Volume
        self.year = year
        self.month = month
        self.day   = day

    def load_saved_data(self):

        with open ('linear_regression.pkl','rb')as f:
            self.model = pickle.load(f)

    def get_predicted_price(self):
        self.load_saved_data()


        test_array = np.zeros([1,self.model.n_features_in_])
        test_array[0,0] = self.Open
        test_array[0,1] = self.High
        test_array[0,2] = self.Low
        test_array[0,3] = self.Volume
        test_array[0,4] = self.year
        test_array[0,5] = self. month
        test_array[0,6] = self.day

        predicted_close = np.around(self.model.predict(test_array)[0],3)
        return predicted_close


        

