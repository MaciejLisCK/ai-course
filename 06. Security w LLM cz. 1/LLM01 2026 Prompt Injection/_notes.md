prompt injection - dane wejściowe trafiające do LLM zmieniają zachowanie modelu w sposób niezamierzony przez twórcę aplikacji

Dane wejściowe to wszystko co może być w context window:
- prompt użytkownika
- skille
- wynik toola
- wynik MCP
- treść strony www
- treść obrazu, dzwięku, wideo
- wynik rozumowania modelu
- trwała pamięć
- itd.

Problem:
LLM nie odróżnia instrukcji od danych, wszystko jest jednym strumieniem tekstu

3