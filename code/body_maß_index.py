print ("Willkommen zu BMI-Farhood. ")
while True:
    koerpergroesse = (input("Um ihren Body Maß Index zu berechnen, geben sie bitte zunächst ihre Körpergröße in Cm an: "))
    if koerpergroesse.isdigit():
        koerpergroesse = int(koerpergroesse)
        break
    else:
        print("Ungültige Eingabe. Bitte versuchen Sie es erneut:")

while True:
    koerpergewicht = (input("Um fortzufahren, geben sie bitte nun ihr Körpergewicht in Kg an: "))
    if koerpergewicht.isdigit():
        koerpergewicht = int(koerpergewicht)
        break
    else:
        print("Ungültige Eingabe. Bitte versuchen Sie es erneut:")


bodymaßindex = koerpergewicht / (koerpergroesse / 100) ** 2
bmi_gerundet = round(bodymaßindex,1)

print ("Dein Bodymaßindex lautet", bmi_gerundet,"\nViel spaß damit.")
