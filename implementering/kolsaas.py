import matplotlib.pyplot as plt

fil = open("kolsaas.csv")
data = fil.read()

linjer = data.split("\n")
tur = []
for linje in linjer: 
    splittet_linje = linje.split(",")
    tur.append(splittet_linje)

print(tur[0][0])

x = []
y = []
for linje in tur[1:]:
   høyde = float(linje[3])
   time = float(linje[0])
   x.append(time)
   y.append(høyde)

plt.scatter(x,y)
plt.show()
