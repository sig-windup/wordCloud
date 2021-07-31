#텍스트
text="공주맛 쿠키 마법사맛 쿠키 해적맛 쿠키 커스터드 3세맛 쿠키 쿠키런 킹덤 해적맛 쿠키 펫 유령"

#wordcloud 생성
from wordcloud import WordCloud
import matplotlib.pyplot as plt

wordcloud= WordCloud(font_path='C:/Windows/Fonts/HYDNKB.TTF', background_color='white').generate(text)

#이미지 출력 및 저장
plt.figure(figsize=(22,22)) #이미지 크키
plt.imshow(wordcloud, interpolation='lanczos') #이미지의 부드럽기 정도
plt.axis('off') #x y축 제거
#plt.show()
plt.savefig('wordCloud1.png') #파일명으로 저장
