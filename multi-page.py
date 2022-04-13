import streamlit as st
from streamlit_multipage import MultiPage
from streamlit_option_menu import option_menu
import pandas as pd


def input_page(st, **state):
    st.title("Body Mass Index")

    # upload and read files:
    uploaded_file = st.file_uploader("Or choose a file", type=['png', 'jpg'])
    if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

    # weight_ = state["weight"] if "weight" in state else 0.0
    # weight = st.number_input("Your weight (Kg): ", value=weight_)
    #
    # height_ = state["height"] if "height" in state else 0.0
    # height = st.number_input("Your height (m): ", value=height_)
    #
    # if height and weight:
    #     MultiPage.save({"weight": weight, "height": height})


def compute_page(st, **state):
    st.title("Body Mass Index")

    if "weight" not in state or "height" not in state:
        st.warning("Enter your data before computing. Go to the Input Page")
        return

    weight = state["weight"]
    height = state["height"]

    st.metric("BMI", round(weight / height ** 2, 2))


app = MultiPage()
app.st = st

app.add_app("Input Page", input_page)
app.add_app("BMI Result", compute_page)

# 3. CSS style definitions
selected3 = option_menu(None, ["Home", "Upload",  "Tasks", 'Settings'],
                        icons=['house', 'cloud-upload', "list-task", 'gear'],
                        menu_icon="cast", default_index=0, orientation="horizontal",
                        styles={
                            "container": {"padding": "0!important", "background-color": "#fafafa"},
                            "icon": {"color": "orange", "font-size": "25px"},
                            "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                            "nav-link-selected": {"background-color": "green"},
                        }
                        )
app.run()
