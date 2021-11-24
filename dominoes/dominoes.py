import random

class Dominoes:
    def generate_stock(self):
        for x in range(7):
            for y in range(x, 7):
                self.stock.append([x, y])

    def get_piece_id_from_stock(self):
        return random.randint(0, len(self.stock) - 1)

    def initialize_snake(self):
        max_player_index = None
        max_computer_index = None
        for x in range(7):
            if self.player_dominoes[x][0] == self.player_dominoes[x][1]:
                if max_player_index == None:
                    max_player_index = x
                else:
                    if self.player_dominoes[x][0] > self.player_dominoes[max_player_index][0]:
                        max_player_index = x
        for x in range(7):
            if self.computer_dominoes[x][0] == self.computer_dominoes[x][1]:
                if max_computer_index == None:
                    max_computer_index = x
                else:
                    if self.computer_dominoes[x][0] > self.computer_dominoes[max_computer_index][0]:
                        max_computer_index = x

        if (max_computer_index == None) and (max_player_index == None):
            self.status = "computer"
        elif (max_computer_index != None) and (max_player_index == None):
            self.snake.append(self.computer_dominoes[max_computer_index])
            del self.computer_dominoes[max_computer_index]
            self.status = "player"
        elif (max_computer_index == None) and (max_player_index != None):
            self.snake.append(self.player_dominoes[max_player_index])
            del self.player_dominoes[max_player_index]
            self.status = "computer"
        elif self.computer_dominoes[max_computer_index][0] > self.player_dominoes[max_player_index][0]:
            self.snake.append(self.computer_dominoes[max_computer_index])
            del self.computer_dominoes[max_computer_index]
            self.status = "player"
        else:
            self.snake.append(self.player_dominoes[max_player_index])
            del self.player_dominoes[max_player_index]
            self.status = "computer"

    def get_stock_size(self):
        return len(self.stock)

    def get_computer_dominoes_size(self):
        return len(self.computer_dominoes)

    def get_snake(self):
        return self.snake

    def get_player_dominoes(self):
        return self.player_dominoes

    def get_status(self):
        return self.status

    def __init__(self):
        self.stock = []
        self.player_dominoes = []
        self.computer_dominoes = []
        self.snake = []
        self.status = ""

        self.generate_stock()

        for x in range(7):
            piece_id = self.get_piece_id_from_stock()
            self.player_dominoes.append(self.stock[piece_id])
            del self.stock[piece_id]
        for x in range(7):
            piece_id = self.get_piece_id_from_stock()
            self.computer_dominoes.append(self.stock[piece_id])
            del self.stock[piece_id]

        self.initialize_snake()

print("="*70)
dominoes = Dominoes()
print("Stock size: {}".format(dominoes.get_stock_size()))
print("Computer pieces: {}\n".format(dominoes.get_computer_dominoes_size()))
print(dominoes.get_snake()[0])
print("\nYour pieces:")
cnt = 1
for item in dominoes.get_player_dominoes():
    print("{}:{}".format(cnt, item))
    cnt += 1

print()
if dominoes.get_status() == "computer":
    print("Status: Computer is about to make a move. Press Enter to continue...")
else:
    print("Status: It's your turn to make a move. Enter your command.")