df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays':  [[23, 47], [], [24, 43, 87], [13], [67, 32]], 
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', '12. Air France', '"Swiss Air"']})

df
#question(2a)
df_temp= df_Analysis.From_To.str.split('_', expand=True)
df_temp.columns = ['From', 'To']
print("Output")
df_temp
#question(3)
df_temp.From = df_temp.From.str.title()
df_temp.To = df_temp.To.str.title()
print("Output")
df_temp
#question(4)
df_Analysis=df_Analysis.drop("From_To", axis=1).join(df_temp)
print("Output")
df_Analysis
#question(5)
df_delays=pd.DataFrame(df_Analysis["RecentDelays"].values.tolist())
df_delays.columns = ['delay_{}'.format(n) for n in range(1, len(df_delays.columns)+1)]
df_delays
