import pandas as pd
df = pd.read_csv ('/home/techno_disaster/cloud-program-leaderboard/urls/QwikLabs links - Form Responses 1.csv',  usecols= ['URL'])
df.update('"' + df[['URL']].astype(str) + '",')
print(df.to_string(index=False))

