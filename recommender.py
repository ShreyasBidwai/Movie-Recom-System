import pickle
import requests

# Load precomputed data
df = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

import requests

def fetch_movie(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=d4578cd4eea6c727671898e045fc3855&language=en-US"
    response = requests.get(url)
    data = response.json()

    print(f"Data for movie_id {movie_id}: {data}")

    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/original/" + poster_path
    else:
        print(f"No poster_path found for movie_id {movie_id}")
        return "https://via.placeholder.com/300x450?text=No+Image"

def recom(movie):
    index = df[df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movies = []
    recommended_movies_posters = []
    
    for i in distances[1:6]:
        movie_index = i[0]
        tmdb_id = df.iloc[movie_index]['id']  # Get actual TMDb ID from df
        recommended_movies.append(df.iloc[movie_index]['title'])
        recommended_movies_posters.append(fetch_movie(tmdb_id))  # Now passes correct ID
    
    return recommended_movies, recommended_movies_posters



import requests
r = requests.get("https://api.themoviedb.org/3/movie/550?api_key=d4578cd4eea6c727671898e045fc3855")
print(r.status_code)
