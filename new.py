import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from PIL import Image
import numpy as np
import cv2
import pandas as pd
from st_aggrid import AgGrid
import plotly.express as px
import io

# %%
data = [
    ['mango-smoothie', 1, ['mango', 'milk'], 'Cut the mango in pieces. Fill 0.5l of milk into a blender, add mango pieces and blend.'],
    ['banana-smoothie', 1, ['banana', 'milk'], 'Cut 2 bananas in pieces. Fill 0.5l of milk into a blender, add mango pieces and blend.'],
    ['kiwi-smoothie', 1, ['kiwi', 'milk'], 'Cut 2 kiwis in pieces. Fill 0.5l of milk into a blender, add mango pieces and blend.']
    ]

with st.sidebar:
    choose = option_menu(None, ["About", "Groceries", "Recipes", "Storage"],
                         icons=['house', 'camera fill', 'collection', 'basket'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
                             "container": {"padding": "5!important", "background-color": "#fafafa"},
                             "icon": {"color": "black", "font-size": "25px"},
                             "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px",
                                          "--hover-color": "#eee"},
                             "nav-link-selected": {"background-color": "#02ab21"},
                         }
                         )
# %%
logo = Image.open(r'app/data/groceries.jpeg')

if choose == "About":
    col1, col2 = st.columns([0.8, 0.2])
    with col1:  # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #009500;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">About the meal recommender</p>', unsafe_allow_html=True)
    with col2:  # To display brand log
        st.image(logo, width=130)

    st.write("Cooking is a hobby for some and a major problem for others. However, you can always use a helping hand for cooking.\n"
             "\nAs many are working in home office nowadays, it is often a difficult decision to decide what to eat for lunch or dinner.\n"
             "\nIt often happens that one does not know which food items are in the kitchen, it is always a challenge to decide what to cook for a meal.\n"
             "\nThis inspired me to create a system that can recommend recipes based on ingredient suggestions.")

# %%
elif choose == "Groceries":
    col1, col2 = st.columns([0.8, 0.2])
    with col1:  # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #009500;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Upload a photo of your groceries here...</p>', unsafe_allow_html=True)
        st.write("This page analysis your photo and adds the ingredients to your storage cabin.\n"
                 "\nIt then recommends you the best dish with the ingredients that are available.")
    with col2:  # To display brand logo
        st.image(logo, width=150)
    # Add file uploader to allow users to upload photos
    uploaded_file = st.file_uploader("", type=['jpg', 'png', 'jpeg'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)

        col1, col2 = st.columns([0.5, 0.5])
        with col1:
            st.markdown('<p style="text-align: center;">Before</p>', unsafe_allow_html=True)
            st.image(image, width=300)

        with col2:
            st.markdown('<p style="text-align: center;">After</p>', unsafe_allow_html=True)

            converted_img = np.array(image.convert('RGB'))
            gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
            inv_gray = 255 - gray_scale
            blur_image = cv2.GaussianBlur(inv_gray, (125, 125), 0, 0)
            sketch = cv2.divide(gray_scale, 255 - blur_image, scale=256)
            st.image(sketch, width=300)

# %%
elif choose == "Recipes":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #009500;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Collection of your recipes</p>', unsafe_allow_html=True)

    st.subheader('Here are your recipes listed')
    df = pd.DataFrame(data, columns=['name', 'portion', 'ingredients', 'instructions']
                      )

    st.dataframe(df)




# %%
elif choose == "Storage":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #009500;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Storage</p>', unsafe_allow_html=True)
    st.subheader('Import Data into Python')
    st.markdown(
        'To start a data science project in Python, you will need to first import your data into a Pandas data frame.')

