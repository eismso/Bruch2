class Bruch:
    """Die Klasse repäsentiert einen mathematischen Bruch.

        detaillierte Beschreibung hier.
    """
    def __init__(self, z : int, n : int):
        self.zaehler = z #: Zähler des Bruchs
        self.nenner = n #: Nenner des Bruchs

    def __repr__(self):
        return f'{self.zaehler} / {self.nenner}'

    def get_decimal_representation(self) -> float:
        """Wandelt Bruch in einen float Wert und liefert diesen als Rückgabewert.

        Returns
        -------
        float
            Bruch als Dezimalzahl.
        """
        return self.zaehler / self.nenner

    def multiply(self, bruch2 : 'Bruch') -> 'Bruch':
        """Multipliziert zwei Brüche und speichert das Ergebnis in einem neuen Bruch.

        Parameters
        ----------
        bruch2 : Bruch
            Zweiter Operand der Multiplikation.
        Returns
        -------
        Bruch
            Liefert einen neuen Bruch mit dem Ergebnis der Multiplikation.
        """
        # alternativ waere auch moeglich
        #erg = Bruch(1, 1)
        #erg.zaehler = self.zaehler * bruch2.zaehler
        #erg.nenner = self.nenner * bruch2.nenner
        #return erg
        # bis hier
        return Bruch(self.zaehler * bruch2.zaehler, self.nenner * bruch2.nenner)

    def add(self, bruch2: 'Bruch') -> 'Bruch':
        """Addiert zwei Brüche und speichert das Ergebnis in einem neuen Bruch.

        Parameters
        ----------
        bruch2 : Bruch
            Zweiter Operand der Multiplikation.
        Returns
        -------
        Bruch
            Liefert einen neuen Bruch mit dem Ergebnis der Addition
        """
        return Bruch(self.zaehler * bruch2.nenner + bruch2.zaehler * self.nenner, self.nenner * bruch2.nenner)


if __name__ == '__main__':
    br1 = Bruch(1, 2)
    br2 = Bruch(3, 4)

    print(br1.add(br2))
    print(br1.multiply(br2))




















