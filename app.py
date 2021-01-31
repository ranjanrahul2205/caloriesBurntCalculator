import streamlit as st
import pickle
import numpy as np
import emoji

model = pickle.load(open('model.pkl', 'rb'))


def caloriesBurnt(gender, age_input, height, weight, duration):
	prediction = model.predict([[gender, age_input, height, weight, duration]])
	#prediction = prediction.astype(np.int) #ndarray to int
	return prediction[0]

st.title('Calculate calories you burnt today! ' + '\U0001F3CB')

gender_input = st.radio('Select your gender :', ('Male', 'Female'))
st.write('\n')

age_input = st.slider("Enter your age : ", 10, 100)
st.write('Age:', age_input, 'years')

st.write('\n')
height_input = st.text_input('Enter height in cms')

st.write('\n')
weight_input = st.text_input('Enter weight in kgs')

st.write('\n')
duration_input = st.text_input('Enter duration of your workout in minutes')

st.write('\n')
error_code = 0


if st.button('Submit'):
    if(weight_input.isnumeric()):
      weight = int(weight_input)
    else :
      st.error('Invalid weight')
      error_code = 1

    if(height_input.isnumeric()):
        height = int(height_input)
    else :
        st.error('Invalid height')
        error_code = 1

    if(duration_input.isnumeric()):
      duration = int(duration_input)
    else :
      st.error('Invalid duration')
      error_code = 1
    
    if(gender_input == 'Male'):
      gender = 1
    else:
      gender = 0
    
    if(error_code == 0):
      result = caloriesBurnt(gender, age_input, height, weight,duration)
      st.success(str(result) + ' burnt today, Keep going. ' + '\U0001F525')








	




