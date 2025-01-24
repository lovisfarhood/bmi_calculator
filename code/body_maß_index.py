print ("Willkommen zu BMI-Farhood. ")
koerpergroesse = float(input("Um ihren Body Maß Index zu berechnen, geben sie bitte zunächst ihre Körpergröße in Cm an: "))
koerpergewicht = float(input("Um fortzufahren, geben sie bitte nun ihr Körpergewicht in Kg an: "))

bodymaßindex = koerpergewicht / (koerpergroesse / 100) ** 2

print ("Dein Bodymaßindex lautet", bodymaßindex,"\nViel spaß damit.")