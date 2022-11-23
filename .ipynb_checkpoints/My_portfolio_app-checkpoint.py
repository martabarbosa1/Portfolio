import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
# import plotly.express as px

# import nltk
# nltk.download('punkt')
# from wordcloud import WordCloud

# import nltk
# nltk.download()
# from wordcloud import WordCloud

from streamlit_option_menu import option_menu
from PIL import Image

# This code is different for each deployed app.
CURRENT_THEME = "blue"
IS_DARK_THEME = True
EXPANDER_TEXT = """
    This is a custom theme. You can enable it by copying the following code
    to `.streamlit/config.toml`:
    ```python
    [theme]
    primaryColor = "#E694FF"
    backgroundColor = "#00172B"
    secondaryBackgroundColor = "#0083B8"
    textColor = "#C6CDD4"
    font = "sans-serif"
    ```
    """

st.set_page_config(page_title="Marta_Barbosa_app", layout="wide", menu_items=None)

with st.sidebar:
        selected = option_menu("Main Menu", ['Home', 'Hi, I\'m Marta!', 'Portfolio'], 
            icons=['house'], menu_icon="cast", default_index=1)
        
        #Source: https://discuss.streamlit.io/t/streamlit-option-menu-is-a-simple-streamlit-component-that-allows-users-to-select-a-single-item-from-a-list-of-options-in-a-menu/20514
        
if selected == 'Home':
        st.title("My portfolio app")
        st.write('some text')

if selected == 'Hi, I\'m Marta!':
        st.title("Hi, I\'m Marta!")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write('some text about me')            
        with col2:
            image1 = Image.open('./Images/Capturar1.JPG')
            st.image(image1, width = 500)
            
        col1, col2 = st.columns(2)
        with col1:
            st.title("Soft-Skills")
            
            text = 'curious, curious, curious, responsible, responsible, pro-active, pro-active, pro-active'
            wordcloud = WordCloud(width=480, height=480, max_font_size=200, min_font_size=10)
            wordcloud.generate_from_text(text)
            plt.figure()
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.margins(x=0, y=0)
            plt.show()
            
        with col2:
            st.title("Hard-Skills")      

if selected == 'Portfolio':
        st.title('This is my Portfolio')
        
        
        
import streamlit as st
import plotly.figure_factory as ff
import numpy as np

