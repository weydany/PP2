from movie_list import movies

def category(a: list, ctgry: str):
    ans = []
    for i in a:
        if i['category'] == ctgry:
            ans.append(i)

    return ans

print(category(movies, 'Action'))