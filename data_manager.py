import json
from models.clients import client
from models.vehicule import vehicule
from models.reservation import Reservation

def charger_clients():
    try:
        with open('clients.json', 'r') as f:
            return [client.from_dict(c) for c in json.load(f)]
    except Exception as e:
        print(f"ERREUR chargement clients: {e}")
        return []

def charger_vehicules():
    try:
        with open('vehicules.json', 'r') as f:
            return [vehicule.from_dict(v) for v in json.load(f)]
    except Exception as e:
        print(f"ERREUR chargement vehicules: {e}")
        return []

def charger_reservations():
    try:
        with open('reservations.json', 'r') as f:
            return [Reservation.from_dict(r) for r in json.load(f)]
    except:
        return []

def sauvegarder_reservation(reservation):
    reservations = charger_reservations()
    reservations.append(reservation)
    with open('reservations.json', 'w') as f:
        json.dump([r.to_dict() for r in reservations], f, ensure_ascii=False, indent=2)
    print("Reservation sauvegardee dans reservations.json")

def generer_id_reservation():
    reservations = charger_reservations()
    if not reservations:
        return "R0001"
    numeros = [int(r.id_reservation[1:]) for r in reservations]
    return f"R{max(numeros) + 1:04d}"

def filtrer_reservations_par_client(id_client):
    return [r for r in charger_reservations() if r.id_client == id_client]