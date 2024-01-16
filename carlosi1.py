import pandas as pd
import plotly.express as px
import numpy as np
import plost
from PIL import Image
import streamlit as st

#display the actual dashboard
# Page setting
st.set_page_config(page_title="Global Treasury",
                   page_icon=":bar_chart:",
                   layout="wide"
)
#image logo load
st.image('Colgate.png')

#display first table
s1= pd.read_excel(
    io="ai.xlsx",
    engine='openpyxl')

st.dataframe(s1)
#Calculation First mathematical analysis

total_cp = int(s1['Amount'].sum())
average_rate = int(s1['Interest Rate'].mean())

left_column, middle_column = st.columns(2)
with left_column:
    st.subheader("Total ECP: {:,.2f} USD".format(total_cp))
with left_column:
    st.subheader("Average Interest Rate: {0}%".format(round(average_rate,2)))

#deploy graphs

sales_by= (
s1.groupby(by=["Business Partner"]).sum()[["Amount"]]
)
fig_plt= px.bar(sales_by,
                x="Amount",
                y=sales_by.index,
                orientation="h",
                title="<b>ECP by Bank</b>",
                color_discrete_sequence=["#0083b8"]*len(sales_by),
                template="plotly_white"
)
st.plotly_chart(fig_plt)


