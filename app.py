import streamlit as st 
from PIL import Image
import joblib as jb

#____________________ Page configuration


st.set_page_config(
    layout='centered',
)
#____________________ Variables

image_path = 'blood_test.png'

#____________________Loading Data

#load model
jb.load('blood_model.pkl')

#____________________ Functions
@st.cache_resource
def load_img(image_file):
    # Leer la imagen
    image = Image.open(image_file)    
    return image

col1, col2 , col3 = st.columns([1,1,1], gap='large')

with col2:
    st.image(load_img(image_path), use_column_width=True)

with st.form('my_form', clear_on_submit=True):

    t1, t2, t3 = st.tabs(['Personal Information', 'Load test results', 'Review'])

    with t1:
        c1,c2 = st.columns(2, gap='large')
        with c1:
            name = st.text_input('Name', placeholder='Input name ....')
        with c2:
            lastname = st.text_input('Lastname', placeholder='Input lastname ....')
        
        c3, c4, c5 = st.columns([1,2,4], gap='small')
        with c3:
            age = st.text_input('Age', placeholder='Input...')
        with c4:
            gender = st.selectbox('Select gender', ('Female', 'Male'),index=None, placeholder='Choose an option')
        with c5:
            email = st.text_input('Email', placeholder='Input Email.....')
            
        
            
    submit_button = st.form_submit_button("Submit", disabled=True)
    
st.divider()
st.markdown('''
                :grey[*Please fill all the form information....*]
                ''')