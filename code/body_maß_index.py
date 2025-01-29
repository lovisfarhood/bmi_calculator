import re

muster = r"^\d+(\.\d+)?$"

print ("Willkommen zu BMI-Farhood. ")
while True:
    koerpergroesse = (input("Um ihren Body Maß Index zu berechnen, geben sie bitte zunächst ihre Körpergröße in Cm an: "))
    if re.match(muster, koerpergroesse):
        koerpergroesse = float(koerpergroesse)
        break
    else:
        print("Ungültige Eingabe. Bitte versuchen Sie es erneut:")

while True:
    koerpergewicht = (input("Um fortzufahren, geben sie bitte nun ihr Körpergewicht in Kg an: "))
    if re.match(muster, koerpergewicht):
        koerpergewicht = float(koerpergewicht)
        break
    else:
        print("Ungültige Eingabe. Bitte versuchen Sie es erneut:")


bodymaßindex = koerpergewicht / (koerpergroesse / 100) ** 2
bmi_gerundet = round(bodymaßindex,1)

print ("Dein Bodymaßindex lautet", bmi_gerundet,"\nViel spaß damit.")
