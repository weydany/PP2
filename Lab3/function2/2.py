from movie_list import movies

def movies_55(a: list):
    ans = []
    for i in a:
        if i['imdb'] > 5.5:
            ans.append(i)

    return ans

print(movies_55(movies))