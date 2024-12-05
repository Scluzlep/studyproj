import jieba

with open('sanguo.txt', 'r', encoding='utf-8') as f:
    txt = f.read()
    a = jieba.lcut(txt)
    word_count = {}
    for i in a:
        if len(i) > 1:
            if i in word_count:
                word_count[i] += 1
            else:
                word_count[i] = 1
#     word = [i for i in word_count if word_count[i] >= 50]
# print(word)
top_30_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:30]

for word, count in top_30_words:
    print(f'{word}: {count}')