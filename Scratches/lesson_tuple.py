# task 1, create a tuple from list (see comma at the end)
singleton = ([0, 1, 1, 2, 3, 5, 8, 13, 21],)

# task 2, see that tuple is immutable
# ex-capitals
capitals = ['Philadelphia', 'Rio de Janeiro', 'Saint Petersburg']

capitals[0] = 'Washington, D.C.'
capitals[1] = 'Brasília'
capitals[2] = 'Moscow'
print(capitals)  # ['Washington, D.C.', 'Brasília', 'Moscow']

former_capitals = tuple(capitals)
former_capitals[0] = 'Washington, D.C.'  # TypeError