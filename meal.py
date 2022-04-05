import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import glob
from PIL import Image

# from streamlit_webrtc import webrtc_streamer
# import av
st.title('Meal recommendation')
st.text('This paragraph will only be used \nfor instructions in the first phase of the project.')

# Draw a title and some text to the app:
'''
This is some _markdown_.\n
This is some _markdown_.
'''

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Choose a source:",
    ("From file", "Take picture")
)

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a 3D uint8 tensor with TensorFlow:
    bytes_data = img_file_buffer.getvalue()
    img_tensor = tf.io.decode_image(bytes_data, channels=3)

    # Check the type of img_tensor:
    # Should output: <class 'tensorflow.python.framework.ops.EagerTensor'>
    st.write(type(img_tensor))

    # Check the shape of img_tensor:
    # Should output shape: (height, width, channels)
    st.write(img_tensor.shape)


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

## webcam streaming:
# webrtc_streamer(key='sample')
#
## search for images in data:
# images = glob.glob("data")
# index = st.number_input('Index')
#
# if st.button('Next'):
#     index += 1
#
# if st.button('Prev'):
#     if index > 0:
#         index = index -1
#
# image = Image.open(images[index])
# st.image(image, use_column_width=True)
#


in_stock = pd.DataFrame(
    {'name': ['apple', 'citron', 'banana', 'kiwi', 'milk', 'sugar', 'flour'],
     'quantity': [2, 3, 1, 2, None, None, None],
     'amount-in-grams': [None, None, None, None, None, 500, 1000],
     'amount-in-ml': [None, None, None, None, 200, None, None],
     'category': ['fresh fruits', 'fresh fruits', 'fresh fruits', 'fresh fruits', 'dairy', 'baking', 'baking']
     }
)
st.subheader('This is the database for food in stock')
st.dataframe(in_stock)  # 👈 Draw the dataframe

# %%
