import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


header = st.beta_container()
dataset = st.beta_container()
eda = st.beta_container()

with header:
    st.title("Supermarket Sales Analysis")
    st.text("This project shows the analysis of the performance of a supermarket using the data provided")

with dataset:
    st.header("Supermarket xlsx")
    st.text("I downloaded the xlsx file from https://www.kaggle.com/aungpyaeap/supermarket-sales")
    df = pd.read_excel("/Users/asumankabugo/Desktop/supermarket_sales - Sheet1.xlsx")

    # date transformation
    df["Date"] = pd.to_datetime(df["Date"])
    # transform to weekday
    df['weekday'] = df['Date'].dt.day_name()
    # transform into month
    df['month'] = df['Date'].dt.month_name()

    # We need to extract the hour from the ‘Date’ variable to do this analysis.
    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S')
    df['hour'] = df['Time'].dt.hour
    st.write('Shape')
    st.write(df.shape)

    # navigation bar
    rad =st.sidebar.radio('Exploratory Data Analysis',['Uni-variate (categorical) Analysis',
                                                       'Uni-variate (numerical) Analysis','Bi-variate Analysis'])

    # columns to select for Independent analysis
if rad == "Uni-variate (categorical) Analysis":
    independent_anly =['Gender','Customer_type','City','Payment','Branch']
    # sidebar for analysis of each independent feature
    x_axis1 = st.sidebar.selectbox('Uni-variate (categorical) Analysis?', independent_anly)
    # figure
    fig = px.bar(df,
                 x=x_axis1,
                 color=x_axis1,
                 title=f'Uni-variate Analysis, {x_axis1}')
    st.plotly_chart(fig)

    # columns for Independent (Numerical) analysis
if rad == "Uni-variate (numerical) Analysis":
    numerical_analy = ['gross_income','Rating']
    # sidebar for each independent numerical feature
    x_axis2 = st.sidebar.selectbox('Uni-variate (numerical) Analysis', numerical_analy)
    # figure
    fig = px.histogram(df,
                 x=x_axis2,
                 color=x_axis2,
                 title=f'Uni-variate(numerical) Analysis, {x_axis2}')
    st.plotly_chart(fig)

    # Columns to select
if rad == "Bi-variate Analysis":
    columns = ['Branch','City','Customer_type','Gender','Product_line','Unit_price','Quantity','Payment',
               'Rating','weekday','month','hour']
    # Allow columns to analyse
    x_axis = st.sidebar.selectbox('Bi-variate Analysis', columns)
    # Bi-variate analysis
    fig = px.bar(df,
                     x=x_axis,
                     y='gross_income',
                     color=x_axis,
                     title=f'Gross_income vs. {x_axis}')

    st.plotly_chart(fig)






