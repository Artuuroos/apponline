 
from http.client import CONFLICT
from re import X
from telnetlib import DO
from typing import Collection
import streamlit as st
import psycopg2
import psycopg2.extras
from sqlalchemy import create_engine
import pandas
from bs4 import BeautifulSoup
import requests
import time 
from time import sleep
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import plotly.express as px 
import plotly
from matplotlib import dates as mpl_dates
from cProfile import label
from distutils.cmd import Command
import datetime 
from streamlit.cli import main  
from streamlit.proto.RootContainer_pb2 import RootContainer
import pandas as pd 
import plotly.figure_factory as ff
import numpy as np
from streamlit_option_menu import option_menu 
import yagmail
from dbTable import *
from http.client import CONFLICT
from re import X
from telnetlib import DO
from typing import Collection
import smtplib, ssl
def app():
    st.title("Preisvorhersage/Diagramm")

    conn = psycopg2.connect(host ="dpg-cajo73sgqg428kba9ikg-a.frankfurt-postgres.render.com",
                            database="dbticket", 
                            user="dbticket_user", 
                            password="Nhaema5GzFDyW3j0sGHVYjfhRBu0fTvy")

    engine = create_engine('postgresql://dbticket_user:Nhaema5GzFDyW3j0sGHVYjfhRBu0fTvy@dpg-cajo73sgqg428kba9ikg-a.frankfurt-postgres.render.com/dbticket')
    cursor = conn.cursor()
    
    
    coll1,coll2=st.columns(2)
    with coll1:
            loginname=st.text_input("Login: ",st.session_state.name)
            loginpassw=st.text_input("Passwort:",type="password")
            anfragenlistebenutzer=[]
            with st.form(key='form3'):
                lo = st.form_submit_button(label='Einloggen')
            
            def Login(loginname,loginpassw):
                abfrage = cursor.execute("SELECT login.username FROM login WHERE username=%s", [loginname])
                if not cursor.fetchone():  # An empty result evaluates to False.
                    st.write("Kein Benutzer mit diesem Benutzernamen")
                else:
                    abfragep = cursor.execute("""SELECT login.passwort FROM login WHERE passwort=%s""", [loginpassw])
                    if not cursor.fetchone():  # An empty result evaluates to False.
                        st.write("Falsches Passwort")
                    else:
                        st.write("Sie haben sich erfolgreich eingeloggt")
                        
            def zuordnen(loginname):
                richtigentabellen=cursor.execute("Select anfragen.tabelle from anfragen where username=%s", [loginname])
                alleanfragen=cursor.fetchall()
                if alleanfragen==None:
                    st.info("Zu diesem Benutzernamen gibt es noch keine Tabelle") 
                else:
                    for tabell in alleanfragen:
                        anfragenlistebenutzer.append(tabell[0])
                    st.selectbox("Tabelle: ", anfragenlistebenutzer)
            if lo:   
                Login(loginname,loginpassw)
            with coll2:         
                with st.form(key='form10'):
                    st.text_input("Benutzer",loginname)
                    tab=st.form_submit_button(label='Tabellen zeigen')
            if tab:  
                zuordnen(loginname)