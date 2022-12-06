# Wojciech Kowalczyk 2 IO 166285 

class ListaWpis:
    def __init__(self, wart: str, nast: 'ListaWpis' = None, poprz: 'ListaWpis' = None):
        self.wart = wart
        self.nast = nast
        self.poprz = poprz

    def dodaj_po_nim(self, wart: str):
        stary_nast = self.nast
        nowy = ListaWpis(wart)
        self.nast = nowy
        nowy.poprz = self
        if stary_nast is not None:
            stary_nast.poprz = nowy
            nowy.nast = stary_nast

    def dodaj_przed_nim(self, wart: str):
        stary_poprz = self.poprz
        nowy = ListaWpis(wart)
        self.poprz = nowy
        nowy.nast = self
        if stary_poprz is not None:
            stary_poprz.nast = nowy
            nowy.poprz = stary_poprz

    def zamien(self, el_inny: 'ListaWpis'):
        if self.nast == el_inny:
            if el_inny.nast is not None:
                el_inny.nast.poprz = self
            if self.poprz is not None:
                self.poprz.nast = el_inny
            temp = self.poprz
            self.nast = el_inny.nast
            el_inny.nast = el_inny.poprz
            self.poprz = el_inny
            el_inny.poprz = temp
        if self.poprz == el_inny:
            if self.nast is not None:
                self.nast.poprz = el_inny
            if el_inny.poprz is not None:
                el_inny.poprz.nast = self
            temp = el_inny.poprz
            el_inny.nast = self.nast
            self.nast = self.poprz
            el_inny.poprz = self
            self.poprz = temp
        if self == el_inny:
            return
        if self.poprz != el_inny and self.nast != el_inny:
            if el_inny.nast is not None:
                el_inny.nast.poprz = self
            if self.poprz is not None:
                self.poprz.nast = el_inny
            el_inny.poprz.nast = self
            self.nast.poprz = el_inny
            temp = self.nast
            temp_b = self.poprz
            self.nast = el_inny.nast
            self.poprz = el_inny.poprz
            el_inny.nast = temp
            el_inny.poprz = temp_b

    def __str__(self):
        return self.wart


class Lista_2k_k:
    def __init__(self, element: 'ListaWpis' = None):
        self.element = element
        self.pierwszy = None
        self.ostatni = None
        if (self.element.nast is None) and (self.element.poprz is None):
            self.element.nast = self.element
            self.element.poprz = self.element
            self.pierwszy = self.element
            self.ostatni = self.element
        if (self.element.nast is None) and (self.element.poprz is not None):
            self.ostatni = self.element
            k = self.element
            while self.element.poprz is not None:
                self.element = self.element.poprz
            self.pierwszy = self.element
            self.element = k
        if (self.element.nast is not None) and (self.element.poprz is None):
            self.pierwszy = self.element
            k = self.element
            while self.element.nast is not None:
                self.element = self.element.nast
            self.ostatni = self.element
            self.element = k
        if (self.element.nast is not None) and (self.element.poprz is not None):
            k = self.element
            while self.element.nast is not None:
                self.element = self.element.nast
            self.ostatni = self.element
            self.element = k
            while self.element.poprz is not None:
                self.element = self.element.poprz
            self.pierwszy = self.element
            self.element = k
        self.ostatni.nast = self.pierwszy
        self.pierwszy.poprz = self.ostatni

    def druknij_liste(self):
        k = self.element
        self.element = self.pierwszy
        print(self.element)
        while self.element != self.ostatni:
            self.element = self.element.nast
            print(self.element)
        self.element = k

    def dodaj_el(self, dodaj):
        self.ostatni.nast = dodaj
        dodaj.nast = self.pierwszy
        self.pierwszy.poprz = dodaj
        dodaj.poprz = self.ostatni
        self.ostatni = dodaj

    def usun_el(self, usun):
        if usun == self.pierwszy:
            usun.nast.poprz = self.ostatni
            self.ostatni.nast = usun.nast
            self.pierwszy = usun.nast
            self.element = usun.nast
        if usun == self.ostatni:
            self.ostatni = usun.poprz
            usun.wart = None
            usun.poprz.nast = None
        if (usun != self.ostatni) and (usun != self.pierwszy):
            usun.poprz.nast = usun.nast
            usun.nast.poprz = usun.poprz
            usun.wart = None

    def pobierz_el(self, idx: int):
        k = self.element
        self.element = self.pierwszy
        if idx > 0:
            while idx > 0:
                self.element = self.element.nast
                idx = idx - 1
        else:
            while idx < 0:
                self.element = self.element.poprz
                idx = idx + 1
        i = self.element
        self.element = k
        return i

    def usun_wszystkie_pasujace(self, wart: str):
        usunietych = 0
        k = self.element
        self.element = self.pierwszy
        while self.element != self.ostatni:
            if self.element.wart == wart:
                self.usun_el(self.element)
                usunietych = usunietych + 1
            self.element = self.element.nast
        if self.ostatni.wart == wart:
            self.usun_el(self.ostatni)
            usunietych = usunietych + 1
        self.element = k
        return usunietych

    def wypisz(self, aktualna, nastepna):
        print(str(aktualna) + " + " + str(nastepna) + " + ", end=' ')

    def obrob_wartosci(self):
        k = self.element
        self.element = self.pierwszy
        while self.element != self.ostatni:
            self.wypisz(self.element.wart, self.element.nast.wart)
            self.element = self.element.nast
        print(str(self.ostatni) + " + " + str(self.ostatni.nast), end=' ')
        print('\n')
        self.element = k

    def print_w_tyl(self):
        print(str(self.element) + " <> ", end=' ')
        k = self.element
        self.element = self.element.poprz
        while self.element != k:
            print(str(self.element) + " <> ", end=' ')
            self.element = self.element.poprz
        print(str(self.element) + " <> ")
        self.element = k
        print('\n')

    def odwroc(self):
        p = self.pierwszy
        self.pierwszy = self.ostatni
        self.ostatni = p
        self.element = self.pierwszy
        while self.element != self.ostatni:
            i = self.element.nast
            self.element.nast = self.element.poprz
            self.element.poprz = i
            self.element = self.element.nast
        self.element = self.pierwszy
