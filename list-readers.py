from smartcard.System import readers
from smartcard.Exceptions import NoCardException, CardConnectionException

r = readers()
if len(r) == 0:
    print("Aucun lecteur détecté")
else:
    print("Lecteurs détectés:")
    for reader in r:
        print(f"- {reader}")

    print("\nStatut des cartes dans chaque lecteur:")
    for reader in r:
        connection = reader.createConnection()
        try:
            connection.connect()  # tente de se connecter à la carte
            atr = connection.getATR()
            atr_str = ' '.join(f"{b:02X}" for b in atr)
            print(f"Carte détectée dans '{reader}': ATR = {atr_str}")
        except NoCardException:
            print(f"Aucune carte SIM insérée dans '{reader}'")
        except CardConnectionException as e:
            print(f"Erreur de connexion à la carte dans '{reader}': {e}")
