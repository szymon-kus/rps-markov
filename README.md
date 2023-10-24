# rps-markov
Simulator of game rock, paper, scissors using Markov Chain. 

Dokumentacja programu "Kamień, Papier, Nożyce" z wykorzystaniem łańcucha Markova

Opis programu
Program "Kamień, Papier, Nożyce" jest prostą symulacją gry, w której użytkownik rywalizuje z komputerem. Program wykorzystuje strategie i macierz przejść, aby nauczyć się najlepszego wyboru na podstawie historii rozgrywki. Po przeprowadzeniu symulacji, użytkownik ma możliwość zmierzenia się z nauczonym komputerem. Po zakończeniu symulacji i rozgrywki z komputerem wyświetlają się wykresy z wynikami gry. 

Opis kodu
1. Importowanie niezbędnych bibliotek:
import numpy as np
import random
import matplotlib.pyplot as plt

2. Inicjalizacja stanów gry i macierzy przejść:
W tym miejscu inicjalizujemy stany gry, czyli możliwe wybory użytkownika i komputera. Definiujemy również macierz przejść.

states = ["Papier", "Kamień", "Nożyce"]
probability = np.full((len(states), len(states)), 1/3)

3. Funkcja `choose_state_on_strategy(strategy)`
Pozwala na wybór stanu gry na podstawie strategii, gdzie `strategy` jest numerem indeksu stanu w macierzy przejść "probability".

4. Funkcja `state_to_name(numer)`
Przekształca numer stanu na jego nazwę - 0 na kamień, 1 na papier, 2 na nożyce

5. Funkcja `game()`
Przeprowadza symulację gry. Wybierane są stany komputera i użytkownika, a następnie określany jest wynik rundy.

6. Funkcja `update_matrix(state, computer_choose, user_choice, score)’
Aktualizuje macierz przejść na podstawie wyniku rundy, zwiększając prawdopodobieństwo wygranej strategii i zmniejszając pozostałe.

7. Funkcja `show_score(score, program_move, user_move)`
Wyświetla wynik rundy.

8. Program pyta użytkownika o liczbę rund gry do przeprowadzenia symulacji.

9. Inicjalizowane są punkty symulacji oraz listy wyników symulacji.

10. Przeprowadzana jest symulacja gry, a wyniki zapisywane są w listach.

11. Następnie program przechodzi do rozgrywki przeciwko nauczonemu komputerowi, gdzie użytkownik ma możliwość wybierania ruchów.

12. Wyniki gry z nauczonym komputerem są zapisywane i wyświetlane na końcu.

13. Program generuje wykres wyników symulacji i gry.

Instrukcje użytkowania:
1. Uruchom program.
2. Podaj liczbę losowych rund, które chcesz przeprowadzić w symulacji.
3. Program przeprowadzi symulację gry pomiędzy komputerem a użytkownikiem.
4. Po zakończeniu symulacji, zostaniesz poproszony o rozegranie gry przeciwko nauczonemu komputerowi.
5. Wybieraj ruchy (0 - Papier, 1 - Kamień, 2 - Nożyce) i obserwuj wyniki gry.
6. Po zakończeniu gry, wyniki symulacji i gry zostaną wyświetlone na wykresie.

Uwagi:
- Program aktualizuje strategie na podstawie wyników symulacji.
- Możesz zakończyć grę przeciwko nauczonymu komputerowi w dowolnym momencie, wpisując "q" podczas wyboru ruchu.
![image](https://github.com/szymon-kus/rps-markov/assets/144013915/a8d44e81-5a2e-421d-bcc3-d8ff90b8bb7b)
