import streamlit as st
import numpy as np
import pandas as pd

class Evaluator:
    def __init__(_self,df):
        _self.df=df

    def show_head(_self):
        st.write('First 10 rows of DataFrame are: ')
        st.dataframe(_self.df.head(10))

    def show_dimensions(_self):
        #df.shape->(row,col)->(0,1)
        st.write(f'The dimensions of dataset are row : {_self.df.shape[0]} and columns: {_self.df.shape[1]}')

    def show_columns(_self):
        if _self.df.shape[1]==0:
            st.warning("No Columns!")
        else:
            #covernting list of of strings in to single string usincomma as separator
            st.write(f'The columns are: {", ".join(map(str,_self.df.columns))}')