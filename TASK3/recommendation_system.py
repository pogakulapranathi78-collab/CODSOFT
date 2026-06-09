import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset
movies = {
    "Movie": [
        "Avengers",
        "Iron Man",
        "Captain America",
        "Batman",
        "Superman",
        "Spider-Man"
    ],
    "Action": [1, 1, 1, 1, 1, 1],
    "SciFi": [1, 1, 0, 0, 0, 1],
    "Adventure": [1, 0, 1, 0, 0, 1]
}

df = pd.DataFrame(movies)

features = df[["Action", "SciFi", "Adventure"]]

similarity = cosine_similarity(features)

movie_name = input("Enter a movie name: ")

if movie_name in df["Movie"].values:
    
    index = df[df["Movie"] == movie_name].index[0]

    scores = list(enumerate(similarity[index]))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("\nRecommended Movies:\n")

    count = 0

    for movie in scores[1:]:
        print(df.iloc[movie[0]]["Movie"])
        count += 1

        if count == 3:
            break

else:
    print("Movie not found.")