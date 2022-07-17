from Entities.xo_game import XOGame

m = int(input('Enter number of players: '))
n = int(input('Enter board size: '))

game = XOGame(n, m)

game.print_board()

while not game.game_over():
    print(f"It is player number {game.get_current_player()}s turn. Please enter a coordinate:")
    x, y = map(int, input().split())
    try:
        game.action(x, y)
    except:
        print("error")
    game.print_board()

print(game.winner())