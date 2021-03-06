import bottle
import model

SKRIVNOST = "moja_prva_skrivnost"
vislice = model.Vislice()

@bottle.get('/')
def index():
    return bottle.template('index.tpl')

@bottle.post('/nova_igra/')
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.request.set_cookie("idigre", id_igre, path = '/')
    bottle.redirect('/igra/')

!!@bottle.post('/igra/')
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.redirect('/igra/{}/'.format(id_igre))

!!@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
    igra, poskus1 = vislice.igre[id_igre]
    return bottle.template('igra.tpl', id_igre = id_igre, igra = igra, poskus = poskus1)

!!@bottle.post('/igra/<id_igre:int>/')
def ugibaj(id_igre):
    crka = bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra/{}/'.format(id_igre))

@bottle.get('/img/<pictures>')
def serve_pictures(picture):
    return bottle.static_file(picture, root='img')

bottle.run(reloader=True, debug=True)

