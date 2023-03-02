# Vern mot kjøretidsfeil og logiske feil i programmer 

## Kjøretidsfeil 

Håndtering av kjøretidsfeil i Python gjøres med nøkkelordene try og except.
Python forsøker å kjøre kodeblokken som ligger under `try:`, hvis Python får en feilmelding vil den kjøre kodeblokken som ligger under `except:`.

```python
try:
    alder = int(input("Alder: "))
    fødselsår = 2022 - alder    
    print(f"Fødselsår: {fødselsår}")
except:
    print("Feil: Alder må være et heltall")

prin("koden fortsetter")
```
### Eksperttips: While-løkke med try-excpet 

```python
while True:
    try:
        alder = int(input("Alder: "))
        break
    except:
        print("Alder må være et heltall, prøv igjen")
```

## Logiske feil i programmer 

For å oppdage logiske feil i python-programmer kan vi bruke nøkkelordet `assert` for å forsikre oss om at koden gir korrekte resultat.

```python
assert 10>5 # Ti er større enn fem derfor gjør den ingenting
assert 10 > 20 # Ti er ikke større en 20 derfor gir denne en feilmelding
```

Eksempel: Test av funksjoner med assert 

```python
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

assert omkrets(3,2)==10
assert omkrets(3,3)==12
assert omkrets(2,4)==14
```

### Eksperttips: Håndtering av kjøretidsfeil og logiske fiel 

```python
while True:
    try:
        alder = int(input("Alder: "))
        break
    except:
        print("Alder må være et heltall, prøv igjen")
fødselsår = 2022 - alder    
print(f"Fødselsår: {fødselsår}")
```