import pandas as pd
import matplotlib.pyplot as plt
import requests

API_KEY = '6b5a5ff4a2f5633b40fa28496382cceb'

def get_movie_data():
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=fr-FR&sort_by=popularity.desc'
    response = requests.get(url)
    data = response.json()
    return data['results']

movies = get_movie_data()

df = pd.DataFrame(movies, columns=['title', 'popularity', 'vote_count', 'vote_average'])

print(df.head(10))

plt.figure(figsize=(10, 6))
plt.bar(df['title'].head(10), df['popularity'].head(10))
plt.xticks(rotation=45)
plt.xlabel('Film')
plt.ylabel('Popularité')
plt.title('Top 10 des films les plus populaires')
plt.tight_layout()
plt.show()