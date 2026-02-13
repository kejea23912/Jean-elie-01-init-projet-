
from multiprocessing.dummy.connection import Client


class client:
    def __init__(self, id_client:str, nom, prenom, mail, telephone, adresse):
        self.id_client = id_client
        self.nom = nom
        self.prenom = prenom
        self.mail = mail 
        self.telephone = telephone
        self.adresse = adresse


    def to_dict(self):
        return {
            "id_client": self.id_client,
            "nom": self.nom,
            "prenom": self.prenom,
            "mail": self.mail,
            "telephone": self.telephone,
            "adresse": self.adresse
        }
    @staticmethod
    def from_dict(data):
        return Client(
            data["id_client"],
            data["nom"],
            data["prenom"],
            data["mail"],
            data["telephone"],
            data["adresse"]
        )
    def __str__(self):
        return f"{self.id_client} - {self.prenom} {self.nom} ({self.mail})"