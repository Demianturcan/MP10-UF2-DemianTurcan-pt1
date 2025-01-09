

class Client:
    def __init__(self, id_client, nom, email):
        self.id_client = id_client
        self.nom = nom
        self.email = email
        self.comandes = []

    def __repr__(self):
        return f"client{self.id_client}( id={self.id_client}, nom='{self.nom}', email='{self.email}', "f"comandes={len(self.comandes)} )"

    def afegir_comanda(self, comanda):
        self.comandes.append(comanda)

    def consultar_comandes(self):
        print(f"Comandes del client {self.nom}: {len(self.comandes)}")
        print(self.comandes)

