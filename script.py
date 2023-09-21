import pandas as pd
import numpy as np

df = pd.read_csv('bank_marketing.csv')
client = df[["client_id", "age", "job", "marital", "education", 
             "credit_default", "housing", "loan"]]
campaign = df[["client_id", "campaign", "month", "day", 
               "duration", "pdays", "previous", "poutcome", "y"]]
economics = df[["client_id", "emp_var_rate", "cons_price_idx", 
                "euribor3m", "nr_employed"]]

client.rename(columns = {'client_id':id}, inplace =True)
