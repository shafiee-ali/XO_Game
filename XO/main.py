from Entities.xo_game import XOGame

game = XOGame(4, 3)

game.print_board()

while not game.is_end_game():
    print(f"It is player number {game.get_current_player()}s turn. Please enter a coordinate:")
    x, y = map(int, input().split())
    try:
        game.action(x, y)
    except:
        print("error")
    game.print_board()
