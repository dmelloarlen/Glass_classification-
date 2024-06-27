
import pandas as pd
import streamlit as sl

df= pd.read_csv("glass_clean.csv")
print(df)
sl.title("Glass classification ")
# sl.write(df)
print(df.info())
name=df.columns
print(name)
df.drop(df[0].columns)
sl.write(df)
df.sort_values(df.columns[-12],axis=0,ascending=[False],inplace=True)
sl.write("glass with minimum quality:",df.tail(1))
sl.write("glass with maximum quality:",df.head(1))

a=sl.selectbox("choose one",df.columns,index=2)

   
sl.bar_chart(df[a])
  