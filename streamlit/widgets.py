import streamlit as s
import pandas as p

s.title("Streamlit Text input")

name=s.text_input("Enter your name: ")
if name:
    s.write(f"Hello , {name}")

age=s.slider("Select your age: ",0,100,25)
s.write(f"Your age is: {age}")
options=["Python","C++","Java","DOT.NET"]
choice= s.selectbox("Choose your favourite laguage: ",options)
s.write(f"your favouite language is: {choice} ")

data = {
    "Name": ['jhon','riya','sita'],
    "Age": [22,24,34],
    "City": ['patna','up','delhi']
}

df = p.DataFrame(data)
df.to_csv("sampledata.csv")
s.write(df)

uploade_files=s.file_uploader("Choose a CSV file",type="csv")

if uploade_files is not None:
    df=p.read_csv(uploade_files)
    s.write(df)
