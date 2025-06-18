import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import numpy as np

class LinearRregressor:
    def __init__(_self,df):
        _self.df=df.select_dtypes(include=['number']).dropna()
        _self.columns=_self.df.columns.values

    def Linear(_self):
        st.markdown("select more than one feature for accuracy :)")
        x=st.multiselect('X',_self.columns,default=None,key='Linear_Reg_X')
        y=st.selectbox('y',_self.columns,key='Linear_reg_y')

        if st.button('Calculate Linear Regession'):
            if x and y:
                scaler=StandardScaler()
                x_scaled=scaler.fit_transform(_self.df[x])
                reg=LinearRegression()
                reg.fit(x_scaled,_self.df[[y]])
                st.write(f'Training score: {round(reg.score(x_scaled,_self.df[[y]]),3)}')

                coefficient_val=reg.coef_[0].tolist()+[reg.intercept_[0]]
                coefficient_names=x.copy()+['Constant']
                coefficient_df=pd.DataFrame([coefficient_val],columns=coefficient_names,index=['Coefficients'])

                st.table(coefficient_df)
                
                st.session_state['goodscene']=True
                st.session_state['scaler']=scaler
                st.session_state['x_scaled']=x_scaled
                st.session_state['coefficient_df']=coefficient_df
                st.session_state['x_column']=x
                st.session_state['y_column']=y
                st.session_state['coefficient_names']=coefficient_names
                st.session_state['df']=_self.df

        y_pred=0
        if st.session_state.get('goodscene',False):
            if st.button('Generate Random Number'):
                coe_df=st.session_state['coefficient_df']
                x_columns=st.session_state['x_column']
                col_names=st.session_state['coefficient_names']
                scaler=st.session_state['scaler']
                df=st.session_state['df']
                y_column=st.session_state['y_column']

                rand_index=np.random.randint(0,_self.df.shape[0])
                x_raw=df[x_columns].iloc[rand_index].values.reshape(1,-1)
                x_raw_scaled=scaler.transform(x_raw)[0]

                for i,x_col in enumerate(col_names[:-1]):
                    coef=coe_df[x_col].iloc[0]
                    value=x_raw_scaled[i]
                    result=coef*value
                    y_pred+=result
                    st.write(f"{x_col}: {round(coef,3)} * {round(value,3)} = {round(result,3)}")

                y_pred+=coe_df['Constant'].iloc[0]

                st.write(f"Predicted y= {round(y_pred,3)}")
                st.write(f"Actual y= {df[y_column].iloc[rand_index]}")
