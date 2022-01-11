# * unpacks elements of an iterable object
# ** works with dictionaries

def sum(a, b, *args):
    result = a + b
    for x in args:
        result += x
    return result


def concat(*args, sep=" "):
    return sep.join(args)


def capital(**kwargs):
    for key, value in kwargs.items():
        print(value, "is the capital city of", key)


def say_bye(**names):
    for name in names:
        print("Au revoir,", name)
        print("See you on", names[name]["next appointment"])
        print()

def tracklist(**tracks):
    for track in tracks:
        print(track)
        for a, b in tracks[track].items():
            print(f"ALBUM: {a} TRACK: {b}")


print("hey")
print(*"hey")

print(sum(1, 2, 3, 4, 5))
arr = [3, 4, 5]
print(sum(1, 2, *arr))
# print(sum(1, 2, arr))  # Invalid!

print("======")
print("======")
print(concat("a", "b", "c"))
print("======")
print("======")
capital(Canada="Ottawa", Estonia="Tallinn", Venezuela="Caracas", Finland="Helsinki")
print("======")
print("======")
humans = {"Laura": {"next appointment": "Tuesday"},
          "Robin": {"next appointment": "Friday"}}

say_bye(**humans)

print("======")
print("======")
# task 1
tracklist(Woodkid={"The Golden Age": "Run Boy Run",
                   "On the Other Side": "Samara"},
          Cure={"Disintegration": "Lovesong",
                "Wish": "Friday I'm in love"})