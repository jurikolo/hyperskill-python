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
            self.domino_snake.append(self.computer_dominoes[max_computer_index])
            del self.computer_dominoes[max_computer_index]
            self.status = "computer"
        elif (max_computer_index == None) and (max_player_index != None):
            self.domino_snake.append(self.player_dominoes[max_player_index])
            del self.player_dominoes[max_player_index]
            self.status = "player"
        elif self.computer_dominoes[max_computer_index][0] > self.player_dominoes[max_player_index][0]:
            self.domino_snake.append(self.computer_dominoes[max_computer_index])
            del self.computer_dominoes[max_computer_index]
            self.status = "computer"
        else:
            self.domino_snake.append(self.player_dominoes[max_player_index])
            del self.player_dominoes[max_player_index]
            self.status = "player"

    def __init__(self):
        self.stock = []
        self.player_dominoes = []
        self.computer_dominoes = []
        self.domino_snake = []
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

        print("Stock pieces:", self.stock)
        print("Computer pieces:", self.computer_dominoes)
        print("Player pieces:", self.player_dominoes)
        print("Domino snake:", self.domino_snake)
        print("Status:", self.status)

dominoes = Dominoes()