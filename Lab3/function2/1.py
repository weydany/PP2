from movie_list import movies

def check(d: dict):
    if d['imdb'] > 5.5:
        return True
    return False

print( check(movies[0]) )