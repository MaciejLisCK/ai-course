V matrix
    - kolumna
        - skompresowana reprezentacja embeddingu
        - wizytówka cech danego tokenu
    - el. kolumny
        - składowa skompresowanej reprezentacji embeddingu 
V output
    - kolumna
        - suma ważona atencją skompresowanych reprezentacji embeddingów poprzednich (i obecnego)
        - suma ważona atencją wizytówek cech poprzednich (i obecnego) 
        - mnożymy wszystkie poprzednie wizytówki cech przez uwagę

        - puszyste    niebieskie     stworzenie
            0.5          0.3            0.1
             *            *              *
          wizytówka    wizytówka      wizytówka
            cech         cech           cech
             ||           ||             ||
           spore         średnie       znikome
         wzmocnienie   wzmocnienie   wzmocnienie 
             o             o             o
           cechy         cechy         cechy
         "puszyste"   "niebieskie"     własne
        
                    +               +             =    wizytówka do wzmocnienia semantycznego tokenu stworzenie
                                                       ("stworzenie" zostanie wzmocnione mocno wizytówką 
                                                        cech "puszyste" i średnio wizytówką cech "niebieskie")

        - suma ważona uwagą skompresowanych reprezentacji embeddingów poprzednich (i obecnego)
        - suma ważona uwagą wizytówek cech poprzednich (i obecnego) 
