class Reservation:
    def __init__(self,id_reservation, id_client,id_vehicule, date_depart: str, date_retour: str,forfait_km: int,
        cout_journalier,prix_km_supp,cout_estime):
        self.id_reservation = id_reservation
        self.id_client = id_client
        self.id_vehicule = id_vehicule
        self.date_depart = date_depart
        self.date_retour = date_retour
        self.forfait_km = forfait_km
        self.cout_journalier = cout_journalier
        self.prix_km_supp = prix_km_supp
        self.cout_estime = cout_estime
