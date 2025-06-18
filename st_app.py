import streamlit as st
from melon.Loader import Loader
from melon.Evaluator import Evaluator
from melon.GraphicGenerator import GrapghicGenerator
from melon.LinearRegressor import LinearRregressor
from melon.LogisticRegression import LogisticRegressor

#streamlit run st_app.py

st.header('Linear Regressor')

#Loader.py
data_loader=Loader()
data_loader.check_labels()
data_loader.check_separator()
Uploaded_file=data_loader.load_file()

if Uploaded_file is not None:
    df=data_loader.load_data(Uploaded_file)
    st.write("Original loaded data:")
    st.dataframe(df.head(4))
    st.markdown('<hr/>',unsafe_allow_html=True)

    #Evaluator.py
    st.header('Data Evaluation')
    st.write('Non-numeric columns and rows with missing values have been dropped.')
    data_evaluator = Evaluator(df)
    data_evaluator.show_head()
    data_evaluator.show_dimensions()
    data_evaluator.show_columns()

    #GraphicGenerator.py
    st.header('Graphic Plots')
    Plot=GrapghicGenerator(df)

    check_pairplot=st.checkbox('Pairplot')
    check_scatterplot=st.checkbox('Scatterplot')
    check_correlation=st.checkbox('Correlation')
    check_linearplot=st.checkbox('Linearplot')

    if check_pairplot:
        Plot.pairplot()
        st.markdown('<hr/>',unsafe_allow_html=True)
    if check_scatterplot:
        Plot.scatterplot()
        st.markdown('<hr/>',unsafe_allow_html=True)
    if check_correlation:
        Plot.correlationploy()
        st.markdown('<hr/>',unsafe_allow_html=True)
    if check_linearplot:
        Plot.linearreg()
        st.markdown('<hr/>',unsafe_allow_html=True)

    st.header('Linear Regression')
    data_linear_reg=LinearRregressor(df)
    data_linear_reg.Linear()
    st.markdown('<hr/>',unsafe_allow_html=True)

    #LogisticRgressor.py
    st.header('Logistic Regression')
    logistic = LogisticRegressor(df)
    logistic.classify()
