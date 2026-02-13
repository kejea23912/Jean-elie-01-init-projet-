class vehicule: 
    def __init__(self, id_v:str, marque, modele, cylindree:int, kilometrage:float, damc:str):
        self.id_vehicule= id_v
        self.marque = marque
        self.modele = modele
        self.cylindree = cylindree
        self.kilometrage = kilometrage
        self.date_mise_en_circulation = damc

    def to_dict(self):
        return {
            "id_vehicule": self.id_vehicule,
            "marque": self.marque,
            "modele": self.modele,
            "cylindree": self.cylindree,
            "kilometrage_actuel": self.kilometrage_actuel,
            "date_mise_en_circulation": self.date_mise_en_circulation
        }
    
    @staticmethod
    def from_dict(data):
        return Vehicule(
            data["id_vehicule"],
            data["marque"],
            data["modele"],
            data["cylindree"],
            data["kilometrage_actuel"],
            data["date_mise_en_circulation"]
        )
    
    def __str__(self):
        return f"{self.id_vehicule} - {self.marque} {self.modele} ({self.cylindree} cyl., {self.kilometrage_actuel} km)"
