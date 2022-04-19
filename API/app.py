#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 00:02:52 2021

@author: tushar
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image

pickle_in = open("classifier.pkl","rb")
classifier = pickle.load(pickle_in)


def welcome():
    return "Welcome All"

def predict_note_authentiction(variance,skewness,curtosis,entropy):
    
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction

def main(): 
    html_temp="""
    
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Bank Authenticator ML APP<h2>
    </div>
    
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    variance = st.text_input("Varience","Type Here")
    skewness = st.text_input("Skewness","Type Here")
    curtosis = st.text_input("Curtosis","Type Here")
    entropy = st.text_input("Entropy","Type Here")
    
    result=""
    
    if st.button("Predict"):
        result=predict_note_authentiction(variance, skewness, curtosis, entropy)
    st.success('The output is{}'.format(result))
    
    if st.button("About"):
        st.text("Lets Leran")
        st.text("Built with Stremlit")
        
if __name__=='__main__':
    main()
        
    

