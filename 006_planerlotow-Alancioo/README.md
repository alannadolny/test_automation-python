# Planer lotów

| Termin oddania | Punkty     |
|----------------|:-----------|
|    21.01.2022  23:00 |  10         |

--- 
Przekroczenie terminu o **n** zajęć wiąże się z karą:
- punkty uzyskania za realizację zadania są dzielone przez **2<sup>n</sup>**.

--- 
### Zadanie 
Bazując na prezentowanym na wykładzie przykładzie `flight_planner`, 
rozbudować go o następujące funkcjonalności:
- program powinien umożliwiać wybieranie lotów pomiędzy konkretnymi miastami, 
  w konkretnym przedziale czasowym oraz z odpowiednim limitem cenowym
- taka wyszukiwarka powinna posiadać opcje wyszukiwania lotów:
  * najtańszych
  * najszybszych
  * najlepiej dopasowanych do ograniczeń czasowych
- program powinien również uwzględniać nie tylko dostępność samolotu 
	ale także dostępne w samolotach miejsca.
  
Stosując BDD, zdefiniować odpowiednie, *features*, *user stories* i *use cases*.

Następnie zaimplementować testy wykorzystując Pythona i bibliotekę `behave`
opisujące powyższe zachowanie programu.

Zaimplementować (rozwinąć przykład `flight_planner`) tak by spełniał 
wszystkie testy.
