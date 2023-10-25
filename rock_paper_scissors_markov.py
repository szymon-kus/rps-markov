import numpy as np
import random
import matplotlib.pyplot as plt

states = ["Papier", "Kamień", "Nożyce"]

probability = np.full((len(states), len(states)), 1/3)

def choose_state_on_strategy(strategy):
    return np.random.choice(len(states), p=probability[strategy])

def state_to_name(number):
    return states[number]

def game():
    state = random.choice(range(len(states)))
    computer_choose = choose_state_on_strategy(state)
    return state, computer_choose

def update_matrix(state, computer_choose, user_choice, score):
    if score == "Wygrana komputera":
        winner_program_state = computer_choose
    else:
        winner_program_state = user_choice
    
    for i in range(len(states)):
        if i == winner_program_state:
            probability[state][i] += 0.1  
            if probability[state][i] > 1.0:
                probability[state][i] = 1.0  
        else:
            probability[state][i] -= 0.05  
            if probability[state][i] < 0.0:
                probability[state][i] = 0.0 
    
    sum_probability = np.sum(probability[state])
    if sum_probability != 0.0:
        probability[state] /= sum_probability

def show_score(score, program_move, user_move):
    print("Komputer wybrał:", state_to_name(program_move))
    print("Użytkownik wybrał:", state_to_name(user_move))
    print("Wynik rundy:", score)

while True:
    try:
        num_rounds = int(input("Podaj ilość losowych rund do przeprowadzenia symulacji: "))
        if num_rounds > 0:
            break
        else:
            print("Podaj dodatnią liczbę rund.")
    except ValueError:
        print("Niepoprawny format. Podaj liczbę rund.")

simulation_points = {'komputer': 0, 'gracz': 0}

comp_simulation_points = []
user_simulation_points = []

for _ in range(num_rounds):
    state, computer_choose = game()
    user_choice = random.choice(range(len(states)))
    score = "Wygrana komputera" if computer_choose == user_choice else "Wygrana użytkownika" if (computer_choose + 1) % len(states) == user_choice or (computer_choose - 2) % len(states) == user_choice else "Remis"
    
    update_matrix(state, computer_choose, user_choice, score)
    comp_simulation_points.append(simulation_points['komputer'])
    user_simulation_points.append(simulation_points['gracz'])
    simulation_points['komputer'] += 1 if score == "Wygrana komputera" else 0
    simulation_points['gracz'] += 1 if score == "Wygrana użytkownika" else 0

game_num_rounds = num_rounds
print("Po " + str(game_num_rounds) + " losowych rundach rozpoczynamy grę z nauczonym komputerem.")

game_points = {'komputer': 0, 'gracz': 0}

comp_game_points = []
user_game_points = []

user_choice = random.choice(range(len(states)))

for _ in range(game_num_rounds):
    state = user_choice
    computer_choose = choose_state_on_strategy(state)
    
    while True:
        user_input = input("Wybierz swój ruch (0 - Papier, 1 - Kamień, 2 - Nożyce, q - Wyjdź z gry): ")
        
        if user_input == 'q':
            break
        
        try:
            user_choice = int(user_input)
            if user_choice not in [0, 1, 2]:
                print("Niepoprawny wybór. Wybierz 0, 1 lub 2.")
            else:
                if computer_choose == user_choice:
                    game_results = "Remis"
                elif (computer_choose + 1) % len(states) == user_choice or (computer_choose - 2) % len(states) == user_choice:
                    game_results = "Wygrana komputera"
                    game_points['komputer'] += 1
                else:
                    game_results = "Wygrana użytkownika"
                    game_points['gracz'] += 1
                
                comp_game_points.append(game_points['komputer'])
                user_game_points.append(game_points['gracz'])
                
                show_score(game_results, computer_choose, user_choice)
                break
        
        except ValueError:
            print("Niepoprawny wybór. Wybierz 0, 1 lub 2.")
    
    if user_input == 'q':
        break
    
print("Wyniki gry:")
print("Liczba rund:", len(comp_game_points))
print("Punkty komputera:", game_points['komputer'])
print("Punkty gracza:", game_points['gracz'])

num_simulation_rounds = len(comp_simulation_points)
plt.figure(figsize=(10, 6))
plt.plot(range(num_simulation_rounds), comp_simulation_points, label='Wyniki Komputera (Symulacja)')
plt.plot(range(num_simulation_rounds), user_simulation_points, label='Wyniki Użytkownika (Symulacja)')
plt.plot(range(num_simulation_rounds, num_simulation_rounds + len(comp_game_points)), comp_game_points, label='Wyniki Komputera (Gra)')
plt.plot(range(num_simulation_rounds, num_simulation_rounds + len(user_game_points)), user_game_points, label='Wyniki Użytkownika (Gra)')
plt.xlabel('Liczba rund')
plt.ylabel('Punkty')
plt.legend()
plt.title('Wyniki gry "Kamień, Papier, Nożyce" - Komputer vs. Użytkownik')
plt.show()
