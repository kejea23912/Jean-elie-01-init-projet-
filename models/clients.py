
class client:
    def __init__(self, id:str, n, p, m, t, a):
        self.id_client = id
        self.nom = n
        self.prenom = p
        self.mail = m 
        self.telephone = t
        self.adresse = a


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