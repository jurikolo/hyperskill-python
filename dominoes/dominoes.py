import random

class Dominoes:
    # def generate_stock(self):
    #     for x in range(7):
    #         for y in range(7):
    #             self.stock.append([x, y])

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
        # for x in self.computer_dominoes:
        #     if x[0] == x[1]:
        #         if max_computer_item == []:
        #             max_computer_item = x
        #         else:
        #             if x[0] > max_computer_item[0]:
        #                 max_computer_item = x
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

    def set_status(self, status):
        self.status = status

    def is_game_over(self):
        # check if any player is out of dominoes
        if len(self.player_dominoes) == 0 or len(self.computer_dominoes) == 0:
            return True

        # check if all dominoes with particular value are out and corner items are the same
        corner_item = self.snake[0][0]
        cnt = 1
        for item in self.snake:
            if item[0] == corner_item:
                cnt += 1
            if item[1] == corner_item:
                cnt += 1
        if cnt == 8:
            if corner_item == self.snake[len(self.snake) - 1][1]:
                return True
        return False

    def get_winner(self):
        if len(self.player_dominoes) == 0:
            return "player"
        elif len(self.computer_dominoes) == 0:
            return "computer"
        else:
            return "draw"

    def get_out_of_moves(self):
        return self.out_of_moves

    def make_computer_turn(self):
        while True:
            index = random.randint(len(self.computer_dominoes) * -1, len(self.computer_dominoes))
            if self.validate_input(index, self.computer_dominoes) == "valid":
                break
        if index < 0:
            self.snake.insert(0, self.computer_dominoes[abs(index) - 1])
            del self.computer_dominoes[abs(index) - 1]
        elif index > 0:
            self.snake.append(self.computer_dominoes[abs(index) - 1])
            del self.computer_dominoes[abs(index) - 1]
        else:
            if len(self.stock) > 0:
                index = random.randint((len(self.stock) - 1) * -1, len(self.stock) - 1)
                self.computer_dominoes.append(self.stock[index])
                del self.stock[index]
        self.status = "player"

    def make_player_turn(self, index):
        if index < 0:
            if self.player_dominoes[abs(index) - 1][1] == self.snake[0][0]:
                self.snake.insert(0, self.player_dominoes[abs(index) - 1])
            else:
                item = self.flip(self.player_dominoes[abs(index) - 1])
                self.snake.insert(0, item)
            del self.player_dominoes[abs(index) - 1]
        elif index > 0:
            if self.player_dominoes[index - 1][0] == self.snake[0][0]:
                self.snake.append(self.player_dominoes[index - 1])
            else:
                item = self.flip(self.player_dominoes[index - 1])
                self.snake.append(item)
            del self.player_dominoes[index - 1]
        else:
            if len(self.stock) > 0:
                index = random.randint((len(self.stock) - 1) * -1, len(self.stock) - 1)
                self.player_dominoes.append(self.stock[abs(index)])
                del self.stock[abs(index)]
        self.status = "computer"

    def validate_input(self, index_as_string, dominoes_set):
        # index is list index, quite obvious
        # dominoes is a list of dominoes, either player or computer
        result = ""
        try:
            index = int(index_as_string)
        except ValueError:
            return "invalid_input"
        if abs(index) > len(dominoes_set):
            result = "invalid_input"
        elif index < 0:
            if (dominoes_set[abs(index) - 1][0] == self.snake[0][0]) or (dominoes_set[abs(index) - 1][1] == self.snake[0][0]):
                result = "valid"
            else:
                result = "invalid_move"
        elif index > 0:
            if (dominoes_set[index - 1][0] == self.snake[len(self.snake) - 1][1]) or (dominoes_set[index - 1][1] == self.snake[len(self.snake) - 1][1]):
                result = "valid"
            else:
                result = "invalid_move"
        else:
            result = "valid"
        if result == "valid":
            self.out_of_moves = []
        return result

    def flip(self, item):
        result = [item[1], item[0]]
        return result

    def __init__(self):
        self.stock = []
        self.player_dominoes = []
        self.computer_dominoes = []
        self.snake = []
        self.status = ""
        self.out_of_moves = []

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


def snake_to_string(snake):
    snake_as_string = ""
    if len(snake) < 7:
        for piece in snake:
            snake_as_string += str(piece)
    else:
        snake_as_string += str(snake[0])
        snake_as_string += str(snake[1])
        snake_as_string += str(snake[2])
        snake_as_string += str(snake[-3])
        snake_as_string += str(snake[-2])
        snake_as_string += str(snake[-1])
    return snake_as_string

dominoes = Dominoes()
while True:
    print("="*70)
    print("Stock size: {}".format(dominoes.get_stock_size()))
    print("Computer pieces: {}".format(dominoes.get_computer_dominoes_size()))

    print()
    print(snake_to_string(dominoes.get_snake()))
    print()

    print("Your pieces:")
    cnt = 1
    for item in dominoes.get_player_dominoes():
        print("{}:{}".format(cnt, item))
        cnt += 1

    print()
    if dominoes.is_game_over():
        break

    if dominoes.get_status() == "computer":
        print("Status: Computer is about to make a move. Press Enter to continue...")
    else:
        print("Status: It's your turn to make a move. Enter your command.")

    user_input = input()
    while (dominoes.get_status() == "player") and dominoes.validate_input(user_input, dominoes.get_player_dominoes()) not in ["valid"]:
        if (dominoes.validate_input(user_input, dominoes.get_player_dominoes())) == "invalid_input":
            print("Invalid input. Please try again.")
        else:
            print("Illegal move. Please try again.")
        user_input = input()

    if dominoes.get_status() == "computer":
        dominoes.make_computer_turn()
    else:
        dominoes.make_player_turn(int(user_input))

    # Out of stock, draw game
    if dominoes.get_stock_size() == 0:
        break

winner = dominoes.get_winner()
if winner == "player":
    print("Status: The game is over. You won!")
elif winner == "computer":
    print("Status: The game is over. The computer won!")
else:
    print("Status: The game is over. It's a draw!")