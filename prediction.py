# Libraries for Data Manipulation
import pandas as pd
# Libraries for saving
import pickle
import json

#load files

with open('list_num_cols.txt', 'r') as file_1:
 num_inf = json.load(file_1)

with open('list_cat_cols.txt', 'r') as file_2:
 cat_inf = json.load(file_2)

with open('model.pkl', 'rb') as file_3:
  model_inf = pickle.load(file_3)


    
my_data = [{
'Year' : 2006,
'Engine HP': 350.0,
'Engine Cylinders': 6.0,
'Number of Doors': 4.0,
'highway MPG': 28,
'city mpg':20,
'Engine Fuel Type': 'regular unleaded',
'Transmission Type': 'MANUAL',
'Driven_Wheels':'rear wheel drive',
'Vehicle Size':'Midsize',
'Vehicle Style':'Hatchback',
'Make': 'BMW',
'Model':'1 Series M',
'Market Category':'Crossover,Luxury,Hatchback',
'Popularity':'400'}]

data_inference = pd.DataFrame(my_data)

# Tampilkan DataFrame
data_inference
    # Transform the new data using the pipeline
predictions = model_inf.predict(data_inference)

# Print the predictions
print("Predict mobil:", predictions)
