queries = [
'смотреть сериалы онлайн',
'новости спорта',
'афиша кино',
'курс доллара',
'сериалы этим летом',
'курс по питону',
'сериалы про спорт',
]

words_count = []
for line in queries:
    words = line.split()
    words_count.append(len(words))
    
words_count.sort()
words_count_uniq = []

for key in words_count:
    if key not in words_count_uniq:
        words_count_uniq.append(key)

full_queries = len(queries)
for key in words_count_uniq:
    var = (words_count.count(key)*100/full_queries)
    var = round(var, 2)
    var = str(str(var) + "%")
    print("Поисковых запросов, содержащих", key, "слов(a):", var)


