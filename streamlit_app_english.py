#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import streamlit as st

tasks = pd.read_csv('little_red_cap.csv')
tasks
tasks['options'] = tasks.apply(lambda row: eval(row['options']), axis=1)
tasks['result'] = tasks.apply(lambda row: eval(row['result']), axis=1)
tasks

st.header('Упражнения по английскому')

'---'
for i, row in tasks.iterrows():
    st.subheader(row['description'])
 
    
    col1, col2 = st.columns(2)
    with col1:
        st.write('')
        st.write(str(row['raw']))
        
    with col2:
        option = row['options']

        row['result'] = st.selectbox(
            'nolabel',
            ['–––'] + option,
            key = f"{i}",
            label_visibility="hidden",            
        ) 
        if row['result'] == '–––':
            pass
        elif row['result'] == row['answer']:
            st.success('', icon="✅")
        else:
            st.error('', icon="😟")


    row['total'] = row['result'] == row['answer']    
    '---'        

total_sum = sum(task['total'] for task in tasks)

if total_sum == len(tasks):
    st.success('Поздравляем! Вы ответили на все вопросы!')
    st.balloons()

