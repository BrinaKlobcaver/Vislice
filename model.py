import random
import json

STEVILO_DOVOLJENIH_NAPAK = 9
PRAVILNA_CRKA ="+"
PONOVLJENA_CRKA = "0"
VEC_KOT_CRKA = ">"
POSEBEN_ZNAK = "#"
NAPACNA_CRKA = "-"
ZMAGA = "w"
PORAZ = "x"
ZACETEK = "s"

class Igra:

    def __init__(self, geslo, crke = None):
        self.geslo = geslo
        if crke is None:
            self.crke = []
        else:
            self.crke = crke
    
    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self):
        return[crka for crka in self.crke if crka in self.geslo]  

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
       return all(crka in self.crke for crka in self.geslo)
        
    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        delni = ''
        for crka in self.geslo:
            if crka in self.crke:
                delni += crka + " "
            else:
                delni += '_ '
        return delni[:-1]

    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())

    def ugibaj(self, ugib):
        if len(ugib) > 1 or len(ugib) == 0:
            return VEC_KOT_CRKA
        crka = ugib.upper()
        if crka not in 'ABCČDEFGHIJKLMNOPRSŠTUVWZŽĐ':
            return POSEBEN_ZNAK
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)

            if crka in self.geslo:
                if self.zmaga():
                    return ZMAGA
                else:
                    return PRAVILNA_CRKA
            else:
                if self.poraz():
                    return PORAZ
                else:
                    return NAPACNA_CRKA

with open("besede.txt", "r", encoding = "utf-8") as datoteka_z_besedami:
    bazen_besed = [vrstica.strip().upper() for vrstica in datoteka_z_besedami]

    
def nova_igra():
    return Igra(random.choice(bazen_besed))


class Vislice:

    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1

    def nova_igra(self):
        igra = nova_igra()
        id_igre = self.prost_id_igre()
        self.igre[id_igre] = (igra, ZACETEK)
        return id_igre

    def ugibaj(self, id_igre, crka):
        igra, _ = self.igre[id_igre]
        poskus = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, poskus)

    def zapisi_igre_v_datoteko(self):
        with open(self.datoteka_s_stanjem, 'w', encoding ='utf_8') as f:
            igre1 = {
                id_igre : ((igra.geslo, igra.crke), poskus)
                for id_igre, (igra, poskus) in self.igre.items()
            } 
            json.dump(igre1, f)
            return 

    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem, 'r', encoding ='utf_8') as f:
            igre = json.load(f)
            self.igre = {
                id_igre : ((igra.geslo, igra.crke), poskus)
                for id_igre, (igra, poskus) in self.igre.items()
            }
#popravi tole nujno oz. dopolni!!!!!!!!!!!!!!!!!!!!!!!!