import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title("My portfolio app")

page_names=['Home', 'Hi, I\'m Marta!', 'Portfolio']
page=st.radio('Please choose the page:', page_names)