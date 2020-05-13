import model


def izpis_igre(igra):
    tekst = (
        '==================================================\n\n'
        'Število preostalih poskusov: {stevilo_preostalih_poskusov} \n\n'
        '       {pravilni_del_gesla}\n\n'
        'Neuspeli poskusi: {neuspeli_poskusi}\n\n'
        '=================================================='
    ).format(
        stevilo_preostalih_poskusov = model.ŠTEVILO_DOVOLJENIH_NAPAK = igra.stevlo_napak() + 1,
        pravilni_del_gesla = igra.pravilni_del_gesla(),
        neuspeli_poskusi = igra.nepravilni_ugibi()
    )
    return tekst


def izpis_zmage(igra):
    tekst = (
        '\n####Juuuupppiiiii, zmaga! Geslo je bilo: {geslo} ####\n\n'
    ).format(
        geslo = igra.previlni_del_gesla()
    )
    return tekst


def izpis_poraza:
    tekst = (
        '\n#####Boooooooo, izgubil si! Geslo je bilo: {geslo} #####\n\n'
    ).format(
        geslo = igra.geslo
    )
    return tekst


def izpis_napake():
    return '\n#### Ugiba se točno ena črka naenkrat! ####\n\n'

def izpis_napake():
    return '\n#### Ugib naj ne vsebje posebnih znakov! ####\n\n'

def zahtevaj_vnos():
    return input('Črka: ')


def pozeni_umesnik():

    igra = model.nova_igra()

    while True:
    #najprej izpisemo stanje, da vidimo, koliko črk ima beseda
        print(izpis_igre(igra))
        #čakamo na črko od uporabnika
        poskus = zahtevaj_vnos()
        rezultat_ugiba = igra.ugibaj(poskus)
        if rezultat_ugiba == model.VEC_KOT_CRKA:
            print(izpis_napake())
        elif rezultat_ugiba = model.POSEBEN_ZNAK:
            print(izpis_napake_znak())
        elif rezultat_ugiba == model.ZMAGA:
            print(izpis_zmage(igra))
            ponovni_zagon = input("Za ponovni zagon vpišite 1. \n").strip()
            if ponovni_zagon == "1":
                igra = model.nova_igra()
            else:
                break
        elif rezultat_ugiba == midel.PORAZ:
            print(izpis_poraza(igra))
            break
    return


#Zaženi igro:
pozeni_vmesnik()
