import streamlit as st
import matplotlib.pyplot as plt
from bokeh.plotting import figure
import plotly.figure_factory as ff
import numpy as np
import pandas as pd

st.title('My streamlit first app')

st.title('My app title is : Wonderfuf app')
st.write('hello,*World!*:sunglasses: ')

st.write('st.write accept text, but also other data formats, such as numbers,data frames, styled data frames, and sassorted objects,... ')
st.write(1,2,3,4)
st.write(pd.DataFrame(
    {'first column':[1,2,3,4],
    'second column':[10,20,30,40]
    }
))

data_frame=pd.DataFrame(np.random.randn(200,3),columns=['a','b','c'])
st.write('st.write accepts also multiple arguments like ')
st.write('1=1=',2)
st.write('below is DataFrame:',data_frame,'Above is a dataframe')
st.title('Displaying data elements with code snippets:')
