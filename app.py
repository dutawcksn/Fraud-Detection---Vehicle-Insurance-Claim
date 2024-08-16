import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import plotly.express as px
import pickle

st.set_page_config(page_title="Fraud Detection", layout="wide")
# Create menu
selected = option_menu(
    menu_title=None,
    options=["Home", "Prediction"],
    icons=["house", "calculator"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

row0_spacer1, row0_1, row0_spacer2 = st.columns((0.1, 3.2, 0.1))
row1_spacer1, row1_1, row1_spacer2, row1_2 = st.columns((0.1, 1.5, 0.1, 1.5))
row0_spacer3, row3_0, row0_spacer4 = st.columns((0.1, 3.2, 0.1))

df = pd.read_csv('clean_data.csv')

Age = []
for i in df['Age']:
    if i >= 17 and i <= 19:
        Age.append('Teen')
    elif i >= 20 and i <= 45:
        Age.append('Middle Age')
    elif i >= 46 and i <= 60 :
        Age.append('Old')
    else:
        Age.append('Elder')
df['Age'] = Age

Sex = []
for i in df['Sex']:
    if i == 0:
        Sex.append('Male')
    else:
        Sex.append('Female')
df['Sex'] = Sex

PolicyType = [] 
for i in df['PolicyType']:
   if i == 0:
      PolicyType.append('Sedan - Collision')
   elif i == 1:
      PolicyType.append('Sedan - Liability')
   elif i == 2:
      PolicyType.append('Sedan - All Perils')
   elif i == 3:
      PolicyType.append('Sport - Collision')
   elif i == 4:
      PolicyType.append('Utility - All Perils')
   elif i == 5:
      PolicyType.append('Utility - Collision')
   elif i == 6:
      PolicyType.append('Sport - All Perils')
   elif i == 7:
      PolicyType.append('Utility - Liability')
   else:
      PolicyType.append('Sport - Liability') 
df['PolicyType'] = PolicyType

AccidentArea = []
for i in df['AccidentArea']:
   if 1 == 0:
      AccidentArea.append('Urban') 
   else:
      AccidentArea.append('Rural')
df['AccidentArea'] = AccidentArea

BasePolicy = []
for i in df['BasePolicy']:
   if i == 0:
      BasePolicy.append('Collision')
   elif i == 1:
      BasePolicy.append('Liability')
   else: 
      BasePolicy.append('All Perils')
df['BasePolicy'] = BasePolicy

Fault = []
for i in df['Fault']:
   if i == 0:
      Fault.append('PolicyHolder')
   else: 
      Fault.append('Third Party')
df['Fault'] = Fault

VehicleCategory = []
for i in df['VehicleCategory']:
   if i == 0:
      VehicleCategory.append('Sedan')
   elif i == 1:
      VehicleCategory.append('Sport')
   else: 
      VehicleCategory.append('Utility')
df['VehicleCategory'] = VehicleCategory

VehiclePrice = []
for i in df['VehiclePrice']:
   if i == 0:
      VehiclePrice.append('20000 - 29000')
   elif i == 1:
      VehiclePrice.append('30000 - 39000')
   elif i == 2:
      VehiclePrice.append('More than 69000')
   elif i == 3:
      VehiclePrice.append('Less than 20000')
   elif i == 4:
      VehiclePrice.append('40000 - 59000')
   else: 
      VehiclePrice.append('60000 - 69000')
df['VehiclePrice'] = VehiclePrice

AgeOfPolicyHolder = []
for i in df['AgeOfPolicyHolder']:
   if i == 0:
      AgeOfPolicyHolder.append('31 to 35')
   elif i == 1:
      AgeOfPolicyHolder.append('36  to 40')
   elif i == 2:
      AgeOfPolicyHolder.append('41 to 50')
   elif i == 3:
      AgeOfPolicyHolder.append('51 to 65')
   elif i == 4:
      AgeOfPolicyHolder.append('26 to 30')
   elif i == 5:
      AgeOfPolicyHolder.append('over 65')
   elif i == 6:
      AgeOfPolicyHolder.append('16 to 17')
   elif i == 6:
      AgeOfPolicyHolder.append('21 to 25')
   else: 
      AgeOfPolicyHolder.append('18 to 20')
df['AgeOfPolicyHolder'] = AgeOfPolicyHolder

AddressChange_Claim = []
for i in df['AddressChange_Claim']:
   if i == 0:
      AddressChange_Claim.append('No Change')
   elif i == 1:
      AddressChange_Claim.append('4 to 8 years')
   elif i == 2:
      AddressChange_Claim.append('2 to 3 years')
   elif i == 3:
      AddressChange_Claim.append('1 year')
   else: 
      AddressChange_Claim.append('under 6 months')
df['AddressChange_Claim'] = AddressChange_Claim

model = pickle.load(open("Model/xgb_model.pkl", "rb"))

if selected == "Home":
    row0_1.title("Vehicle Insurance Claim - Fraud Detector App")
    with row0_1:
        st.markdown(
            "-"
        )
        st.markdown('Dataset : ')
        st.write(df.head())
        st.markdown('Atribut Dataset :')
        st.markdown("1. AccidentArea: Area terjadinya kecelakaan.")
        st.markdown("2. Sex: Jenis Kelamin.")
        st.markdown("3. Age: Umur nasabah.")
        st.markdown("4. Fault: Jenis Kesalahan.")
        st.markdown("5. PolicyType: Tipe Kebijakan.")
        st.markdown("6. VehicleCategory: Kategori Kendaraan.")
        st.markdown("7. VehiclePrice: Kategori harga kendaraan.")
        st.markdown("8. AgeOfPolicyHolder: Umur pengguna kebijakan.")
        st.markdown("9. AddressChange_Claim: Rentang waktu pengubahan alamat ketika klaim asuransi.")
        st.markdown("10. Base Policy: Dasar Kebijakan.")

elif selected == "Prediction":
    with row0_1:
        st.subheader('Input Data')
    with row1_1:
        AccidentArea = st.number_input('Area', min_value=0, max_value=20, value=0)
        Sex = st.number_input('Sex', min_value=0, max_value=200, value=0)
        Age = st.number_input('Age', min_value=0, max_value=200, value=0)
        Fault = st.number_input('Fault', min_value=0, max_value=100, value=0)
        BasePolicy = st.number_input('BasePolicy', min_value=0, max_value=100, value=0)
    with row1_2:
        PolicyType = st.number_input('PolicyType', min_value=0, max_value=1000, value=0)
        VehicleCategory = st.number_input('VehicleCategory', min_value=0, max_value=1000, value=0)
        VehiclePrice = st.number_input('VehiclePrice', min_value=0, max_value=1000, value=0)
        AgeOfPolicyHolder = st.number_input('AgeOfPolicyHolder', min_value=0, max_value=100, value=0)
        AddressChange_Claim = st.number_input('AddressChange_Claim', min_value=0, max_value=100, value=0)
    with row3_0:
        button = st.button('Predict')
        if button:
            data = np.array([[AccidentArea, Sex, Age, Fault, PolicyType, VehicleCategory, VehiclePrice, AgeOfPolicyHolder, AddressChange_Claim, BasePolicy]])
            pred = model.predict(data)
            if pred == 1:
                st.write('Fraudulent')
            else:
                st.write('Not Fraudulent')