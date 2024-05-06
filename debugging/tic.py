#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Vérifier les lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérifier les colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérifier la diagonale principale
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    # Vérifier la diagonale secondaire
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_valid_move(row, col):
    # Vérifier que les coordonnées sont entre 0 et 2
    return 0 <= row <= 2 and 0 <= col <= 2

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))

            if not is_valid_move(row, col):
                print("Invalid input. Please enter numbers between 0 and 2.")
                continue  # Demander de nouveau à l'utilisateur

            if board[row][col] == " ":
                board[row][col] = player

                if check_winner(board):
                    # Afficher le plateau final et annoncer le gagnant (c'est le joueur courant)
                    print_board(board)
                    print("Player " + player + " wins!")
                    break

                # Changer de joueur
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")

        except ValueError:
            # Gérer les cas où l'utilisateur entre des valeurs invalides
            print("Invalid input. Please enter valid numbers.")

tic_tac_toe()