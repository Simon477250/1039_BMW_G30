import streamlit as st
import pandas as pd
import plotly.express as px
import openpyxl

header = st.container()
dataset = st.container()

with header:
    st.title('Analysetool 1039 BMW G30')
    uploaded_file = st.file_uploader('Import Data')
    if uploaded_file is not None:
        input_measured_data = pd.read_csv(uploaded_file, delimiter=';' , encoding_errors='ignore')#,skiprows=1)
        st.write(input_measured_data)
        #print(input_measured_data.columns)
        print(input_measured_data['TIME'].unique())
        options = st.multiselect('Choose values', input_measured_data.columns[1:])
        st.write('Your choise:', options)

        fig_datas_df = px.line(input_measured_data,x='TIME',y=options)
        st.write(fig_datas_df)


