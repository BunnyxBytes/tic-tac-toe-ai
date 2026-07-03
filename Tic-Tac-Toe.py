import tkinter as tk
from tkinter import messagebox

#Theme
BG_COLOR = "#0d1117"
GRID_COLOR = "#21262d"
X_COLOR = "#58a6ff"
O_COLOR = "#f78166"
FONT = ("Consolas",32,"bold")


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe AI")
        self.window.geometry("500x600")
        self.window.configure(bg="#0d1117")
        self.window.resizable(False,False)
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()

        self.result_label = tk.Label(
            self.window,
            text="",
            font=("Consolas",24,"bold"),
            fg="yellow",
            bg="#0d1117"
        )
        self.result_label.grid(row=3,column=0,columnspan=3,pady=20)

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                self.window.configure(bg=BG_COLOR)

                btn = tk.Button(
                    self.window,
                    text="",
                    font=("Consolas",32,"bold"),
                    width=4,
                    height=2,
                    bg="#21262d",
                    fg="yellow",
                    relief="ridge",
                    bd=3,
                    command=lambda r=i,c=j: self.human_move(r,c)
                )
                btn.grid(row=i, column=j,padx=4,pady=4)
                self.buttons[i][j] = btn
                

    def check_winner(self, player):
        b = self.board
        for i in range(3):
            if all([b[i][j] == player for j in range(3)]): return True
            if all([b[j][i] == player for j in range(3)]): return True
        if all([b[i][i] == player for i in range(3)]): return True
        if all([b[i][2-i] == player for i in range(3)]): return True
        return False

    def is_full(self):
        return all([self.board[i][j]!= ' ' for i in range(3) for j in range(3)])

    def minimax(self, is_maximizing):
        if self.check_winner('O'): return 1
        if self.check_winner('X'): return -1
        if self.is_full(): return 0

        if is_maximizing:
            best = -float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'O'
                        score = self.minimax(False)
                        self.board[i][j] = ' '
                        best = max(score, best)
            return best
        else:
            best = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'X'
                        score = self.minimax(True)
                        self.board[i][j] = ' '
                        best = min(score, best)
            return best

    def best_move(self):
        best_score = -float('inf')
        move = (-1, -1)
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'
                    score = self.minimax(False)
                    self.board[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        return move

    def human_move(self, r, c):
        if self.board[r][c] == ' ':
            self.board[r][c] = 'X'
            self.buttons[r][c].config(text='X',
                                      fg="#58a6ff",
                                      bg="#21262d",
                                      state="disabled"
                                      )

            if self.check_winner('X'):
                self.result_label.config(text="YOU WON!")
                return
            if self.is_full():
                self.result_label.config(text="DRAW")
                return

            self.ai_move()

    def ai_move(self):
        r, c = self.best_move()
        self.board[r][c] = 'O'
        self.buttons[r][c].config(text='O',
                                  fg="#f78166",
                                  bg="#21262d",
                                  state="disabled"
                                 )

        if self.check_winner('O'):
            self.result_label.config(text="AI WON!")
            return
        elif self.is_full():
            self.result_label.config(text="DRAW")
            return

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()