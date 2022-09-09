from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to PB Demand Prediction!

Input the variables, click a button, and get the outputs. 
"""


st.title('Offer Demand Predictor')
st.header('Enter the characteristics of the offer:')

start_date = st.date_input('Offer start date')
end_date = st.date_input('Offer end date')
share_price = st.number_input('Offer price in pence')
discount = st.number_input('Discount as a decimal', min_value=0.01, max_value=0.99, value=0.05)


if st.button('Predict Demand'):
    price = predict(carat, cut, color, clarity, depth, table, x, y, z)
    st.success(f'The predicted demand is ${price[0]:.2f} USD')
