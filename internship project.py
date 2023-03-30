# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:59:33 2023

@author: tabas
"""

import pickle
import numpy as np
import streamlit as st

loaded_model = pickle.load(open("C:/Users/tabas/feature_vectors",'rb'))

   #creating a function for prediction
def similarity(movies):
    sorted_similar_movies = sorted(similarity_score ,key = lambda x:x[1],reverse = True )
    print(sorted_similar_movies)
    

    
#giving the title

def main():
    
    st.title('Movie Recommendation web app')
    
    #getting the data input from the user
   																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																									
																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																									
    budget = st.text_input('budget','type here')
    genres= st.text_input('about genres','type here')
    keywords =st.text_input('about keywords','type here')
    original_language = st.text_input('about original_language','type here')
    original_title =st.text_input('about original_title','type here')
    overview=st.text_input('about overview','type here')
    popularity=st.text_input('about popularity','type here')
    production_companies=st.text_input('about production_companies','type here')
    production_countries=st.text_input('about production_countries','type here')
    release_date=st.text_input('about release_date','type here')
    revenue	=st.text_input('about revenue','type here')
    spoken_languages=st.text_input('about spoken_languages','type here')
    tagline=st.text_input('about tagline','type here')
    title=st.text_input('about title','type here')	
    cast=st.text_input('about cast','type here')
    crew=st.text_input('about crew','type here')
    director=st.text_input('about director','type here')
												
    #code for recommendation
    Result = ''
    
    #creating a button for similarity
    if st.button == ('Movie Result'):
        Result = similarity([budget,genres,keywords,original_language,original_title,overview,popularity,production_companies,production_countries,release_date,revenue,spoken_language,tagline,title,cast,crew,director])      
    st.success('the output is {}'.format (Result))
    
if __name__ == "__main__":
    main()
    