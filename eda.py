import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title = 'predict harga mobil - EDA'
)

def run():
    #membuat judul
    st.title('harga Prediction')

    #membuat subheader
    st.subheader('EDA untuk analisa dataset ') 



    #bikin deskripsi
    st.write('Page ini dibuat oleh Thariq')

    st.write('**TES**')

    st.write('# TES')

    #bikin garis pemisah
    st.markdown('---')

    #Show dataframe
    df = pd.read_csv('data.csv')
    st.dataframe(df)

    # Visualization
    plt.figure(figsize=(16, 5))

    # Weight vs Height Scatter Plot
    plt.subplot(2, 3, 4)
    sns.scatterplot(x='MSRP', y='city mpg',data= df)
    plt.title('MSRP VS city mpg')

    # Show the Plot
    plt.show()


    #Scatterplot 

    sns.scatterplot(df,x='MSRP', y='Year')
    plt.title('MSRP VS Year')



    size = df['Vehicle Size'].value_counts()
    size

    size.plot(kind='bar', rot=0)

    # Box plot untuk melihat adanya outlier
    plt.figure(figsize=(8, 6))
    sns.boxplot(df['Engine HP'])
    plt.title('HP')
    plt.xlabel('Engine HP')
    plt.show()


    #Scatterplot between Size and Rent

    sns.scatterplot(data=df,x='highway MPG', y='Engine HP')
    plt.title('mpg')