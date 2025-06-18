import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix


class LogisticRegressor:
    def __init__(_self, df):
        _self.df=df.select_dtypes(include=['number']).dropna()
        _self.columns=_self.df.columns.values


    def classify(_self):
        x=st.multiselect('Select Features (X):',_self.columns,key='logistic_x')
        y=st.selectbox('Select Target (MUST BE BINARY):',_self.columns,key='logistic_y')

        if st.button('Run Logistic Regression'):
            if x and y:
                X=_self.df[x]
                Y=_self.df[y]

            if len(Y.unique())!=2:
                st.error("Selected target must be binary (only 2 classes).")
                return

            #classes binary conversion
            if sorted(Y.unique())!=[0,1]:
                Y=Y.map({Y.unique()[0]: 0,Y.unique()[1]: 1})

            model = LogisticRegression()
            model.fit(X, Y)

            preds=model.predict(X)

            acc=accuracy_score(Y,preds)
            cm=confusion_matrix(Y,preds)

            st.success(f"Accuracy: {round(acc*100,2)}%")
            st.write("Confusion Matrix:")
            st.dataframe(pd.DataFrame(cm))
