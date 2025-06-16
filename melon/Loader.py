import streamlit as st
import pandas as pd
import numpy as np

class Loader:
    def __init__(_self):
        _self.no_label=False
        _self.separator=','
    
    def check_labels(_self):
        if st.checkbox('File has no header'):
            _self.no_label=True

    def check_separator(_self):
        sep_dict={
            'comma [Default]':',',
            'semicolon' :';',
            'space': ' ',
            'tab': '\t'
             }
        selected_sep =st.selectbox('Select the separator file used in the file',list(sep_dict.keys()))
        # if sep==True:
        _self.separator=sep_dict[selected_sep]

    def load_file(_self):
        return st.file_uploader('Upload csv, tsv or txt file: ',type=['csv','txt','tsv'])
        

    @st.cache_data
    def load_data(_self,uploaded_file):
        # st.write("Original loaded data:")
        # st.dataframe(df.head())
        if _self.no_label:
            df=pd.read_csv(uploaded_file,sep=_self.separator,header=None)

            st.write("Original loaded data:")
            st.dataframe(df.head())
            st.markdown('Loader.py')
            
            df=df.select_dtypes(include=['number']) #,exclude=['']
            df.dropna(inplace=True)
            df.columns=['X'+ str(i+1) for i in range(df.shape[1])]
            return df
        else:
            df=pd.read_csv(uploaded_file,sep=_self.separator,header=0)
            st.markdown('Loader.py')
            st.write("Original loaded data:")
            st.dataframe(df.head(5))

            df.dropna(inplace=True)
            lowercase=lambda x: str(x).lower()
            df.rename(columns=lowercase,inplace=True)#axis=1-> columns,0->row

            df=df.select_dtypes(include=['number'])
            st.markdown('Loader.py')
            st.write("Numeric data:")
            return df

