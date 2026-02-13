import os
from models.tarifs import TarifsManager

def nettoyer_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def afficher_menu():
    print("=" * 60)
    print("SYSTEME DE LOCATION DE VEHICULES")
    print("=" * 60)
    print("1. Afficher les clients")
    print("2. Afficher les vehicules")
    print("3. Creer une reservation")
    print("4. Afficher la grille tarifaire")
    print("5. Afficher toutes les reservations")
    print("6. Afficher les reservations d'un client")
    print("7. Quitter")
    print("=" * 60)

def demander_choix_menu():
    return input("Votre choix : ")

def afficher_clients(clients):
    nettoyer_terminal()
    print("=" * 60)
    print("LISTE DES CLIENTS")
    print("=" * 60)
    for client in clients:
        print(client)
    print()

def afficher_vehicules(vehicules):
    nettoyer_terminal()
    print("=" * 60)
    print("LISTE DES VEHICULES")
    print("=" * 60)
    for vehicule in vehicules:
        print(vehicule)
    print()

def demander_id_client():
    return input("ID du client : ")

def demander_reservation(clients, vehicules, tarifs_manager):
    nettoyer_terminal()
    print("=" * 60)
    print("CREER UNE NOUVELLE RESERVATION")
    print("=" * 60)
    print("\nClients disponibles :")
    for client in clients:
        print(f"  - {client}")
    id_client = input("ID du client : ")
    print("\nVehicules disponibles :")
    for vehicule in vehicules:
        print(f"  - {vehicule}")
    id_vehicule = input("ID du vehicule : ")
    date_depart = input("Date de depart (AAAA-MM-JJ) : ")
    date_retour = input("Date de retour (AAAA-MM-JJ) : ")
    print("Forfaits disponibles : 100, 200, 300, +300")
    forfait_km = input("Forfait kilometrique : ")
    if forfait_km != '+300':
        forfait_km = int(forfait_km)
    vehicule = next((v for v in vehicules if v.id_vehicule == id_vehicule), None)
    cylindree = vehicule.cylindree if vehicule else 4
    tarif = tarifs_manager.obtenir_tarif(cylindree, forfait_km)
    cout_journalier, prix_km_supp = tarif if tarif else (0, 0)
    return {'id_client': id_client, 'id_vehicule': id_vehicule, 'date_depart': date_depart, 
            'date_retour': date_retour, 'forfait_km': forfait_km, 'cout_journalier': cout_journalier, 
            'prix_km_supp': prix_km_supp}

def afficher_recapitulatif(reservation):
    print("=" * 60)
    print("RECAPITULATIF DE LA RESERVATION")
    print("=" * 60)
    print(f"Reservation {reservation.id_reservation}")
    print(f"Client: {reservation.id_client}")
    print(f"Vehicule: {reservation.id_vehicule}")
    print(f"Du {reservation.date_depart} au {reservation.date_retour}")
    print(f"Forfait: {reservation.forfait_km} km")
    print(f"Cout journalier: {reservation.cout_journalier}€")
    print(f"Prix km supp.: {reservation.prix_km_supp}€/km")
    print(f"Cout estime: {reservation.cout_estime:.2f}€")
    print("=" * 60)

def afficher_reservations(reservations):
    nettoyer_terminal()
    print("=" * 60)
    print("LISTE DES RESERVATIONS")
    print("=" * 60)
    for r in reservations:
        print(f"{r.id_reservation} | Client: {r.id_client} | Vehicule: {r.id_vehicule} | {r.date_depart} -> {r.date_retour} | Forfait: {r.forfait_km} km | Cout estime: {r.cout_estime:.2f}€")
    print()

def afficher_reservations_client(reservations, id_client):
    nettoyer_terminal()
    print("=" * 60)
    print(f"RESERVATIONS DU CLIENT {id_client}")
    print("=" * 60)
    for r in reservations:
        print(f"{r.id_reservation} | Vehicule: {r.id_vehicule} | {r.date_depart} -> {r.date_retour} | Forfait: {r.forfait_km} km | Cout estime: {r.cout_estime:.2f}€")
    print()