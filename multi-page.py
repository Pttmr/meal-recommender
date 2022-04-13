import streamlit as st
import pandas as pd
from streamlit_multipage import MultiPage
from streamlit_option_menu import option_menu


def upload_page(st, **state):
    st.title("Image Upload")

    st.write("Hello upload page")
    uploaded_file = st.file_uploader("Or choose a file", type=['png', 'jpg'])
    # if uploaded_file is not None:
    # To read file as bytes:
    #     bytes_data = uploaded_file.getvalue()
    #     st.write(bytes_data)

    # # To convert to a string based IO:
    #     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    #     st.write(stringio)
    #
    # # To read file as string:
    #     string_data = stringio.read()
    #     st.write(string_data)
    #
    # # Can be used wherever a "file-like" object is accepted:
    #     dataframe = pd.read_csv(uploaded_file)
    #     st.write(dataframe)



def recommender_page(st, **state):
    st.title("This page recommends you the best dish with the ingredients that are available")


app = MultiPage()
app.st = st

app.add_app("Image upload", upload_page)
app.add_app("BMI Result", recommender_page)

selected3 = option_menu(None, ["Home", "Upload",  "Recipes", 'Storage'],
                        icons=['house', 'cloud-upload', "collection", 'basket'],
                        menu_icon="cast", default_index=0, orientation="horizontal",
                        styles={
                            "container": {"padding": "0!important", "background-color": "#fafafa"},
                            "icon": {"font-size": "25px"},
                            "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                            "nav-link-selected": {"background-color": "green"},
                        }
                        )
app.run()
