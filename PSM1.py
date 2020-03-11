import math

class Main:

    def podajLiczbe(wiadomosc):
        while True:
            try:
                liczba = float(input(wiadomosc))
            except ValueError:
                print("Podaj float")
                continue
            else:
                return liczba

# liczbe float którą wpisujemy trzeba podać po kropce - a w javie po przecinku

#sin(x) = sin(0) + xcos(0) - x^2 sin(0) / 2! - x^3 cos(0) / 3! + x^4 sin(0) / 4! + x^5 cos(0) / 5! - x^6 sin(0) / 6! - x^7 cos(0) / 7! + x^8 sin(0) / 8!
# + x^9 cos(0) / 9! + x^10 sin(0) / 10!
#sin(0) = 0, cos(0) = 1, więc można uprościć wzór
#sin(x) = x - x^3 / 3! + x^5 / 5! - x^7 / 7! + x^9 / 9!

    petla = 10
    wejscie = float(podajLiczbe("Podaj liczbe"))
    wejscie = float(wejscie % 2)

    #wynik prawdilowy do ktorego bedziemy porownywac nasz wynik
    wynikPrawdilowy = math.sin(math.pi*wejscie)
    print("Poprawny wynik: " + str(wynikPrawdilowy))

    #zmiana znaku sin w odpowiednich cwiartkach
    zmiana = 1
    if(wejscie>0.5):
        if(wejscie<1):
            wejscie = 1 - wejscie
        elif(wejscie<1.5):
            zmiana = -1
            wejscie -= 1
        else:
            zmiana = -1
            wejscie = 2-wejscie

    alfa = bool(False)  #zmiana znaku przy powtorzeniu pętli
    licznik = 1         #używamy do wyliczenia silnii
    poczatkowaWartosc = math.pi*float(wejscie)     #poczatkowa wartosc sin(x)
    poprzednia = poczatkowaWartosc      #wartosc poprzedniego obliczenia
    potega = poczatkowaWartosc*poczatkowaWartosc #x^2, policzone wczesniej dla effeciency

#    print("1) => " + str(poczatkowaWartosc*zmiana) + ", różnica => " + str(abs(abs(poczatkowaWartosc)-abs(wynikPrawdilowy))))
    for i in range(0, 9, 2):
        licznik += 2
        poprzednia = poprzednia*(potega/(licznik*(licznik-1)))
        if(poczatkowaWartosc == zmiana):
            poczatkowaWartosc = poczatkowaWartosc + poprzednia
        else:
            poczatkowaWartosc = poczatkowaWartosc - poprzednia
        alfa = not alfa
        print("" + str((i + 1)) + ") => " + str(poczatkowaWartosc*zmiana) + ", roznica => " + str(abs(abs(poczatkowaWartosc)-abs(wynikPrawdilowy))))
# git add ./*
# git commit ( -m " " )
# git push