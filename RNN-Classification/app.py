import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler,OneHotEncoder
from tensorflow.keras.models import load_model
import pickle
import streamlit as st

model=load_model('regressionmodel.h5')

with open('label_encoder_gender.pkl','rb') as file:
    label_encoder_gender=pickle.load(file)
with open('one_hot_encoder_geo.pkl','rb') as file:
    one_hot_enocder_geo=pickle.load(file)
with open('Scaler.pkl','rb') as file:
    scaler=pickle.load(file)

st.title('Estimated Salary Prediction')

# User input
geography=st.selectbox('Geography',one_hot_enocder_geo.categories_[0])
gender=st.selectbox('Gender',label_encoder_gender.classes_)
age=st.slider('Age',18,92)
balance=st.number_input('Balance')
credit_score=st.number_input('Credit Score')
exited=st.selectbox('Exited',[0,1])
tenure=st.slider('Tenure',0,10)
num_of_products=st.slider("Number of products",1,4)
has_cr_card=st.selectbox('Has Credit card',[0,1])
is_active_member=st.selectbox('Is Active member',[0,1])

input_data=pd.DataFrame({
    'CreditScore':[credit_score],
    'Gender':[label_encoder_gender.transform([gender])[0]],
    'Age':[age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'Exited': [exited]
})

geo_encoded=one_hot_enocder_geo.transform([[geography]]).toarray()
geo_encoded_df=pd.DataFrame(geo_encoded,columns=one_hot_enocder_geo.get_feature_names_out(['Geography']))

input_data=pd.concat([input_data.reset_index(drop=True),geo_encoded_df],axis=1)
input_data_scaled=scaler.transform(input_data)

prediction=model.predict(input_data_scaled)
prediction_proba=prediction[0][0]

st.write(f'Estimated Salary is: {prediction_proba:.2f}')


