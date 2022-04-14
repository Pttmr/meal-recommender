import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image, ImageOps
import pandas as pd
import numpy as np
import tensorflow as tf
import joblib


# %%
# loading the classifier model1
# model1 = joblib.load("model1.pkl")
reconstructed_model1 = tf.keras.models.load_model('/home/bee110493/.config/JetBrains/DataSpell2021.3/projects'
                                                      '/meal-recommender/model1')

# model2 = tf.keras.models.load_model("model1.pkl")
# %%


data = [
    ['apple-juice', 1, ['apple', 'water'],
     'Cut and peel 2 apples. Fill 0.5l of water into a blender, add apple pieces and blend.'],
    ['banana-smoothie', 1, ['banana', 'milk'],
     'Cut 2 bananas in pieces. Fill 0.5l of milk into a blender, add mango pieces and blend.'],
    ['orange-juice', 1, ['orange', 'water'],
     'Cut 2 oranges in half. Juice them with a fruit press, add water if wanted.']
]
recipe = str(data[0][0])

with st.sidebar:
    choose = option_menu(None, ["About", "Groceries", "Cooking recipes", "Fridge"],
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

    st.write(
        "Cooking is a hobby for some and a major problem for others. However, you can always use a helping hand for "
        "cooking. :tomato: \n "
        "\nAs many are working in home office 💻 nowadays, it is often a difficult decision to decide what to eat for "
        "lunch or dinner.\n "
        "\nIt often happens that one does not know which food items 🥗 are in the kitchen, it is always a challenge "
        "to decide what to cook for a meal.\n "
        "\nThis inspired me to create a system that can recommend recipes 📔  based on ingredient suggestions.")



# %%
elif choose == "Groceries":
    col1, col2 = st.columns([0.8, 0.2])
    with col1:  # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #009500;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Upload a photo of your groceries here...</p>', unsafe_allow_html=True)
        st.markdown("This page analysis your photo 📷 and adds the ingredients to your storage cabin.")

    with col2:  # To display brand logo
        st.image(logo, width=150)
    # Add file uploader to allow users to upload photos

    uploaded_file = st.file_uploader("", type=['jpg', 'png', 'jpeg'])
    # picture = tf.keras.preprocessing.image.load_img(uploaded_file, target_size=(100,100,3))

    if uploaded_file is not None:
        show = st.image(uploaded_file, width=130)
        # picture = tf.keras.preprocessing.image.load_img(uploaded_file, target_size=(100,100,3))

    st.markdown("It then recommends you the best dish 🍱 with the ingredients that are available. 🥳")

    if st.button("Give me a recommendation!"):
        st.write("Please upload an Image to classify!")
    else:
        with st.spinner("Classifying..."):
            #picture = tf.keras.preprocessing.image.load_img(uploaded_file, target_size=(100, 100, 3))
            #np.testing.assert_allclose(reconstructed_model1.predict(picture))

            # model1.predict(picture)
            # np.testing.assert_allclose(
            #     model1.predict(picture), reconstructed_model.predict(test_input)
            # )

            # tf.keras.Sequential([model1, tf.keras.layers.Softmax()])

            st.write(f"I recommend you try {recipe}!")


# %%
elif choose == "Cooking recipes":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #009500;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Collection of your recipes</p>', unsafe_allow_html=True)

    st.subheader('Here are your recipes listed:')
    df = pd.DataFrame(data, columns=['name', 'portion', 'ingredients', 'instructions']
                      )

    st.dataframe(df)




# %%
elif choose == "Fridge":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #009500;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Fridge</p>', unsafe_allow_html=True)
    st.subheader('Currently you have in your fridge:')

    fridge = [
        ['milk', 'ml', 2000],
        ['sugar', 'g', 500],
        ['wheat-flour', 'g', 750],
        ['butter', 'g', 150],
        ['eggs', 'count', 4],
        ['apples', 'count', 2]
    ]

    df2 = pd.DataFrame(fridge, columns=['name', 'unit', 'amount'])
    st.dataframe(df2)
