import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('word.jpg')
width,height = image.size
new_image = image.resize((1400, 300))
st.image(new_image,caption="Let's Count word!!")

my_expander = st.expander(label='CLick me :)')
with my_expander:
    user_input = st.text_input("Enter the text")



letter_counts = {}

for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
    count = user_input.count(letter)
    letter_counts[letter] = count


df = pd.DataFrame.from_dict(letter_counts, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'WordName'})

st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='WordName',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  
)
st.write(p)