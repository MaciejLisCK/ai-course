kroki do LLM:
1. regresja liniowa => dopasowanie prostej do danych
2. regresja logistyczna => rozdzielenie 2 klas prostą
3. sieć neuronowa => rozdzielenie 2 klas krzywą
4. sieć neuronowa + softmax =>  rozdzielenie wielu klas krzywymi
5. sieć neuronowa + softmax + 3d(polprzezroczyste obzszary kolorowe) => skala (https://claude.ai/artifact/HcHfbjJgQwxxUTGZaRQKBJ)

999. sieć neuronowa (x1^2, x2^2, x1*x2) - kernel trick


Każdy krok usuwa jedno ograniczenie.
regresja liniowa - prosta nie umie klasyfikować
regresja liniowa - sigmoid nie umie krzywych, więc dochodzą warstwy. Warstwy nie umieją wielu klas, więc dochodzi softmax. Mało wymiarów nie wystarcza, więc rośnie skala. LLM to suma odpowiedzi na kolejne „a co, jeśli to nie wystarczy?”.