TARIFS = {
    4: {100: (35.00, 0.25), 200: (50.00, 0.20), 300: (65.00, 0.15), '+300': (80.00, 0.10)},
    5: {100: (45.00, 0.30), 200: (60.00, 0.25), 300: (75.00, 0.20), '+300': (95.00, 0.15)},
    6: {100: (60.00, 0.40), 200: (80.00, 0.35), 300: (100.00, 0.30), '+300': (120.00, 0.25)}
}

class TarifsManager:
    def __init__(self):
        self.tarifs = TARIFS
    
    def obtenir_tarif(self, cylindree, forfait_km):
        forfait_key = '+300' if forfait_km == '+300' or (isinstance(forfait_km, int) and forfait_km > 300) else forfait_km
        return self.tarifs.get(cylindree, {}).get(forfait_key)
    
    def afficher_grille(self):
        print("=" * 70)
        print("GRILLE TARIFAIRE")
        print("=" * 70)
        print(f"{'Cylindrée':<15} {'Forfait':<10} {'Coût/jour':<15} {'Prix km supp.':<15}")
        print("-" * 70)
        for cylindree in sorted(self.tarifs.keys()):
            for forfait in [100, 200, 300, '+300']:
                cout_journalier, prix_km_supp = self.tarifs[cylindree][forfait]
                forfait_str = f"{forfait} km" if forfait != '+300' else forfait
                print(f"{cylindree} cylindres   {forfait_str:<10} {cout_journalier:.2f}€{'':<10} {prix_km_supp:.2f}€/km")
            print("-" * 70)