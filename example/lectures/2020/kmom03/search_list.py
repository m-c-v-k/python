movies = [
    "Spider-Man: Far From Home",
    "Dora and the Lost City of Gold",
    "John Wick: Chapter 3 - Parabellum",
    "Zombieland: Double Tap",
    "Captain Marvel",
    "Star Wars: The Rise of Skywalker"
]
movie = input("Enter movie: ")
# found = False
# for list_movie in movies:
#     if movie == list_movie:
#         print("Movie already exist!")
#         found = True
#         break

# if movie in movies:
#     print("Movie already exist!")
# else:
#     movies.append(movie)

try:
    movies.index(movie)
    print("Movie already exist!")
except ValueError:
    movies.append(movie)
print(movies)
