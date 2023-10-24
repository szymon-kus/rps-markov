import numpy as np
import random
import matplotlib.pyplot as plt

# zdefioniowanie stanów gry
states = ["Papier", "Kamień", "Nożyce"]

# inicjalizacja macierzy przejść 
probability = np.full((len(states), len(states)), 1/3)

# funkcja, która umozliwia dokonanie wyboru na podstawie strategii
def choose_state_on_strategy(strategy):
    # strategia jest numerem indeksu stanu w macierzy przejść "probability"
    return np.random.choice(len(states), p=probability[strategy])

# przekształcanie numeru stanu na nazwę stanu (0 -> papier, 1-> kamien, 2->nozyce)
def state_to_name(numer):
    return states[numer]

# symulacja gry
def game():
    # losowy wybór początkowego stanu
    state = random.choice(range(len(states)))
    
    # wybór strategii na podstawie obecnego stanu
    computer_choose = choose_state_on_strategy(state)
    
    # wybor uzytkownika
    user_choice = random.choice(range(len(states)))
    
    # określenie wyniku rundy
    if computer_choose == user_choice:
        score = "Remis"
    elif (computer_choose + 1) % len(states) == user_choice or (computer_choose - 2) % len(states) == user_choice:
        score = "Wygrana komputera"
    else:
        score = "Wygrana użytkownika"
    
    return score, state, computer_choose, user_choice

#  aktualizacja macierzy przejść
def update_matrix(state, computer_choose, user_choice, score):
    # ustalanie, który stan programu wygrał
    if score == "Wygrana programu":
        winner_programe_state = computer_choose
    else:
        winner_programe_state = user_choice
    
    # aktualizacja macierzy przejść na podstawie wyniku
    for i in range(len(states)):
        if i == winner_programe_state:
            probability[state][i] += 0.1  # zwiększamy prawdopodobieństwo wygranej strategii
            if probability[state][i] > 1.0:
                probability[state][i] = 1.0  # ograniczamy wartość do 1
        else:
            probability[state][i] -= 0.05  # zmniejszamy pozostałe prawdopodobieństwa
            if probability[state][i] < 0.0:
                probability[state][i] = 0.0  # ograniczamy wartość do 0
    
    # Normalizacja prawdopodobieństw (suma prawdopodobieństw w każdym wierszu wynosi 1)
    sum_probability = np.sum(probability[state])
    if sum_probability != 0.0:
        probability[state] /= sum_probability

# wyswietlanie wyniku rundy
def show_score(score, program_move, user_move):
    print("Komputer wybrał:", state_to_name(program_move))
    print("Użytkownik wybrał:", state_to_name(user_move))
    print("Wynik rundy:", score)

# Liczba rund gry do symulacji
print("Podaj ilość losowych rund do przeprowadzenia symulacji: ")
num_rounds = int(input())

# Inicjalizacja punktów
simulation_points = {'komputer': 0, 'gracz': 0}

# Listy do przechowywania wyników symulacji
comp_simulation_points = []
user_simulation_points = []

# Powtarzanie symulacji gier
for _ in range(num_rounds):
    wynik_symulacji, state, computer_choose, user_choice = game()
    update_matrix(state, computer_choose, user_choice, wynik_symulacji)
    comp_simulation_points.append(simulation_points['komputer'])
    user_simulation_points.append(simulation_points['gracz'])
    simulation_points['komputer'] += 1 if wynik_symulacji == "Wygrana komputera" else 0
    simulation_points['gracz'] += 1 if wynik_symulacji == "Wygrana użytkownika" else 0

# Rozpoczęcie gry z nauczonym komputerem
game_num_rounds = num_rounds
print("Po " + str(game_num_rounds) + " losowych rundach rozpoczynamy grę z nauczonym komputerem.")

# Inicjalizacja punktów
game_points = {'komputer': 0, 'gracz': 0}

# Lista do przechowywania wyników gry
comp_game_points = []
user_game_points = []

# Inicjalizacja początkowego wyboru użytkownika
user_choice = random.choice(range(len(states)))

# Powtarzanie rund gry przeciwko nauczonemu komputerowi
for _ in range(game_num_rounds):
    # Komputer wybiera strategię na podstawie historii gry użytkownika
    state = user_choice
    computer_choose = choose_state_on_strategy(state)
    
    # Użytkownik dokonuje swojego wyboru
    print("Wybierz swój ruch (0 - Papier, 1 - Kamień, 2 - Nożyce, q - Wyjdź z gry):")
    user_choice = input()
    
    if user_choice == 'q':
        break
    
    if not user_choice.isnumeric():
        print("Niepoprawny wybór. Wybierz 0, 1 lub 2.")
        continue
    
    if int(user_choice) > 2:
        print("Podaj poprawną wartość")
        continue

    user_choice = int(user_choice)
    
    if user_choice < 0 or user_choice > 2:
        print("Niepoprawny wybór. Wybierz 0, 1 lub 2.")
        continue
    
    # Określenie wyniku rundy (wynik gry)
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
    
    # Wyświetlenie wyniku rundy
    show_score(game_results, computer_choose, user_choice)

# Wyświetlanie wyników gry
print("Wyniki gry:")
print("Liczba rund:", len(comp_game_points))
print("Punkty komputera:", game_points['komputer'])
print("Punkty gracza:", game_points['gracz'])

# Wykres wyników symulacji i gry przeciwko nauczonemu komputerowi
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
