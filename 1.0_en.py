import random, os, json

"""
EVEN THOUGH THIS GAME IS OPEN-SOURCE, DO NOT EDIT THE GAME'S CODE
IT MAY CAUSE UNEXPECTED ERRORS!
"""

print('You have 100 Russian roubles. You are going to invest.')
print('Welcome to \033[3mINVESTER: AMPLIFIED (v1.0)\033[0m!')

def action():
    print('')
    command = None
    command = input('Enter a command, such as "START" to start the game, "STORY" to view the story or "?" to see the list of commands: ')
    if command.casefold() == 'start': play()
    elif command.casefold() == 'story': print('''
You are the investor of those 3 companies:
    - \033[38;2;63;72;204mA\033[0m company: Stands for \033[38;2;63;72;204;4mA\033[38;2;63;72;204mđù\033[0m (Vietnamese:~ Damn). Low profits and losses, less losses than profits;
    - \033[38;2;163;73;164mB\033[0m company: Stands for, uhh... \033[38;2;163;73;164;4mT\033[38;2;163;73;164mhanh \033[38;2;163;73;164;4mB\033[38;2;163;73;164mình\033[0m, I guess? Yep, \033[38;2;163;73;164;4mT\033[38;2;163;73;164mhanh \033[38;2;163;73;164;4mB\033[38;2;163;73;164mình\033[0m. "Trung bình" (Vietnamese: medium) profits and losses;
    - \033[38;2;136;0;21mC\033[0m company: Stands for \033[38;2;136;0;21;4mC\033[38;2;136;0;21moin \033[38;2;136;0;21;4mC\033[38;2;136;0;21mard\033[0m (based on a Vietnamese joke). Profits will make you rich, otherwise you are bankrupt. Less profits than losses, unfortunately. Perhaps they use your money to gamble.
Profits and losses of companies will affect your money and how much money will you gain/lose depends on how much money you invest in companies.
The best of luck with your 100 Russian roubles!''')
    elif command.casefold() == 'help' or command.casefold() == '?' : print('''
ABOUTME/ABOUTUS     Displays information about me — creator of this game
ABOUTUPDATE         Displays information about the update version
CREDITS             Displays information about the game's publisher
CWD                 Displays the current working directory
HELP/?              Displays the list of commands you can use at the action area
READ                Reads a .json file contains a game's data
START               Starts the game
STORY               Tells the story of the game
UPDATE              Finds and change the game's update version (requires requests module)''')
    elif command.casefold() == 'cwd': print(f'''
Current working directory: {os.getcwd()}. This is where game's data files will be saved if you choose to save them.''')
    elif command.casefold() == 'read': read()
    elif command.casefold() == 'aboutme' or command.casefold() == 'aboutus': print('''
My name is Thiện, you can call me ThienFakeVN or ThieenjVN.
I am the only one who created this game. This game is also the first game I have ever created.
My games are free-to-play and open-source. They use the Terminal screen and are written in Python. Their content is both simple and complicated, based on what I am thinking about.
My GitHub account for anyone needs it: ThienFakeVN.''')
    elif command.casefold() == 'credits' or command.casefold() == 'credit': print('''
\033[1mCREDITS — \033[3mINVESTER: AMPLIFIED (v1.0)\033[0m
\033[3mINVESTER: AMPLIFIED\033[0m is the remake version of \033[3mINVESTER\033[0m. This game is free-to-play and open-source.
PUBLISHER          ThienFakeVN
GAME'S CONTENT     ThienFakeVN
CODE WRITER        ThienFakeVN

\033[1mSPECIAL THANKS\033[0m
Central Bank of the Russian Federation (issuing Russian rouble, if you don't know, it is used in this game)
Visual Studio Code (my programming software)
w3schools.com (the first place I started learning programming)
A student named Thanh Bình who goes to the same school with me (\033[38;2;163;73;164mB\033[0m company stands for \033[38;2;163;73;164;4mT\033[38;2;163;73;164mhanh \033[38;2;163;73;164;4mB\033[38;2;163;73;164mình\033[0m, doesn't it?)
The black-and-white Terminal screen (default screen of programming files)
Python programming language (used to program this game)
And of course, you (who are playing this game)''')
    elif command.casefold() == 'aboutupdate': print('''
\033[3mINVESTER: AMPLIFIED (v1.0)\033[0m is the first version of \033[3mINVESTER: AMPLIFIED\033[0m. This update introduces these content:
    - Player is a investor 3 companies: \033[38;2;63;72;204mA\033[0m, \033[38;2;163;73;164mB\033[0m và \033[38;2;136;0;21mC\033[0m. The player has 100 roubles to invest in these companies;
    - The action area can run these commands : ABOUTME, ABOUTUS, ABOUTUPDATE, CREDITS, CWD, HELP, READ, START, STORY, UPDATE ,?;
    - ...''')
    elif command.casefold() == 'update': update()
    else: print('Invaild command, enter "?" to see the list of commands.')
    action()

