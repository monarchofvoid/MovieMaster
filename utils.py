# utils.py

def display_movies(movies):
    if not movies:
        print("No movies found.")
    else:
        for movie in movies:
            print(f"ID: {movie[0]}, Title: {movie[1]}, Genre: {movie[2]}, Year: {movie[3]}")

def input_with_prompt(prompt, default=None):
    value = input(prompt)
    return value if value else default
