#!/usr/bin/env python
# coding: utf-8

# In[251]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import itertools as it
from collections import Counter


# In[29]:


data = pd.read_csv('movie_bd_v5.csv')
data.sample(5)


# In[220]:


data.describe()


# # Предобработка

# In[350]:


answers = {} # создадим словарь для ответов 

#добавим колонку прибыли
profit = pd.DataFrame(data.revenue - data.budget)
profit.columns = ['profit']
total = pd.concat([data, profit], axis = 1)

#добавим колонку с длинами названий
len_title = pd.DataFrame(total.original_title.apply(lambda x: len(x)))
len_title.columns = ['len_title']
new_total = pd.concat([total, len_title], axis = 1)

#добавим колонку с длинами описаний
len_overview = pd.DataFrame(total.overview.apply(lambda x: len(str(x).split(' '))))
len_overview.columns = ['len_overview']
new_total2 = pd.concat([new_total, len_overview], axis = 1)


# # 1. У какого фильма из списка самый большой бюджет?

# Использовать варианты ответов в коде решения запрещено.    
# Вы думаете и в жизни у вас будут варианты ответов?)

# In[7]:


# тут пишем ваш код для решения данного вопроса:
data[data.budget == data.budget.max()].original_title


# In[363]:


# в словарь вставляем номер вопроса и ответ на него
answers['1'] = 'Pirates of the Caribbean: On Stranger Tides'


# # 2. Какой из фильмов самый длительный (в минутах)?

# In[11]:


data[data.runtime == data.runtime.max()].original_title


# In[364]:


# в словарь вставляем номер вопроса и ответ на него
answers['2'] = 'Gods and Generals'


# # 3. Какой из фильмов самый короткий (в минутах)?
# 
# 
# 
# 

# In[13]:


data[data.runtime == data.runtime.min()].original_title


# In[365]:


# в словарь вставляем номер вопроса и ответ на него
answers['3'] = 'Winnie the Pooh'


# # 4. Какова средняя длительность фильмов?
# 

# In[14]:


data.runtime.mean()


# In[366]:


# в словарь вставляем номер вопроса и ответ на него
answers['4'] = 110


# # 5. Каково медианное значение длительности фильмов? 

# In[15]:


data.runtime.median()


# In[367]:


# в словарь вставляем номер вопроса и ответ на него
answers['5'] = 107


# # 6. Какой самый прибыльный фильм?
# #### Внимание! Здесь и далее под «прибылью» или «убытками» понимается разность между сборами и бюджетом фильма. (прибыль = сборы - бюджет) в нашем датасете это будет (profit = revenue - budget) 

# In[31]:


total[total.profit == total.profit.max()].original_title


# In[368]:


# в словарь вставляем номер вопроса и ответ на него
answers['6'] = 'Avatar'


# # 7. Какой фильм самый убыточный? 

# In[32]:


total[total.profit == total.profit.min()].original_title


# In[369]:


# в словарь вставляем номер вопроса и ответ на него
answers['7'] = 'The Lone Ranger'


# # 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?

# In[34]:


total[total.profit > 0].count()


# In[370]:


# в словарь вставляем номер вопроса и ответ на него
answers['8'] = 1478


# # 9. Какой фильм оказался самым кассовым в 2008 году?

# In[300]:


total[total.release_year == 2008].profit.sort_values(ascending=False)


# In[301]:


total[total.profit == 816921825].original_title


# In[371]:


# в словарь вставляем номер вопроса и ответ на него
answers['9'] = 'The Dark Knight'


# # 10. Самый убыточный фильм за период с 2012 по 2014 г. (включительно)?
# 

# In[39]:


total[(total.release_year >= 2012) & (total.release_year <= 2014)].profit.sort_values()


# In[40]:


total[total.profit == -165710090].original_title


# In[372]:


# в словарь вставляем номер вопроса и ответ на него
answers['10'] = 'The Lone Ranger'


# # 11. Какого жанра фильмов больше всего?

# In[62]:


# эту задачу тоже можно решать разными подходами, попробуй реализовать разные варианты
# если будешь добавлять функцию - выноси ее в предобработку что в начале
total.genres.apply(lambda x: Counter(str(x).split('|'))).sum()


# In[373]:


# в словарь вставляем номер вопроса и ответ на него
answers['11'] = 'Drama'


# # 12. Фильмы какого жанра чаще всего становятся прибыльными? 

# In[302]:


total1 = total[total.profit > 0]
total1.genres.apply(lambda x: Counter(str(x).split('|'))).sum()


# In[374]:


# в словарь вставляем номер вопроса и ответ на него
answers['12'] = 'Drama'


# # 13. У какого режиссера самые большие суммарные кассовые сборы?

# In[305]:


total2 = total
total2['director'] = total.director.apply(lambda x: str(x).split('|'))


# In[306]:


total3 = total2.explode('director')
total3.groupby(['director']).sum()['revenue'].sort_values(ascending = False)


# In[375]:


# в словарь вставляем номер вопроса и ответ на него
answers['13'] = 'Peter Jackson'


# # 14. Какой режисер снял больше всего фильмов в стиле Action?

# In[312]:


total4 = total[total.genres.str.contains('Action')]
pd.Series(total4.director.apply(lambda x: Counter(str(x).split('|'))).sum()).sort_values(ascending = False)


