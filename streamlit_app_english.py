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
         if row['type']=='select_word' or row['type']=='missing_word':
                st.write('')
                st.write(str.replace(row['raw'], row['object'], '___'))
                
        elif row['type']=='noun_phrases':
            st.write('')
            st.write(str.replace(row['raw'], row['object'], "\033[34m{}".format(row['object'])))

#         st.write('')
#         st.write(str(row['raw']))
        
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
            st.success('Correctly', icon="💪")
        else:
            st.error('Mistake', icon="🤷‍♂️")
    
    if row['result'] == row['answer']:
        row['total'] = 1      
    '---'
#     row['total'] = row['result'] == row['answers']
#     total_sum = sum(row['total'])
#     if total_sum == len(tasks):
#         st.success('Поздравляем! Вы ответили на все вопросы!')
#         st.balloons()

# total_sum = sum(tasks['total'])

# if total_sum == len(tasks):
#     st.success('Поздравляем! Вы ответили на все вопросы!')
#     st.balloons()

