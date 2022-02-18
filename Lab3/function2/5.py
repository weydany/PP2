from movie_list import movies

def avg_category(a: list, ctgry: str):
    sum = 0
    cnt = 0
    for i in a:
        if i['category'] == ctgry:
            sum += i['imdb']
            cnt += 1
    return sum / cnt

print(avg_category(movies, 'Action'))