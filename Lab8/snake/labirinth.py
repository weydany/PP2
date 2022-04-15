labirinth = [[x, 100] for x in range(100, 501, 20)]
labirinth.extend([x, 500] for x in range(100, 501, 20))

labirinth2 = [[100, y] for y in range(100, 201, 20)]
labirinth2.extend([100, y] for y in range(400, 501, 20))
labirinth2.extend([500, y] for y in range(100, 201, 20))
labirinth2.extend([500, y] for y in range(400, 501, 20))