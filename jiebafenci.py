import jieba

with open('sanguo2.txt', 'r', encoding='utf-8') as f:
    txt = f.read()
    a = jieba.lcut(txt)
    word = []
    for i in a:
        if len(i) > 1 and a.count(i) >= 50 and i not in word:
            word.append(i)
print(word)
