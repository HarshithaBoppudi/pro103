import pandas as pd
import plotly_express as px
df=pd.read_csv('corona_data.csv')
figure=px.scatter(df,x='date',y='cases',color='country',title='covid data')
figure.show()
