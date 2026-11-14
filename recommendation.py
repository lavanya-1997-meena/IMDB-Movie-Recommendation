import pandas as pd
import re
from cleaning import cleaned_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load cleaned dataset
df = pd.read_csv(r"F:\IMDb_project5\cleaned_movies.csv")

tfidf_object=TfidfVectorizer(stop_words='english',max_features=10000,ngram_range=(1,2))
tfidf_matrix=tfidf_object.fit_transform(df['combine_text'])
print(tfidf_matrix.shape)
print(tfidf_matrix.toarray())
features=tfidf_object.get_feature_names_out()
print(features)
tfidf_df=pd.DataFrame(tfidf_matrix.toarray(),columns=features)
print(tfidf_df.head())

def recommend_movie(text,k=3):
   # Clean user input
    cleaned_input = cleaned_text(text)
     # Check empty input
    if not cleaned_input:
        return pd.DataFrame()
    # Convert user input into TF-IDF vector
    text_vect=tfidf_object.transform([text])
    #calculate cosine similarity
    movie_similarity=cosine_similarity(text_vect,tfidf_matrix)[0]
    # get top 5 index
    top_indices=movie_similarity.argsort()[-k:][::-1][1:k+1]
    recommendation=[]
    for index in top_indices:
        # put index value and find cosine similarity score
        cscore=movie_similarity[index]
        if cscore<=0:
            continue
        recommendation.append({
            
    "Movie Name": df.iloc[index]["Movie_Title"],
    "Storyline": df.iloc[index]["cleaned_storyline"],
    "Similarity Score": round(float(cscore), 4)
    })
        if len(recommendation)==k:
           break
    return pd.DataFrame(recommendation)


        
    
result=recommend_movie('a fading celebrity takes a blackmarket drug a ...',k=5)
print(result)