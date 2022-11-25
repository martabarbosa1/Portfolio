import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
# import plotly.express as px

from wordcloud import WordCloud, ImageColorGenerator


from streamlit_option_menu import option_menu
from PIL import Image


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
            
        col1, col2 = st.columns(2, gap = 'large')
        with col1:
            st.title("Soft-Skills")
               
            # Create text
            text = 'curious curious curious responsible responsible responsible proactive proactive proactive keen_eye \
            keen_eye teamwork teamwork teamwork adaptability adaptability Communication Communication creative creative creative creative \
            problem_oriented problem_oriented listening listening listening critical_thinking critical_thinking critical_thinking planning planning Honesty Honesty'

            # Create and generate a word cloud image:                   
            cloud_mask = np.array(Image.open("./Images/cloud_sil.jpg"))
            plt.imshow(cloud_mask)
            plt.axis("off")

            # Create wordcloud
            wordcloud = WordCloud(background_color="white", 
                      mask=cloud_mask,
                      contour_width=1, 
                      repeat=True, contour_color='white',
                      min_font_size=3)

            # Generate a wordcloud
            wordcloud.generate(text)

            # store to file
            wordcloud.to_file("./Images/cloud_sil_wordcloud.png")

            # show

            plt.imshow(wordcloud)
            plt.axis("off")
            st.pyplot()
      
            
            
            
        with col2:
            st.title("Tech-Skills")      

if selected == 'Portfolio':
        st.title('This is my Portfolio')
        

