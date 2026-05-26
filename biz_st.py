import streamlit as st

st.title('첫 번째 웹사이트')

"이건 부제목"

"#첫 번째 웹사이트"


'# :blue[시각화 라이브러리]'

'##### :orange[Matplotlib: st.pyplot()]'
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,100)
y=np.sin(x)

fig, ax=plt.subplots()
ax.plot(x,y)
st.pyplot(fig)
