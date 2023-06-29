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
        option = (row['options']).translate({ord(i): None for i in "']["})
        option = option.split(",")

        row['result'] = st.selectbox(
            'nolabel',
            ['–––'] + option,
            label_visibility="hidden",
        ) 
        if row['result'] == '–––':
            pass
        elif row['result'] == row['answer']:
            st.success('', icon="✅")
        else:
            st.error('', icon="😟")


#     row['total'] = row['result'] == row['answer']    
    '---'        

# total_sum = sum(task['total'] for task in tasks)

# if total_sum == len(tasks):
#     st.success('Успех!')
#     st.balloons()

