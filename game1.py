def field_board(field):
  print(f" {field[0]} | {field[1]} | {field[2]} ")
  print("---+---+---")
  print(f" {field[3]} | {field[4]} | {field[5]} ")
  print("---+---+---")
  print(f" {field[6]} | {field[7]} | {field[8]} ")

def player_move(field):
  while True:
    move = input("Введите номер ячейки (1-9): ")
    if move.isdigit() and int(move) in range(1, 10) and field[int(move) - 1] == " ":
      return int(move)
    else:
      print("Неверный ход. Попробуйте снова.")

def win_check(field, symbol):
  combinations = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # горизонтали
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # вертикали
    (0, 4, 8), (2, 4, 6)             # диагонали
  ]

  for combination in combinations:
    if field[combination[0]] == symbol and \
       field[combination[1]] == symbol and \
       field[combination[2]] == symbol:
      return True
  return False

def game():
  field = [" "] * 9
  player = "X"
  move_count = 0

  while True:
    field_board(field)
    move = player_move(field)
    field[move - 1] = player
    move_count += 1

    if win_check(field, player):
      field_board(field)
      print(f"Игрок {player} выиграл!")
      break

    if move_count == 9:
      field_board(field)
      print("Ничья!")
      break

    player = "O" if player == "X" else "X"

if __name__ == "__main__":
    game()