import pandas as pd
from warnings import filterwarnings
filterwarnings(action='ignore')
from pycaret.regression import *

data = pd.read_csv('insurance.csv')

print(data.head())

r2 = setup(data=data, target='charges', session_id=123, normalize=True,
           polynomial_features=True, trigonometry_features=True, 
           feature_interaction=True, bin_numeric_features=['age','bmi'])


lr = create_model('lr')
save_model(lr, model_name='deployment_04042022')
print("Process completed !!!")