from itertools import count
import string
from tweepyEx import scrape
from textblob import TextBlob
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import re
import nltk

numtweet = 120

data = scrape('#StarWars', '2022-1-01',numtweet)
tweets = list(data['text'])
tweets_ls = pd.DataFrame(tweets)

tweets_ls.drop_duplicates(inplace = True)
tweets_ls['text'] = tweets_ls[0]

# Usar Regex para eliminar RTs y caracteres no importantes a la hora de hacer el estudio (Pre-procesamiento)
remove_rt = lambda x: re.sub('RT @\w+: '," ",x)
rt = lambda x: re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",x)

tweets_ls["text"] = tweets_ls.text.map(remove_rt).map(rt)
tweets_ls["text"] = tweets_ls.text.str.lower()
tweets_ls.head(10)

# Realizar el analisis de sentimientos
tweets_ls[['polarity', 'subjectivity']] = tweets_ls['text'].apply(lambda Text: pd.Series(TextBlob(Text).sentiment))
for index, row in tweets_ls['text'].iteritems():
    score = SentimentIntensityAnalyzer().polarity_scores(row)
    neg = score['neg']
    neu = score['neu']
    pos = score['pos']
    comp = score['compound']
    if neg > pos:
        tweets_ls.loc[index, 'sentiment'] = "negative"
    elif pos > neg:
        tweets_ls.loc[index, 'sentiment'] = "positive"
    else:
        tweets_ls.loc[index, 'sentiment'] = "neutral"
    tweets_ls.loc[index, 'neg'] = neg
    tweets_ls.loc[index, 'neu'] = neu
    tweets_ls.loc[index, 'pos'] = pos
    tweets_ls.loc[index, 'compound'] = comp

tweets_ls.head(10)
print(tweets_ls)

#Crear dataframes aparte por cada uno de los sentimientos, en negativo, positivo, y neutral
tweets_ls_negative = tweets_ls[tweets_ls["sentiment"]=="negative"]
tweets_ls_positive = tweets_ls[tweets_ls["sentiment"]=="positive"]
tweets_ls_neutral = tweets_ls[tweets_ls["sentiment"]=="neutral"]

# Contar los valores negativos, positivos y neutrales para el analisis grafico que se realizara
def countInColumn(data,feature):
    total=data.loc[:,feature].value_counts(dropna=False)
    percentage=round(data.loc[:,feature].value_counts(dropna=False,normalize=True)*100,2)
    return pd.concat([total,percentage],axis=1,keys=['Total','Percentage'])

# Creacion informacion para grafica de torta
pichart = countInColumn(tweets_ls,"sentiment")
names= pichart.index
size=pichart["Percentage"]
print("Cantidad de tweets por cada uno de los sentimientos")
print(countInColumn(tweets_ls,"sentiment"))

# Creacion de la grafica
my_circle=plt.Circle( (0,0), 0.7, color='white')
plt.pie(size, labels=names, colors=['green','blue','red'])
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.show()

tweets_ls['text_len'] = tweets_ls['text'].astype(str).apply(len)
tweets_ls['text_word_count'] = tweets_ls['text'].apply(lambda x: len(str(x).split()))

print("El promedio del tamaño de cada tweet dividido por sentimiento")
print(round(pd.DataFrame(tweets_ls.groupby("sentiment").text_len.mean()),2))

print("El promedio del tamaño de palabras usadas en cada tweet dividido por sentimiento")
print(round(pd.DataFrame(tweets_ls.groupby("sentiment").text_word_count.mean()),2))

# Remover puntuación de cada uno de los tweets
def remove_punct(text):
    text  = "".join([char for char in text if char not in string.punctuation])
    text = re.sub('[0-9]+', '', text)
    return text

tweets_ls['punct'] = tweets_ls['text'].apply(lambda x: remove_punct(x))

# Aplicando tokenizacion (separando cada palabra para obtener un arreglo con estas)
def tokenization(text):
    text = re.split('\W+', text)
    return text

tweets_ls['tokenized'] = tweets_ls['punct'].apply(lambda x: tokenization(x.lower()))

# Aplicando Stemming
ps = nltk.PorterStemmer()

def stemming(text):
    text = [ps.stem(word) for word in text]
    return text

tweets_ls['stemmed'] = tweets_ls['tokenized'].apply(lambda x: stemming(x))

print(tweets_ls['tokenized'])