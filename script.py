import pandas as pd
import numpy as np

df = pd.read_csv('bank_marketing.csv')
client = df[["client_id", "age", "job", "marital", "education", 
             "credit_default", "housing", "loan"]]
campaign = df[["client_id","campaign", "month", "day", 
               "duration", "pdays", "previous", "poutcome", "y"]]
economics = df[["client_id","emp_var_rate", "cons_price_idx", 
                "euribor3m", "nr_employed"]]
client.rename(columns = {'client_id':id}, inplace =True)
campaign.rename(columns = {'duration':'contact_duration','previous':'previous_campaign_contacts','y':'campaign_outcome','poutcome':'previous_outcome','campaign':'number_contacts'}, inplace = True)
economics.rename(columns ={'euribor3m':'euribor_three_months','nr_employed':'number_employed'},inplace = True)
client['education'] = client['education'].str.replace('.','_')
client['education'] = client['education'].replace('unknown',np.NAN)
df['job'] = df['job'].str.replace('.','')
campaign['previous_outcome'] = campaign['previous_outcome'].map({'sucess': 1,'failure': 0})
campaign['previous_outcome'] = campaign['previous_outcome'].replace('nonexistance',np.NAN)
campaign['campaign_outcome'] = campaign['campaign_outcome'].map({'sucess': 1,'failure': 0})
values = 1
campaign['campaign_id'] = values
campaign['year'] = '2022'
# Capitalize month column
campaign["month"] = campaign["month"].str.capitalize()
# Convert day to string
campaign["day"] = campaign["day"].astype(str)
# Add last_contact_date column
campaign['last_contact_date'] = pd.read_csv(campaign['day']) + '-' + campaign['month'] + '-' + campaign['month']
# Convert to datetime
campaign['last_contact_date'] = pd.to_datetime(campaign['last_contact_date'], format ='%d-%b-%Y')
client.drop(columns = ['month','day','year'], inplace= True)
client.csv('client.csv',index =False)
campaign.csv('campaign.csv',index =False)
economics.csv('economics.csv',index =False)
client_table =""" CREATE TABLE client
(id,
age,
job,
marital,
education,
credit_default,
housing,
loan)
\copy client from 'client.csv' DELIMITER ',' CSV HEADER
"""
campaign_table =""" CREATE TABLE campaign
(client_id,
campaign,
month,
day,
previous_campaign_contacts,
previous_outcome,
campaign_outcome,
number_contacts
)
\copy campaign from 'campaign.csv' DELIMITER ',' CSV HEADER
"""
economics_table =""" CREATE TABLE economics
(client_id,
emp_var_rate,
cons_price_idx,
euribor_three_months,
number_employed
)
\copy economics from 'economics.csv' DELIMITER ',' CSV HEADER
"""