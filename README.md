
# Find alcohols by url



## etapy



## 1. Zapytanie

Stworzenie request.py odpowiadającego za wysyłanie zapytań oraz zapisywanie wyników do pliku

## 2. Baza alkoholi

Znalezienie bazy alkoholi oraz opracowanie pre_process_data_1.py, a następnie pre_process_data_2.py odpowiedzialnych za obróbkę danych

## 3. Wyniki

Przeprowadzono kilka prób dla różnych konfiguracji
Najlepsze rezultaty uzyskano dla zapytań, w których:

 - 
- jako wymagany brand alkoholu,
- jako opcjonalne nazwę alkoholu
- jako opcjonalne kategorie alkoholi: beer, wine, cider, mead, sake, gin, brandy, whiskey, rum, tequila, vodka, absinthe

Dla najlepszej próby uzyskano 113 wyników.

Dla najlepszej próby parametr optionalTreshold wynosił :
1 dla marek z kategorią alkoholu "other",
2 dla marek z przypisaną kategorią alkoholu

Wszystkie wyniki dla najlepszej próby wydają się być prawidłowe.

Możliwe dalsze ulepszenia skryptu: