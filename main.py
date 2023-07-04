import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Analysing Climate Change in India')

DATA_URL_RAINFALL = ('rainfall in india 1901-2015.csv')
DATA_URL_TEMPERATURE = ("Mean Temperature Data.csv")


@st.cache_data
def load_data(DATA_URL, nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

def rainfall_graph(data_rainfall, region, option):
    df = (data_rainfall[(data_rainfall['SUBDIVISION'] == region)])
    st.line_chart(data=df, y=option)
    st.text(df)

region = st.text_input("Enter the region")
option = st.selectbox("Enter time period you would like to visualise", 
                      ('ANNUAL', 'Jan-Feb', 'Mar-May', 'Jun-Sep', 'Oct-Dec'))


if(len(region) > 0):

    data_load_state = st.text('Loading Rainfall data...')

    data_rainfall = load_data(DATA_URL_RAINFALL, 10000)

    data_load_state = st.text('Loading Temperature data...')

    data_temp = load_data(DATA_URL_TEMPERATURE, 10000)

    st.subheader('Visualisations for Region', region)
    st.text('RainFall over the Years')
    rainfall_graph(data_rainfall, region, option)
    



