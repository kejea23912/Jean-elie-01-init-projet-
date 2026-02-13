from datetime import datetime

class Reservation:
    def __init__(self, id_reservation, id_client, id_vehicule, date_depart, date_retour, 
                 forfait_km, cout_journalier, prix_km_supp):
        self.id_reservation = id_reservation
        self.id_client = id_client
        self.id_vehicule = id_vehicule
        self.date_depart = date_depart
        self.date_retour = date_retour
        self.forfait_km = forfait_km
        self.cout_journalier = cout_journalier
        self.prix_km_supp = prix_km_supp
        self.cout_estime = self._calculer_cout_estime()
    
    def _calculer_cout_estime(self):
        date1 = datetime.strptime(self.date_depart, "%Y-%m-%d")
        date2 = datetime.strptime(self.date_retour, "%Y-%m-%d")
        nb_jours = (date2 - date1).days
        if nb_jours < 1:
            nb_jours = 1
        return self.cout_journalier * nb_jours
    
    def to_dict(self):
        return {
            "id_reservation": self.id_reservation,
            "id_client": self.id_client,
            "id_vehicule": self.id_vehicule,
            "date_depart": self.date_depart,
            "date_retour": self.date_retour,
            "forfait_km": self.forfait_km,
            "cout_journalier": self.cout_journalier,
            "prix_km_supp": self.prix_km_supp,
            "cout_estime": self.cout_estime
        }
    
    @staticmethod
    def from_dict(data):
        return Reservation(
            data["id_reservation"],
            data["id_client"],
            data["id_vehicule"],
            data["date_depart"],
            data["date_retour"],
            data["forfait_km"],
            data["cout_journalier"],
            data["prix_km_supp"]
        )
    
    def __str__(self):
        return f"{self.id_reservation} | Client: {self.id_client} | Vehicule: {self.id_vehicule} | {self.date_depart} -> {self.date_retour}"