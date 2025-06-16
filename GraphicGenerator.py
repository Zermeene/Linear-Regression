import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class GrapghicGenerator:
    def __init__(_self,df):
        _self.df=df
        _self.columns=df.columns.values

    def scatterplot(_self):
        st.markdown('### Scatter Plot')
        scatter_col_x=st.multiselect('Columns for the X axis:',_self.columns,default=None,key='x_dispersao')
        scatter_col_y=st.multiselect('Columns for the y axis:',_self.columns,default=None,key='y_dispersao')
        
        if scatter_col_x and scatter_col_y:
            for x_axis in scatter_col_x:
                for y_axis in scatter_col_y:
                    fig=plt.figure(figsize=(14,10))
                    ax=sns.scatterplot(x=_self.df[x_axis],y=_self.df[y_axis])
                    ax.set_title(f'{x_axis.capitalize()} X {y_axis.capitalize()}')
                    ax.set_xlabel(x_axis.capitalize())
                    ax.set_ylabel(y_axis.capitalize())
                    st.pyplot(fig)


    def correlationploy(_self):
        st.markdown('### Correlation Plot')
        corrMatrix=_self.df.corr(numeric_only=True)
        fig=plt.figure(figsize=(14,10))
        ax=sns.heatmap(corrMatrix,annot=True)
        ax.set_title('Heat map of correlations of variables')
        st.pyplot(fig)


    def pairplot(_self):
        st.markdown('### Pair Plot')
        col_pairplot= st.multiselect('Columns: ',_self.columns, default=None,key='xy_pairplot')
            
        if col_pairplot:
            pairplot=sns.pairplot(_self.df[col_pairplot])
            st.pyplot(pairplot)
                
        
    def linearreg(_self):
        st.markdown('### Linear regression')
        col_reg_x=st.multiselect('Columns for x_axix',_self.columns,default=None,key='x_reg')
        col_reg_y=st.multiselect('Columns for y_axix',_self.columns,default=None,key='y_reg')

        if col_reg_x and col_reg_y:
            for x_axis in col_reg_x:
                for y_axis in col_reg_y:
                    fig=plt.figure(figsize=(14,10))
                    ax=sns.regplot(x=_self.df[x_axis],y=_self.df[y_axis],ci=0,line_kws={'color': 'red'})
                    ax.set_title(f'{x_axis.capitalize()} X {y_axis.capitalize()}')
                    ax.set_xlabel(x_axis.capitalize())
                    ax.set_ylabel(y_axis.capitalize())
                    st.pyplot(fig)