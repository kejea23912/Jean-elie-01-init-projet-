import data_manager as dm
import ui
from models.tarifs import TarifsManager
from models.reservation import Reservation

def main():
    print("=" * 60)
    print("Chargement des donnees...")
    clients = dm.charger_clients()
    vehicules = dm.charger_vehicules()
    print(f"✓ {len(clients)} client(s) charge(s)")
    print(f"✓ {len(vehicules)} vehicule(s) charge(s)")
    print("=" * 60)
    
    tarifs_manager = TarifsManager()
    
    while True:
        ui.afficher_menu()
        choix = ui.demander_choix_menu()
        
        if choix == '1':
            ui.afficher_clients(clients)
        
        elif choix == '2':
            ui.afficher_vehicules(vehicules)
        
        elif choix == '3':
            data = ui.demander_reservation(clients, vehicules, tarifs_manager)
            id_resa = dm.generer_id_reservation()
            reservation = Reservation(id_resa, data['id_client'], data['id_vehicule'],
                                     data['date_depart'], data['date_retour'], data['forfait_km'],
                                     data['cout_journalier'], data['prix_km_supp'])
            ui.afficher_recapitulatif(reservation)
            confirm = input("\nSauvegarder cette reservation ? (o/n) : ")
            if confirm.lower() == 'o':
                dm.sauvegarder_reservation(reservation)
                print("✓ Reservation enregistree avec succes !")
        
        elif choix == '4':
            ui.nettoyer_terminal()
            tarifs_manager.afficher_grille()
        
        elif choix == '5':
            reservations = dm.charger_reservations()
            ui.afficher_reservations(reservations)
        
        elif choix == '6':
            id_client = ui.demander_id_client()
            reservations = dm.filtrer_reservations_par_client(id_client)
            ui.afficher_reservations_client(reservations, id_client)
        
        elif choix == '7':
            print("Au revoir !")
            break
        
        else:
            print("Choix invalide")

if __name__ == "__main__":
    main()