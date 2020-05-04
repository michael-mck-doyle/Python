'''
CLASSES AND INHERITANCE
=======================

1) Define an empty Movie class.

2) Add a dunder init method that takes two arguments "year" and "title"

3) Create a sub-class called "RomCom" that inherits from the Movie class

4) Create another sub-class of the Movie class called "ActionMovie"
    that overwrites the dunder init method of Movie and adds another
    instance variable called "pg" that is set by default to the number 13.

5) EXTRA: If you finish early, use the time to practice flushing out these
    classes and white-boarding code. What attributes could a Movie class
    contain? What methods? What tricks can you use through inheritance?
    Any class attributes you could add?

'''


class Movie(object):
    """
    database of movies
    """
    Screenings = 0
    Movies = 0
    Reviews = 0

    newer = []
    older = []

    def __init__(self, year, title):
        self.year = year
        self.title = title
        Movie.Movies += 1

    def movie_age(self, year):
        if int(year) < 2000:
            Movie.older.append()
        else:
            Movie.newer.append()

    for m in older:
        print(m)
    for m in newer:
        print(m)


class Romcom(Movie):

    """
    database of RomCom movies
    """

    def __repr__(self):
        return f"{self.year}, {self.title}"


class ActionMovie(Movie):
    """
    database of Action movies
    """


    def __init__(self, year, title, pg=13):
        super().__init__(year, title)
        self.pg = pg

    def __repr__(self):
        return f"{self.year}, {self.title}, {self.pg}"


Run = ActionMovie(2018, "Run", 13)
print(Run)
print(Movie.Movies)
Jewelable = Romcom(2019, "Jewelable")
print(Jewelable)
print(Movie.Movies)
Gremlins = Movie(1980, "Gremlins")
print(Gremlins)

print(Movie.newer[0:])
print(Movie.older[0:])





