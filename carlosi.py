import pandas as pd
import plotly.express as px
import numpy as np
import plost
from PIL import Image
import streamlit as st
from bs4 import BeautifulSoup
import requests

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
    io="usecp.xlsx",
    engine='openpyxl')

#NIH NIP Loans
s2= pd.read_excel(
    io="ilu.xlsx",
    engine='openpyxl')

st.dataframe(s1)
#Calculation First mathematical analysis

#define the ESTR Rates
url = 'https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/euro_short-term_rate/html/index.en.html'
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')
a=soup.td.text

total_cp = int(s1['Amount'].sum())
average_rate = int(s1['Interest Rate'].mean())

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total ECP: {:,.2f} USD".format(total_cp))
with middle_column:
    st.subheader("Average Interest Rate: {0}%".format(round(average_rate,2)))
with right_column:
    st.subheader("ESTR: {0}%".format(a))
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

#define the NIH LOANS

s25=s2.drop(s2[s2['Transaction Type'] == 'NIH'].index)

loans_by= (
s25.groupby(by=["Business Partner"]).sum()[["Amount"]]
)

fig_plt2= px.bar(loans_by,
                x="Amount",
                y=loans_by.index,
                orientation="h",
                title="<b>NIP by Subsidiary</b>",
                color_discrete_sequence=["#0083b8"]*len(loans_by),
                template="plotly_white"
)

st.plotly_chart(fig_plt2)

s30= s2.drop(s2[s2['Transaction Type'] == 'NIP'].index)

loans_bynih= (
s30.groupby(by=["Business Partner"]).sum()[["Amount"]]
)
fig_plt3= px.bar(loans_bynih,
                x="Amount",
                y=loans_bynih.index,
                orientation="h",
                title="<b>NIH by Subsidiary</b>",
                color_discrete_sequence=["#0083b8"]*len(loans_bynih),
                template="plotly_white"
)

st.plotly_chart(fig_plt3)
