def add_player(player, team=[]):
    team.append(player)
    return team


def add_player_correct(player, team=None):
    if team is None:
        team = []
    team.append(player)
    return team


def create_url(host="localost", port="443"):
    return f"\"https://{host}:{port}\""


def heading(text, size=1):
    if size < 1:
        size = 1
    elif size > 6:
        size = 6
    return "#" * size + f" {text}"


team1 = add_player("Player1")
print(team1)
team2 = add_player("Player2")
print(team2)
print(team1)
print("=====")
print("=====")
team3 = add_player_correct("Player1")
print(team3)
team4 = add_player_correct("Player2")
print(team4)
print(team3)
print("=====")
print("=====")
print(create_url())
print(create_url(host="example.com", port="8080"))
print("=====")
print("=====")
print(heading("asdf"))
print(heading("asdf", 3))
print(heading("asdf", -1))
