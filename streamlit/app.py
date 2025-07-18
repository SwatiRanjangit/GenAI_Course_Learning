import streamlit as s
import pandas as p
import numpy as np


#Title

s.title("Hello streamlit")

# simple text
s.write("This is a plain text")

# create simple dataframe

df = p.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})

# display dataframe

s.write("Here is dataframe")
s.write(df)


#create aline chart 

#create chart data

chart_data = p.DataFrame(
    np.random.randn(10,3),columns=['a','b','c']
)

s.line_chart(chart_data)