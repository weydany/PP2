from movie_list import movies

def avg_imdb(a: list):
    sum = 0
    for i in a:
        sum += i['imdb']
    return sum / len(a)

print(avg_imdb(movies))