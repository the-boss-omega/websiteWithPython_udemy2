import streamlit as st
import pandas
data = {
  'x': [1,3,5,7,9,11,13],
  'y': [200,400,600,800,1000,1200,1400]
}
df = pandas.DataFrame(data)
st.title('the king of the dice')
st.subheader('introdocing the first special digita lotter')
st.write('''click here to try the win
enjoy it but npt to much''')
st.write(df)
st.line_chart(df)
st.area_chart(df)
myslider = st.slider('Celsius')
st.write(myslider,'in farenheit',myslider * 9/5 + 32)
