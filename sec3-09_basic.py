import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


### titleの追加
st.title('Streamlit 超入門')

### テキストを追加
st.write('DataFrame')

df = pd.DataFrame(
    # np.random.rand(20, 3),  # 縦に20、横に3つの行列を作る 正規分布に従う乱数
    # columns=['a', 'b', 'c']
    np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],  # 縦に100、横に2つの行列を作る正規分布に従う乱数 → 各列を50で割る → 新宿付近の緯度経度を足す
    columns=['lat', 'lon']  # latitude (緯度), longitude (軽度)
)

### dfをwebアプリ上に表示
# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0), width=500, height=200)   # 列(axis=0)の中で最大のものをハイライト 行ならaxis=1
# st.table(df.style.highlight_max(axis=0))   # 静的な表

### map
st.map(df)


### magic command
## markdown記法
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

### チャートを各
## 折れ線グラフ
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

### 画像表示
st.write('Display Image')
img = Image.open('C:/Users/0000405047/OneDrive - Sony/画像/PC壁紙/cat3.jfif')   # pythonでpathを表現するときは\ではなく/を使おう
st.image(img, caption='cat', use_column_width=True)  # use_column_widthは、実際のwebアプリの横幅に合わせてくれる

