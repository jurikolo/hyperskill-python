class Painting:
    museum = "Louvre"

    def __init__(self, title, painter, year):
        self.title = title
        self.painter = painter
        self.year = year

    def __str__(self):
        return "{} by {} ({}) hangs in the {}".format(self.title, self.painter, self.year, self.museum)

title = input()
painter = input()
year = input()

my_painting = Painting(title, painter, year)
print(my_painting)
