assert 10>5 # Ti er større enn fem derfor gjør den ingenting

try:
    assert 10 > 20 # Ti er ikke større en 20 derfor gir denne en feilmelding
except:
    print("HOEAHFABSFASFIHABSFAFIEWFBIJAEGBAGJOOGJNGAOJD")

def areal(høyde,bredde):
    areal = høyde*bredde
    try:
        assert høyde >=0
    except: 
        "Høyden er mindre eller lik null, oppgi en positiv høyde"
    try:
        assert bredde >=0
    except: 
        "Bredden er mindre eller lik null, oppgi en positiv bredde"
    return(areal)

    
def omkrets(høyde,bredde):
    omkrets = 2*høyde + 2*bredde
    return(omkrets)


print("Koden er ferdig")