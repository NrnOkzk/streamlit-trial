import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


### titleの追加
st.title('Streamlit 超入門')

### sidebar
# st.sidebar.write('Interactive Widgets')
# text = st.sidebar.text_input('あなたの趣味を教えてください。')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)   # [最小値] [最大値] [default値]

st.write('Interactive Widgets')

### 2 columns
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:  # ボタンが押される
    right_column.write('ここは右カラム')

### expander    FAQでよく使われる
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')

# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)   # [最小値] [最大値] [default値]
# 'あなたの趣味：', text
# 'コンディション：', condition

