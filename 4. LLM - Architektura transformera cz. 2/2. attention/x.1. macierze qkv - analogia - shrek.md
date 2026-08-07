Pokazać zdjęcia

Osioł (Shrek) szuka mikołajka płaskolistnego, zbiera nektar w celu zniesienia klątwy.

# Proste porównanie

1. Osioł szuka obiektu, o konkretnych cechach: roślina, niebieskość kwiatu, kolczastość
2. Każdy obiekt w lesie (kamień, liść, róża, mikołajek) ma nałożony filtr wyostrzający z ich cechy: bycie rośliną, niebieskości kwiatu, kolczastość 
3. Osioł porównuje
    czerwona róża → słabe dopasowanie (zły kolor)
    żółta stokrotka → bardzo słabe dopasowanie (zły kolor, brak kolców)
    mikołajek płaskolistny → bardzo silne dopasowanie
4. Osioł zbiera mikołajki płaskolisne
5. Osioł zabieraja nektar; odrzuca kolce, płatki, łodygi

# Proste porównanie 2

0. Nakładając macierz Q na poszczególne obiekty wynika że to osioł szuka: rośliny, niebieskości kwiatu, kolczastość. Inne rzeczy niczego nie szukają.
2. Każdy obiekt w lesie (kamień, liść, róża, mikołajek) ma nałożoną macierz K wyostrzająca z ich embedingów cech: rośliny, niebieskości kwiatu, kolczastość 
3. Osioł porównuje query-key
    czerwona róża → słabe dopasowanie (zły kolor)
    żółta stokrotka → bardzo słabe dopasowanie (zły kolor, brak kolców)
    mikołajek płaskolistny → bardzo silne dopasowanie
4. Osioł zbiera mikołajki płaskolisne
5. Osioł nakłada macierz V zabierając nektar; odrzuca kolce, płatki, łodygi


# Bardziej trafne porównanie

Osioł (Shrek) szuka mikołajka płaskolistnego, zbiera nektar w celu zniesienia klątwy.

1. Osioł zadaje pytanie: jego embedding przechodzi przez macierz Q, dając wektor zapytania (query) opisujący czego szuka - cechy "roślina", "niebieskość kwiatu", "kolczastość".
2. Nie tylko osioł - każdy obiekt w lesie (róża, stokrotka, mikołajek) przepuszcza swój embedding przez tę samą macierz K, dostając swój wektor klucza (key) - rodzaj "wizytówki" opisującej jego cechy.
3. Osioł porównuje swoje query z kluczem każdego obiektu (iloczyn skalarny), dostając surowy wynik dopasowania:
    czerwona róża → słabe dopasowanie (zły kolor)
    żółta stokrotka → bardzo słabe dopasowanie (zły kolor, brak kolców)
    mikołajek płaskolistny → bardzo silne dopasowanie
4. Wyniki dopasowania przechodzą przez softmax i zamieniają się w wagi sumujące się do 1 - osioł nie wybiera tylko jednej rośliny na zasadzie "wszystko albo nic", tylko rozdziela między nie "uwagę" proporcjonalnie do dopasowania, np. róża 2%, stokrotka 1%, mikołajek 97%.
5. Każdy obiekt przepuszcza swój embedding przez macierz V, dostając wektor wartości (value) - "esencję" rośliny bez cech nieistotnych do przekazania dalej (znika kolczastość, kolor płatków, kształt łodygi - zostaje sama treść, np. "nektar").
6. To, co ostatecznie dostaje osioł, to ważona suma wartości (value) wszystkich obiektów, ważona wagami uwagi z punktu 4 - czyli głównie nektar mikołajka, ale też odrobina "esencji" róży i stokrotki.

