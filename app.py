import streamlit as st 
#from PIL import Image
import joblib as jb

#____________________ Page configuration


st.set_page_config(
    layout='centered',
)

#____________________ Variables

image_path = 'blood_test.png'

Age = 20
BMI = 16
Chol = 10
TG = 5
HDL = 5
LDL = 5
BUN = 5

#____________________Loading Data

#load model
model = jb.load('blood_model.pkl')

#____________________ Functions
# @st.cache_resource
# def load_img(image_file):
#     # Leer la imagen
#     image = Image.open(image_file)    
#     return image

col1, col2 , col3 = st.columns([1,1,1], gap='large')

with col2:
    st.image(image_path, use_column_width=True)
    
with st.form('my_form', clear_on_submit=True):
    b_activation = True 
    
    
    c1,c2,c3 = st.columns(3, gap='small')
    with c1:
        name = st.text_input('Name', placeholder='Input name ....')
    with c2:
        lastname = st.text_input('Lastname', placeholder='Input lastname ....')
    with c3:
        id = st.text_input('id', placeholder='Input id ....')
        
    c4, c5, c6 = st.columns([1,2,4], gap='small')
    with c4:
        age = st.text_input('Age', placeholder='Input...')
    with c5:
        gender = st.selectbox('Select gender', ('Female', 'Male'),index=None, placeholder='Choose an option')
    with c6:
        email = st.text_input('Email', placeholder='Input Email.....')
    
    
    # st.markdown('''
    #                 :green[*Labs' results __________________________________*]
    #                 ''')
    
    c7,c8,c9 = st.columns(3, gap='large')
    with c7:
        bmi= st.slider('BMI', 16.0,45.0,16.0)
    with c8:
        Cr = st.slider('Cr', 20.0,200.0,20.0 )  
    with c9:
        BUN = st.slider('BUN', 0.0,25.0,0.0)
        
    u1,u2,u3,u4 = st.columns(4, gap='large')
    with u1:
        TG= st.slider('TG', 0.0,30.0,0.0)
    with u2:
        Chol= st.slider('Chol', 0.0,15.0,0.0)
    with u3:
        HDL= st.slider('HDL', 0.0,30.0,0.0)
    with u4:
        LDL= st.slider('LDL', 0.0,19.0,0.0) 
            
    with st.expander("Reference' values"):  
        st.markdown('''                
                Body Mass Index (BMI) = 16 - 45 \n
                Total Cholesterol (Chol) = 0 - 11.6 \n
                Triglycerides (TG) = 0 - 18 \n
                High-Density Lipoprotein (HDL) = 0 - 10 \n
                Low-Density Lipoprotein (LDL) = 0.3 - 9.9 \n
                Blood Urea Nitrogen (BUN) = 0.5 - 25 \n
                Creatinina (Cr) = 20 - 200 \n
                
                ''')    
    
      
    s_button = st.form_submit_button("Submit", disabled=False)  


# st.markdown('''
#                 :gray[*Please fill all the form information....*]
#                 ''')

#_________________ Logic

test_result =[
    Age, BMI, Chol, TG, HDL, LDL, BUN
]


if s_button:
    
    w_pred = model.predict([test_result])
    result = int(w_pred[0])
    
    if result == 1:
        st.subheader("⚠️⚠️High risk of diabetes. report to the doctor⚠️⚠️")
        
        
    elif result == 0:
        st.subheader("patient's blood test registered successfully  ✅")
        
    
    
