import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Settings
page_title="Financial Analysis Tool"
layout="centered"
page_icon=":money_with_wings:"

st.set_page_config(page_title=page_title,page_icon=page_icon,layout=layout)
st.title(page_title+" "+page_icon)

df=pd.read_csv("Arcana_score_final.csv")

with st.form("entry_form",clear_on_submit=False):
    
    
    company=st.text_input("",placeholder="Enter the company here")

    submitted=st.form_submit_button("View Insights")

    if submitted:
        df_comp=df.loc[df["company_name"]==company]
        with st.expander("Bar charts"):
            for _,row in df_comp.iterrows():
                x = ['Positive', 'Neutral', 'Negative']
                y = [row["Positive"],row["Neutral"], row["Negative"]]
                fig = go.Figure([go.Bar(x=x, y=y)])
                fig.update_layout(title='Sentiment', xaxis_title=row["year"], yaxis_title='Number of Sales')
                st.plotly_chart(fig,use_container_width=True)



