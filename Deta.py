from deta import Deta

deta = Deta('a0t8xg7st9z_58d3VVgRUPwnCFpBxfCcMq6k3yZJGR7J')
import pandas as pd
df = pd.read_csv('Arcana_score_final.csv')  # Replace with the path to your CSV file

# Upload to Deta Space
deta_space = deta.Base('Mybase')  # Replace <YOUR_SPACE_NAME> with the name of your Deta Space
def insert_period(company_name, positive,negative, neutral):
    return deta_space.put({"key":company_name,"positive_score":positive,"negative_score":negative,"neutral_score":neutral})

for index,row in df.iterrows():
    insert_period(row['company_name'], row['Positive'],row['Negative'], row['Neutral'])
    