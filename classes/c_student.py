import datetime

from PyQt5.QtCore import QDate

class Etudiant:

    lst_Etudiant = []

    def __init__(self, p_nom:str = None, p_prenom:str = None, p_matricule:str = None, p_date_naissance:QDate = None, p_programme:str = None) -> None:

        self._nom = p_nom
        self._prenom = p_prenom
        self._matricule = p_matricule
        self._p_date_naissance = p_date_naissance
        self._age = None
        self.programme = p_programme

    def __str__(self):
        return f"""
******************************************************
Nom: {self.nom}
Prenom: {self.prenom}
Matricule: {self.matricule}
Date de naissance: {self.date_naissance}
Age: {self.age}
Programme: {self.programme}
*******************************************************
        """

    #################################################################################################################################
    @classmethod
    def lst_ajouter(cls):
        cls.lst_Etudiant.append(cls)

    @staticmethod
    def calc_age(dob:QDate):
        return datetime.datetime.today().year - dob.year()
    #################################################################################################################################

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, s:str):
        if s.isalpha():
            self._nom = s

        else:
            raise ValueError("Nom invalide")

    #################################################################################################################################

    @property
    def prenom(self):
        return self._prenom

    @nom.setter
    def prenom(self, s:str):

        if s.isalpha():
            self._prenom = s

        else:
            raise ValueError("Prenom invalide")

    #################################################################################################################################

    @property
    def matricule(self):
        return self._matricule

    @matricule.setter
    def matricule(self, s:str):
        if s.isnumeric() and len(s) == 7:
            self._matricule = s
        else:
            raise ValueError("Matricule invalide")
    #################################################################################################################################
    @property
    def age(self):
        return self._age
    #################################################################################################################################

    @property
    def date_naissance(self):
        return self._p_date_naissance.toString()

    @date_naissance.setter
    def date_naissance(self, s:QDate):

        if s > datetime.datetime.today():
            raise ValueError("Date est invalide")
        else:

            #set date de naissance
            self._p_date_naissance = s

            # set l'age ici
            self._age = self.calc_age(s)

    #################################################################################################################################
