---
name: shelly-out-terrace-light
description: 'Sterowanie światłem tarasowym. Włączanie, wyłączanie, przełączanie, sprawdzanie stanu, temperatury i mocy'
argument-hint: 'włącz | wyłącz | przełącz | status'
user-invocable: true
---

## Kiedy użyć

- Użytkownik prosi o włączenie, wyłączenie lub przełączenie światła tarasowego.
- Użytkownik pyta, czy światło tarasowe jest włączone, albo prosi o odczyt poboru mocy.

## Konfiguracja urządzenia

- Urządzenie: Shelly Outdoor PlugS Gen3
- Adres: `10.1.0.29`

## Procedura

1. Ustal żądaną akcję: `włącz`, `wyłącz`, `przełącz` lub `status`.
2. Wykonaj pasujące zapytanie HTTP GET za pomocą `curl`:

   ```bash
   # włącz
   curl --fail --silent --show-error 'http://10.1.0.29/rpc/Switch.Set?id=0&on=true'

   # wyłącz
   curl --fail --silent --show-error 'http://10.1.0.29/rpc/Switch.Set?id=0&on=false'

   # przełącz
   curl --fail --silent --show-error 'http://10.1.0.29/rpc/Switch.Toggle?id=0'

   # status
   curl --fail --silent --show-error 'http://10.1.0.29/rpc/Switch.GetStatus?id=0'
   ```

3. Po zmianie stanu odczytaj status przez `Switch.GetStatus?id=0`.
4. Potwierdź wynikowy stan polem `output` z JSON-a. W razie potrzeby podaj `apower` jako aktualną moc czynną w watach.
