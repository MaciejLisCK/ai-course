name: shelly-out-terrace-light
description: 'Sterowanie światłem tarasowym. Włączanie, wyłączanie, przełączanie, sprawdzanie stanu, temperatury i mocy'
argument-hint: 'włącz | wyłącz | przełącz | status'
user-invocable: true

# Sterowanie światłem tarasowym

## Kiedy użyć

- Użytkownik prosi o włączenie, wyłączenie lub przełączenie światła na tarasie.
- Użytkownik pyta o aktualny stan światła, pobór mocy, napięcie lub temperaturę urządzenia.

## Dostępne akcje

- `włącz` - ustaw światło w stanie włączonym.
- `wyłącz` - ustaw światło w stanie wyłączonym.
- `przełącz` - odwróć bieżący stan światła.
- `status` - odczytaj stan bez jego zmieniania.

## Procedura

1. Ustal akcję z intencji użytkownika. Gdy prosi o odczyt lub pyta, czy światło działa, użyj `status`.
2. Uruchom [skrypt sterujący](./scripts/control-light.sh) z katalogu głównego workspace:

   ```bash
   bash .github/skills/shelly-out-terrace-light/scripts/control-light.sh włącz
   ```

3. Jeśli akcją było `włącz`, `wyłącz` lub `przełącz`, skrypt zwraca odpowiedź polecenia, a następnie aktualny status. Stan końcowy odczytaj z pola `output` drugiego JSON-a.
4. Przy `status` stan odczytaj z pola `output` jedynego JSON-a.
5. Potwierdź użytkownikowi wynik wyłącznie po udanym zakończeniu skryptu:
   - `output: true` oznacza, że światło jest włączone.
   - `output: false` oznacza, że światło jest wyłączone.
   - Gdy użytkownik pyta o zużycie, podaj `apower` w watach. Dla napięcia podaj `voltage`, a dla temperatury użyj pola temperatury obecnego w odpowiedzi urządzenia, jeśli występuje.

## Błędy

Skrypt wypisuje JSON urządzenia. Dla nieznanej akcji lub nieudanego połączenia kończy się kodem niezerowym. W takim przypadku poinformuj użytkownika, że nie udało się potwierdzić wykonania polecenia, i przekaż zwięzłą przyczynę z wyjścia błędu. Nie zakładaj stanu światła.