# In[376]:


# в словарь вставляем номер вопроса и ответ на него
answers['14'] = 'Robert Rodriguez'


# # 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году? 

# In[313]:


total5 = total[total.release_year == 2012]
actors = total5.sort_values(['revenue'], ascending = False).head(1).cast.unique()
str(actors).split('|')


# In[377]:


# в словарь вставляем номер вопроса и ответ на него
answers['15'] = 'Chris Hemsworth'


# # 16. Какой актер снялся в большем количестве высокобюджетных фильмов?

# In[314]:


total6 = total[total.budget > total.budget.mean()]
pd.Series(total6.cast.apply(lambda x: Counter(str(x).split('|'))).sum()).sort_values(ascending = False)


# In[378]:


# в словарь вставляем номер вопроса и ответ на него
answers['16'] = 'Matt Damon'


# # 17. В фильмах какого жанра больше всего снимался Nicolas Cage? 

# In[326]:


total7 = total[total.cast.str.contains('Nicolas Cage')]
pd.Series(total7.genres.apply(lambda x: Counter(str(x).split('|'))).sum()).sort_values(ascending = False)


# In[379]:


# в словарь вставляем номер вопроса и ответ на него
answers['17'] = 'Action'


# # 18. Самый убыточный фильм от Paramount Pictures

# In[327]:


total8 = total[total.production_companies.str.contains('Paramount Pictures')]
total8[total8.profit == total8.profit.min()].original_title


# In[380]:


# в словарь вставляем номер вопроса и ответ на него
answers['18'] = 'K-19: The Widowmaker'


# # 19. Какой год стал самым успешным по суммарным кассовым сборам?

# In[110]:


total.groupby(['release_year']).sum()['revenue'].sort_values(ascending = False)


# In[381]:


# в словарь вставляем номер вопроса и ответ на него
answers['19'] = 2015


# # 20. Какой самый прибыльный год для студии Warner Bros?

# In[330]:


total9 = total[total.production_companies.str.contains('Warner Bros')]
total9.groupby(['release_year']).sum()['revenue'].sort_values(ascending = False)


# In[382]:


# в словарь вставляем номер вопроса и ответ на него
answers['20'] = 2014


# # 21. В каком месяце за все годы суммарно вышло больше всего фильмов?

# In[332]:


months = total.release_date.apply(lambda x: str(x)[:x.find('/')]).value_counts().sort_values(ascending = False)
display(months)


# In[383]:


# в словарь вставляем номер вопроса и ответ на него
answers['21'] = 'Сентябрь'


# # 22. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)

# In[334]:


months['6'] + months['7'] + months['8']


# In[384]:


# в словарь вставляем номер вопроса и ответ на него
answers['22'] = 450


# # 23. Для какого режиссера зима – самое продуктивное время года? 

# In[347]:


total10 = total.release_date.apply(lambda x: str(x)[:x.find('/')])
total11 = total[(total10 == '1') | (total10 == '2') | (total10 == '12')]
total12 = total11.explode('director')
total12.director.value_counts().sort_values(ascending = False)


# In[385]:


# в словарь вставляем номер вопроса и ответ на него
answers['23'] = 'Peter Jackson'


# # 24. Какая студия дает самые длинные названия своим фильмам по количеству символов?

# In[351]:


total13 = new_total2
total13['production_companies'] = total13.production_companies.apply(lambda x: str(x).split('|'))


# In[352]:


total14 = total13.explode('production_companies')
total14.groupby(['production_companies']).mean()['len_title'].sort_values(ascending = False)


# In[386]:


# в словарь вставляем номер вопроса и ответ на него
answers['24'] = 'Four By Two Productions'


# # 25. Описание фильмов какой студии в среднем самые длинные по количеству слов?

# In[354]:


total14.groupby(['production_companies']).mean()['len_overview'].sort_values(ascending = False)


# In[387]:


# в словарь вставляем номер вопроса и ответ на него
answers['25'] = 'Midnight Picture Show'


# # 26. Какие фильмы входят в 1 процент лучших по рейтингу? 
# по vote_average

# In[233]:


np.quantile(new_total2['vote_average'], 0.99)


# In[234]:


new_total2[new_total2.vote_average > 7.8]


# In[388]:


# в словарь вставляем номер вопроса и ответ на него
answers['26'] = 'Inside Out, The Dark Knight, 12 Years a Slave'


# # 27. Какие актеры чаще всего снимаются в одном фильме вместе?
# 

# In[292]:


pairs = []
pairs2 = []
actors = pd.Series(new_total2.cast.apply(lambda x: str(x).split('|')))
for i in actors:
    temp = it.combinations(i, 2)
    pairs.append(list(temp))
for i in pairs:
    for idx in i:
        pairs2.append(idx)
q = pd.DataFrame({'actpairs':pairs2})
q.actpairs.value_counts()


# In[389]:


# в словарь вставляем номер вопроса и ответ на него
answers['27'] = 'Daniel Radcliffe & Rupert Grint'


# # Submission

# In[390]:


# в конце можно посмотреть свои ответы к каждому вопросу
answers


# In[391]:


# и убедиться что ни чего не пропустил)
len(answers)

