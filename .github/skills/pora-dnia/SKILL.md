---
name: pora-dnia
description: "Zwraca aktualną porę dnia po polsku: noc, rano, południe, popołudnie albo wieczór. Użyj, gdy użytkownik pyta o porę dnia lub chce sklasyfikować godzinę."
argument-hint: "[opcjonalna godzina HH:MM]"
---

# Pora Dnia

Zwróć wyłącznie jedną polską nazwę pory dnia, małymi literami.

## Procedura

1. Jeżeli użytkownik podał godzinę w formacie `HH:MM`, użyj tej godziny. W przeciwnym razie odczytaj aktualną lokalną godzinę systemową, uruchamiając w terminalu `date +%H:%M`. To polecenie działa w dostępnym środowisku `bash`.
2. Przypisz godzinę do zakresu:
   - `noc`: 22:00-05:59
   - `rano`: 06:00-09:59
   - `południe`: 10:00-13:59
   - `popołudnie`: 14:00-17:59
   - `wieczór`: 18:00-21:59
3. Odpowiedz wyłącznie przypisaną nazwą, bez interpunkcji ani wyjaśnień.