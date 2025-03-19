# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

movie = []

for x in range(0, 3):
    nameofMovie = input("Please Enter the Name of Your Favorite Movies: ")
    movie.append(nameofMovie)

print(movie)