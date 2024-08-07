import streamlit as st
import numpy as np
import pandas as pd
import sklearn
import joblib

model = joblib.load("xgbmodel.joblib")
st.title('Developers Salary Prediction in 2023')
st.write("### We need some information to predict the salary")

countries = ['Other', 'United Kingdom of Great Britain and Northern Ireland',
       'United States of America', 'Netherlands', 'Germany', 'France',
       'Spain', 'South Africa', 'Italy', 'Canada', 'Switzerland',
       'Brazil', 'Australia', 'Norway', 'Turkey', 'Sweden', 'India',
       'Poland', 'Finland', 'Portugal', 'Austria', 'Belgium', 'Romania',
       'Denmark', 'Russian Federation', 'Israel', 'Ukraine',
       'Czech Republic', 'Mexico', 'New Zealand'
]

Dev_type = [
    'Developer, full-stack',
 'Developer, back-end',
 'Developer, QA or test',
 'Developer, front-end',
 'other',
 'Developer, mobile',
 'Developer, embedded applications or devices',
 'Developer, desktop or enterprise applications',
 'Developer Experience',
 'Developer, game or graphics',
 'Developer Advocate']

Education = [
    "Bachelor's degree",
 'Non-academic degree',
 "Master's degree",
 'Associate degree',
 'Professional degree'
]

Industry = [
    'Other',
 'Information Services, IT, Software Development, or other Technology',
 'Financial Services',
 'Manufacturing, Transportation, or Supply Chain',
 'Retail and Consumer Services',
 'Higher Education',
 'Legal Services',
 'Insurance',
 'Healthcare',
 'Oil & Gas',
 'Wholesale',
 'Advertising Services'
]

# Architecture of the Webpage
country = st.selectbox("Country", countries)
Dev_tp = st.selectbox("Developer type", Dev_type)
Ed_tp = st.selectbox('Education level', Education)
Ind_tp = st.selectbox('Type of industry', Industry)
years_code = st.slider('Years of experience', 0, 50, 2)
ok = st.button('Calculate salary')

columns = ['YearsCodePro', 'DevType', 'Country', 'EdLevel', 'Industry']

# if ok:
#    X_new = np.array([years_code, Dev_tp, country, Ed_tp, Ind_tp])
#    X_new_df = pd.DataFrame([X_new], columns=columns)
#    salary = model.predict(X_new_df)
    
#    st.subheader(f"The estimated salary is ${salary[0]:.2f}")
if ok:
    try:
        # Prepare input as a DataFrame
        X_new = pd.DataFrame({
            'YearsCodePro': [years_code],
            'DevType': [Dev_tp],
            'Country': [country],
            'EdLevel': [Ed_tp],
            'Industry': [Ind_tp]
        })

        # Ensure columns are in correct data types
        X_new['YearsCodePro'] = X_new['YearsCodePro'].astype('float64')

        # Make prediction using the pipeline
        salary = model.predict(X_new)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")

    except Exception as e:
        st.error(f"An error occurred: {e}")
