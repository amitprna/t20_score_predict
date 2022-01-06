import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.title('T20 Score Predictor')

pipe = pickle.load(open('pipe.pkl','rb'))

teams = ['Pakistan','South Africa','India','New Zealand','Sri Lanka','West Indies','England','Australia','Afghanistan','Bangladesh','Ireland','Zimbabwe']

cities = ['Colombo', 'Mirpur', 'Johannesburg', 'Dubai', 'Auckland', 'Cape Town', 'London', 'Pallekele', 'Barbados', 'Sydney', 'Melbourne', 'Durban', 'St Lucia', 'Wellington', 'Lauderhill', 'Hamilton', 'Centurion', 'Manchester', 'Abu Dhabi', 'Mumbai', 'Nottingham', 'Southampton', 'Mount Maunganui', 'Chittagong', 'Kolkata', 'Lahore', 'Delhi', 'Nagpur', 'Chandigarh', 'Adelaide', 'Bangalore', 'St Kitts', 'Cardiff', 'Christchurch', 'Trinidad']

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams))

city = st.selectbox('Select city',sorted(cities))

col3,col4 = st.columns(2)

with col3:
    current_score = st.number_input('Current Score',max_value=200,key=int)
with col4:
    wickets = st.number_input('Wickets Fallen',max_value=10,key=int)
    
overs = st.slider ('Running Over',min_value=5,max_value=20)

if st.button('Predict Score'):
    balls_thrown = (overs*6)
    wickets_left = 10 -wickets
    crr = current_score/overs

    input_df = pd.DataFrame(
     {'batting_team': [batting_team], 'bowling_team': [bowling_team],'city':city, 'current_score': [current_score],'balls_thrown': [balls_thrown], 'wickets_left': [wickets]})
    result = pipe.predict(input_df)
    st.header("Predicted Score - " + str(int(result[0])))
    st.balloons()