def play(): 
    global money, game_seed, data_game, turns, A, B, C
    game_seed = input('Choose a seed (leave this empty to have a random seed): ')
    if game_seed == '': game_seed = random.random()
    random.seed(game_seed)
    data_game = {'game':'invester', 'version': '1.0', 'seed': game_seed}
    money = 100
    turns = 1
    while turns >= 0:
        print('')
        print(f'Turn {turns}')
        money_input()
        print('')
        A *= random.randint(-2, 5)
        B *= random.randint(-10, 10)
        C *= random.randint(-69, 50)
        money = money_remains + A + B + C
        print(f'''Received money from \033[38;2;63;72;204mA\033[0m company: {A};
Received money from \033[38;2;163;73;164mB\033[0m company: {B};
Received money from \033[38;2;136;0;21mC\033[0m company: {C};
Total money after turn {turns}: {money}.''')
        data_game[f'turn {turns}'].update({'collected A': f'{A}', 'collected B': f'{B}', 'collected C': f'{C}', 'money collected': f'{money}'})
        if money <= 0: game_over()
        turns += 1

def money_input():
    global money, data_game, A, B, C, money_remains
    try: A, B, C = int(input('Choose the amount of money to invest in \033[38;2;63;72;204mA\033[0m company: ')), int(input('Choose the amount of money to invest in \033[38;2;63;72;204mB\033[0m company: ')), int(input('Choose the amount of money to invest in \033[38;2;63;72;204mC\033[0m company: '))
    except ValueError:
        print('Error: Please enter a integer.')
        money_input()
    if A < 0 or B < 0 or C < 0:
        print('Error: Cannot enter a negative number.')
        money_input()
    if A > money or B > money or C > money or A + B > money or B + C > money or A + C > money or A + B + C > money:
        print('Error: The amount of money you chose cannot be more than the amount you have.')
        money_input()
    if A + B + C < money:
        money_remains = money - (A + B + C)
        print(f'You invested {A + B + C} roubles, {money_remains} roubles remained.')
    if A + B + C == money:
        money_remains = 0
        print('You invested all of your money.')
    data_game.update({f'turn {turns}': {'chosen A': f'{A}', 'chosen B': f'{B}', 'chosen C': f'{C}'}})

def game_over():
    random.seed(None)
    print('')
    print('You ran out of money! THe game is over!')
    print(f'Before you go, the seed of this game was {game_seed}.')
    command = input(f'''And you can save this game's data into a .json file by enter "SAVE": ''')
    if command.casefold() == 'save':
        game_code = random.randint(1, 999999999999999999999999)
        with open(f'invested{game_code}.json', 'w', encoding='utf-8') as invested:
            json.dump(data_game, invested, indent = 4)
        print(f'Finished! File location: {os.getcwd()}\\invested{game_code}.json')
    action()

def read():
    print('')
    saved_data_location = input("Enter the .json file's location: ")
    try: 
        with open(saved_data_location, 'r', encoding='utf-8') as saved_data_file:
            saved_data = json.load(saved_data_file)
    except FileNotFoundError:
        print('Error: No file was found in this location.')
        action()
    try:
        if saved_data['game'] == 'invester':
            print(f'''
Version: {saved_data['version']}
Seed: {saved_data['seed']}''')
            turns = 1
            while turns:
                print(f'''
Turn {turns}:
    - A: {saved_data[f'turn {turns}']['chosen A']} => {saved_data[f'turn {turns}']['collected A']};
    - B: {saved_data[f'turn {turns}']['chosen B']} => {saved_data[f'turn {turns}']['collected B']};
    - C: {saved_data[f'turn {turns}']['chosen C']} => {saved_data[f'turn {turns}']['collected C']};
    - Total: {saved_data[f'turn {turns}']['money collected']}.''')
                turns += 1
                if int(saved_data[f'turn {turns - 1}']['money collected']) < 0: action()
    except KeyError:
        print('')
        print("Error: This file does not contain any game's data.")
        action()

def update():
    try: import requests
    except ModuleNotFoundError:
        print('Error: requests module was not found. Please make sure that you have downloaded this module.')
        action()
    print('')
    updates = requests.get('https://raw.githubusercontent.com/ThienFakeVN/ThienFakeVN/refs/heads/invester/updates.py')
    environment = {}
    exec(updates.content, environment)
    chosen_update = input('Choose the update version you want to play: ')
    for update in environment['updates']:
        if update == chosen_update:
            print('The update was found!')
            command = input('Enter "UPDATE" to update: ')
            if command.casefold() == 'update':
                file_path = os.path.abspath(__file__)
                update_content = requests.get(f'https://raw.githubusercontent.com/ThienFakeVN/ThienFakeVN/refs/heads/invester/{chosen_update}_en.py')
                with open(file_path, 'wb') as rewrite:
                    rewrite.write(update_content.content)
                    exit()
            else: action()
        print('No update version was found.')
    action()

print('''
(Call this place action area, where you can run commands)''')
action()