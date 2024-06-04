import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


### titleの追加
st.title('Streamlit 超入門')

st.write('Interactive Widgets')

### checkbox
# if st.checkbox('Show Image'):   # True Falseを返す
#     img = Image.open('C:/Users/0000405047/OneDrive - Sony/画像/PC壁紙/cat3.jfif')   # pythonでpathを表現するときは\ではなく/を使おう
#     st.image(img, caption='cat', use_column_width=True)  # use_column_widthは、実際のwebアプリの横幅に合わせてくれる

### select box
# option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1,11))   # 1~10のリスト
# )   # ここでoptionの値を動的に変えられる
## 実はst.writeを使わなくても書ける
# 'あなたの好きな数字は、', option, 'です。'

### text input
# text = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味：', text

### slider
condition = st.slider('あなたの今の調子は？', 0, 100, 50)   # [最小値] [最大値] [default値]
'コンディション：', condition
