import jieba
from wordcloud import WordCloud

fonts = 'simhei.ttf'
with open('sanguo2.txt', 'r', encoding='utf-8') as f:
    txt = f.read()
a = jieba.lcut(txt)
word_counts = {}
for i in a:
    if len(i) > 1:
        if i in word_counts:
            word_counts[i] += 1
        else:
            word_counts[i] = 1

wc = WordCloud(width=1920, height=1080, background_color='white', mode='RGB', font_path=fonts)
wc.generate_from_frequencies(word_counts)
wc.to_file('wordcloud.png')
