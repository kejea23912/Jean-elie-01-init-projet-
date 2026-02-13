class vehicule: 
    def __init__(self, id_v:str, marque, modele, cylindree:int, kilometrage:float, damc:str):
        self.id_vehicule= id_v
        self.marque = marque
        self.modele = modele
        self.cylindree = cylindree
        self.kilometrage = kilometrage
        self.date_mise_en_circulation = damc
