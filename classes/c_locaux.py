import json
from classes.c_local import Local

lst_locals = []

class Local_Normal(Local):
    def __init__(self, p_type = "Normal", p_numero = "A-453", p_lieu = "Gabrielle Roy", p_dimension = 5, p_places = 32) -> None:
        super().__init__(p_type, p_numero, p_lieu, p_dimension, p_places)

    def __str__(self):
        return f"""
Type: {self._type}
Numero: {self._numero}
Lieu: {self._lieu}
Dimension: {self._dimension}
Places: {self._places}
        """
    
    def serialiser(self):
        with open("ressources/classes.json", "r") as f_read:
            data = json.load(f_read)

        data[self.numero] = self.__dict__

        with open("ressources/classes.json", "w") as f_write:
            json.dump(data, f_write, indent=4, ensure_ascii=False)

    def deserialiser(self, num_classe):
        with open("ressources/classes.json", "r") as f_read:
            data = json.load(f_read)
            self.__dict__ = data[num_classe]

class Local_Technique(Local):
    def __init__(self, p_type = "Technique", p_numero = "A-453", p_lieu = "Gabrielle Roy", p_dimension = 5, p_places = 32, p_marque_ordinateur = "Dell", p_nb_ordinateur = 10) -> None:
        super().__init__(p_type, p_numero, p_lieu, p_dimension, p_places)
        self._marque_ordinateurs = p_marque_ordinateur
        self._nb_ordinateur = p_nb_ordinateur
        self.Projecteur = False

    def __str__(self):
        return f"""
Type: {self.type}
Numero: {self.numero}
Lieu: {self.lieu}
Dimension: {self.dimension}
Places: {self.places}
Marque Ordinateur: {self.marque_ordinateur}
Nombre Ordinateur: {self.nb_ordinateur}
Projecteur: {self.Projecteur}
        """

    def serialiser(self):
        with open("ressources/classes.json", "r") as f_read:
            data = json.load(f_read)

        data[self.numero] = self.__dict__

        with open("ressources/classes.json", "w") as f_write:
            json.dump(data, f_write, indent=4, ensure_ascii=False)

    def deserialiser(self, num_classe):
        with open("ressources/classes.json", "r") as f_read:
            data = json.load(f_read)
            self.__dict__ = data[num_classe]

    @property
    def marque_ordinateur(self):
        return self._marque_ordinateurs
    
    @marque_ordinateur.setter
    def marque_ordinateur(self, v:str):
        if len(v) > 100: raise ValueError("Trop grand")

    ###########################################################################################################################

    @property
    def nb_ordinateur(self):
        return self._nb_ordinateur
    
    @nb_ordinateur.setter
    def nb_ordinateur(self, v:int):
        if v > 25: raise ValueError("Erreur de valeur.")

