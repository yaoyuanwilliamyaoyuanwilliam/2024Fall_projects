import matplotlib.pyplot as plt
import matplotlib.patches as patches


class HexOthelloVisualizer:
    def __init__(self, size=5):
        self.size = size  
        self.board = {}
        self.players = ["B", "W", "R"]  
        self.current_player = 0  
        self.init_board()

    def init_board(self):
        for q in range(-self.size, self.size + 2):
            for r in range(-self.size-1, self.size + 1):
                if -q - r in range(-self.size-1, self.size + 1):
                    self.board[(q, r)] = "."  

        self.board[(0, 0)], self.board[(-1, 2)], self.board[(0, -1)] = "B", "B" , "B"  # black
        self.board[(1, 0)], self.board[(0, 1)], self.board[(3, -1)] = "R", "R", "R"  # red
        self.board[(1, -1)], self.board[(2, -1)], self.board[(0, -2)] = "W", "W", "W"  # white


    def draw_hexagon(self, ax, x, y, color):
        hexagon = patches.RegularPolygon(
            (x, y), numVertices=6, radius=0.5, orientation=0,
            edgecolor="black", facecolor=color
        )
        ax.add_patch(hexagon)

    def get_color(self, value):
        if value == "B":
            return "black"  
        elif value == "W":
            return "white"
        elif value == "R":
            return "red"  
        return "lightgray"  # empty

    def render_board(self):
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_aspect('equal')
        ax.set_xlim(-self.size - 1, self.size + 2)
        ax.set_ylim(-self.size - 1, self.size + 1)
        ax.axis('off')

        for (q, r), value in self.board.items():
            x = q + r / 2
            y = r * (3**0.5) / 2
            color = self.get_color(value)
            self.draw_hexagon(ax, x, y, color)

        plt.show()

    def is_valid_move(self, position, player):
        if self.board.get(position, ".") != ".":
            return False  

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1)] 
        potential_flips = [] 
        for dq, dr in directions:
            q, r = position
            found_opponent = False
            current_path = []
            while True:
                q += dq
                r += dr
                if (q, r) not in self.board or self.board[(q, r)] == ".":
                    break  
                if self.board[(q, r)] == player:
                    if found_opponent:
                        potential_flips.extend(current_path)  
                    break
                else:
                    found_opponent = True 
                    current_path.append((q, r))

        if not potential_flips:
            return False

        simulated_board = self.board.copy()
        simulated_board[position] = player
        for q, r in potential_flips:
            simulated_board[(q, r)] = player

        counts = {p: 0 for p in self.players}
        for value in simulated_board.values():
            if value in counts:
                counts[value] += 1

        for p in self.players:
            if counts[p] == 0:
                return False 

        return True 



    def make_move(self, position):
        player = self.players[self.current_player]
        if not self.is_valid_move(position, player):
            print("Invalid move!")
            return False
        self.board[position] = player
        self.flip_pieces(position, player)
        self.current_player = (self.current_player + 1) % len(self.players)
        return True
    

    def flip_pieces(self, position, player):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1)]  
        to_flip = [] 

        for dq, dr in directions:
            current_path = [] 
            q, r = position
            while True:
                q += dq
                r += dr
                if (q, r) not in self.board or self.board[(q, r)] == ".":
                    break
                if self.board[(q, r)] == player:
                    to_flip.extend(current_path)
                    break
                else:
                    current_path.append((q, r))

        for q, r in to_flip:
            self.board[(q, r)] = player


    def is_game_over(self):
        if all(value != "." for value in self.board.values()):
            return True  
        
        # if any player has valid moves, then the game goes on
        for player in self.players:
            if self.get_valid_moves(player):  
                return False  

        return True
    
    def get_scores(self):
        scores = {player: 0 for player in self.players}
        for value in self.board.values():
            if value in scores:
                scores[value] += 1
        return scores

    
    def get_valid_moves(self, player):
        valid_moves = []
        for position in self.board.keys():
            if self.is_valid_move(position, player):
                valid_moves.append(position)
        return valid_moves


    def play(self):
        while not self.is_game_over():
            self.render_board()
            current_player = self.players[self.current_player]
            valid_moves = self.get_valid_moves(current_player)

            # if no valid move, skip
            if not valid_moves:
                print(f"Player {current_player} has no valid moves and skips this turn.")
                self.current_player = (self.current_player + 1) % len(self.players)
                continue

            print(f"Player {current_player}'s turn")
            print("Available moves:", valid_moves)

            try:
                q, r = map(int, input("Enter your move (q r): ").split())
            except ValueError:
                print("Invalid input! Please enter two integers separated by a space.")
                continue

            if (q, r) not in valid_moves:
                print("Invalid move! Try again.")
                continue

            self.make_move((q, r))

        # game over
        print("Game over!")
        scores = self.get_scores()
        print("Final scores:", scores)
        winner = max(scores, key=scores.get)
        print(f"The winner is Player {winner}!")
        self.render_board()





if __name__ == "__main__":
    O = HexOthelloVisualizer(size=3)  
    O.play()
