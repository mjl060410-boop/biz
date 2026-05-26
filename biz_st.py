import streamlit as st

st.title('첫 번째 웹사이트')

"이건 부제목"

"#첫 번째 웹사이트"

"""
비즈니스 모델 분석

[네이버](https://www.naver.com)  
[홍익대학교](https://www.hongik.ac.kr)

이것이 일반 본문**이것이 굵은 글씨** *이것이 기울임 글씨* ~~이것이 취소선~~

:red[빨간색 글씨]:green[초록색 글씨]:blue[파란색 글씨]

```python
import streamlit as st
print("코드 블록")
```

"""
import streamlit as st
st.caption('캡션(작고흐린 글씨로 표현됨):st.caption()')

with st.echo():
    #이 블록의 코드와 결과를 출력
    name='chunghun Ha'
    st.write("Hello,streamlit",name)


st.latex('\int_a^bf(x)dx')
"$$\int_a^bf(x)dx$$"


st.image("./data/python설명.jpeg",caption="파이썬 로고",width=500)
st.audio("./data/소리.mp3",format="audio",loop=True)
video_file=open("./data/우주.mp4","rb")
video_bytes=video_file.read()
st.video(video_bytes)
st.divider()


"""
|---|---|---|
|이름|학번|학과|
|홍길동|20230001|컴퓨터공학과|
|김철수|20230002|전자공학과|
|이영희|20230003|기계공학과|
"""

'# :blue[시각화 라이브러리]'

'##### :orange[Matplotlib: st.pyplot()]'
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,100)
y=np.sin(x)

fig, ax=plt.subplots()
ax.plot(x,y)
st.pyplot(fig)
