import random

players_names = ('John', 'Jack')
human_player = players_names[0]
bot_player = players_names[1]

def main():

    def human_move() -> int:
        while True:
            human_pencils_raw = input()
            if not human_pencils_raw in ('1', '2', '3'):
                print(f"Possible values: '1', '2' or '3'")
            else:
                human_pencils = int(human_pencils_raw)
                if human_pencils > pencils:
                    print('Too many pencils were taken')
                else:
                    break
        return human_pencils

    def bot_move() -> int:
        if pencils in range(5, pencils + 1, 4):  # 5,9,13,17... - bot takes a random number of pencils from 1 to 3
            return random.randint(1, 3)
        elif pencils == 1:  # 1 - bot takes the last pencil and loses
            return 1
        elif pencils in range(4, pencils + 1, 4):  # 4,8,12,16... - bot takes 3 pencils
            return 3
        elif pencils in range(3, pencils + 1, 4):  # 3,7,11,15... - bot takes 2 pencils
            return 2
        elif pencils in range(2, pencils + 1, 4):  # 2,6,10,14... - bot takes 1 pencil
            return 1

    print('How many pencils would you like to use:')
    while True:
        try:
            pencils = int(input(''))
        except ValueError:
            print('The number of pencils should be numeric')
        else:
            if pencils > 0:
                break
            else:
                print('The number of pencils should be positive')

    print(f'Who will be the first ({players_names[0]}, {players_names[1]}):')
    while True:
        name = input('')
        if name in players_names:
            current_player = name
            break
        else:
            print(f"Choose between '{players_names[0]}' and '{players_names[1]}'")

    while True:  # main game loop
        print('|' * pencils)
        print(f"{current_player}'s turn:")

        if current_player == bot_player:
            bot_pencils = bot_move()
            print(bot_pencils)
            pencils -= bot_pencils
        else:
            pencils -= human_move()

        if current_player == players_names[0]:
            current_player = players_names[1]
        elif current_player == players_names[1]:
            current_player = players_names[0]

        if pencils == 0:
            print(f'{current_player} won!')
            return


if __name__ == '__main__':
    main()
