import streamlit as st
import PIL
import streamlit as st
import psycopg2
import psycopg2.extras
from sqlalchemy import create_engine
import pandas
from PIL import Image
import streamlit as st
import streamlit_multipage 

def app():
    st.title("DB Price App")
    st.header("Anleitung")
    image=Image.open("website.png")
    c=st.container()
        
    st.image(image,caption="DB Ticker-App")

    st.subheader("Beschreibung")

