import re

class BmiCalculator:
    def __init__(self):
        self.koerpergroesse = None
        self.koerpergewicht = None

    def zahleingabe(self, zahlkontrolle):
        muster = r"^\d+(\.\d+)?$"
        while True:
            eingabe = input(zahlkontrolle).replace(",", ".")
            if re.match(muster, eingabe):
                koerpergroesse = float(eingabe)
                break
            else:
                print("Ungültige Eingabe. Bitte versuchen Sie es erneut:")

    def berechne_bmi(self):
        bodymassindex = self.koerpergewicht / (self.koerpergroesse / 100) ** 2
        bmi_gerundet = round(bodymassindex, 1)
        print("Dein Bodymaßindex lautet", bmi_gerundet, "\nViel Spaß damit.")

    def aktivieren(self):
        print("Willkommen zu BMI-Farhood.")
        self.koerpergroesse = self.zahleingabe("Um ihren Body Maß Index zu berechnen, geben sie bitte zunächst ihre Körpergröße in Cm an: ")
        self.koerpergewicht = self.zahleingabe("Bitte geben Sie nun Ihr Körpergewicht in Kg an: ")
        bmi = self.berechne_bmi()
        print ("Dein Bodymaßindex lautet", bmi_gerundet,"\nViel spaß damit.")

