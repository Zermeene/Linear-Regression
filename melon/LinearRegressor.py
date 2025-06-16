import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

class LinearRregressor:
    def __init__(_self,df): 
        _self.df=df.select_dtypes(include=['number']).dropna()
        _self.columns=_self.df.columns.values
        

    def Linear(_self):
        x=st.multiselect('X' ,_self.columns,default=None,key='Linear_Reg_X')
        y=st.selectbox('y',_self.columns,key='Linear_reg_y')

        if st.button('Calculate Linear Regession'):
            if x and y:
                reg=LinearRegression()
                reg.fit(_self.df[x],_self.df[[y]])
                st.write(f'Training score: {round(reg.score(_self.df[x],_self.df[[y]]),3)}')

                coefficient_val=reg.coef_[0].tolist()+[reg.intercept_[0]]
                coefficient_names=x.copy()+['Constant']
                coefficient_df=pd.DataFrame([coefficient_val],columns=coefficient_names,index=['Coefficients'])

                st.table(coefficient_df)

