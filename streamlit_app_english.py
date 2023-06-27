#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import streamlit as st

tasks = pd.read_csv('little_red_cap.csv')
st.write(tasks)

st.header('Генератор упражнений по английскому')

'---'
# def load_data():
#     df = pd.read_csv('little_red_cap.csv')
#     return df

# df = load_data() 
# st.write(df)

for task in tasks:
    st.write('')
    st.write(str(task['description']))
    
#     col1, col2 = st.columns(2)
#     with col1:
#         st.write('')
#         st.write(str(task['raw']))
        
#     with col2:
#         for i in range(len(task['options'])):
#             option = task['options'][i]
#             task['result'][i] = st.selectbox('nolabel', 
#                                              ['–––'] + option, 
#                                              label_visibility="hidden")
#             if task['result'][i] == '–––':
#                 pass
#             elif task['result'][i] == task['answers'][i]:
#                 st.success('', icon="✅")
#             else:
#                 st.error('', icon="😟")
#     task['total'] = task['result'] == task['answers']    
#     '---'        

# total_sum = sum(task['total'] for task in tasks)

# if total_sum == len(tasks):
#     st.success('Успех!')
#     st.balloons()

