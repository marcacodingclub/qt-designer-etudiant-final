import json

class Local:

    def __init__(self, p_type, p_numero, p_lieu, p_dimension, p_places) -> None:
        self._type = p_type
        self._numero = p_numero
        self._lieu = p_lieu
        self._dimension = p_dimension
        self._places = p_places
    
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, v:str):
        print(v)
        if v.capitalize() not in ["Technique", "Normal"]: raise ValueError("Erreur de valeur type")
        self._type = v

    ########################################################################################################

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, v:str):
        if len(v) <= 2:
            raise ValueError("Erreur de valeur numero")
        
        if v[0].isalpha() and v[1] == "-":
            self._numero = v
        else:
            raise ValueError("Erreur de valeur numero")

    ########################################################################################################

    @property
    def lieu(self):
        return self._lieu

    @lieu.setter
    def lieu(self, v:str):
        #if v.upper() not in ["A", "B", "C"]: raise ValueError("Erreur de valeur lieu")
        self._lieu = v.upper()

    ########################################################################################################

    @property
    def dimension(self):
        return self._dimension

    @dimension.setter
    def dimension(self, v:int):
        if v <= 0: raise ValueError("Erreur de valeur dimension") 
        self._dimension = v

    ########################################################################################################

    @property
    def places(self):
        return self._places

    @places.setter
    def places(self, v:int):
        if v <= 25: raise ValueError("Erreur de valeur places") 
        self._places = v
        
    ########################################################################################################