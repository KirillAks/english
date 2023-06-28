#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import streamlit as st

tasks = pd.read_csv('little_red_cap.csv')
tasks

st.header('Генератор упражнений по английскому')

'---'

for i, row in tasks.iterrows():
    row['description']
    
    col1, col2 = st.columns(2)
    with col1:
        st.write('')
        st.write(str(row['raw']))
        
    with col2:
        opt = str(row['options'])
        opt
        option = st.selectbox(
            'nolabel',
            (opt),
            label_visibility="hidden",
        )
#         st.write('You selected:', option)
#         for i in range(len(row['options'])):
#             opt = row['options'][i]
#             option = st.selectbox(
#                 'nolabel',
#                 (['None'].extend(opt)),
#                 label_visibility="hidden",
#             )
            
           
#             row['result'][i] = st.selectbox('nolabel', 
#                                              ['–––'].extend(option), 
#                                              label_visibility="hidden")
#             if row['result'][i] == '–––':
#                 pass
#             elif row['result'][i] == row['answers'][i]:
#                 st.success('', icon="✅")
#             else:
#                 st.error('', icon="😟")
#     row['total'] = row['result'] == row['answers']    
#     '---'        

# total_sum = sum(task['total'] for task in tasks)

# if total_sum == len(tasks):
#     st.success('Успех!')
#     st.balloons()
    

