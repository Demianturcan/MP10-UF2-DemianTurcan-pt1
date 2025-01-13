# gestio_erp/comandes.py
class Comanda:
    ESTATS = {
        "PENDENT": "pendent",
        "COMPLETADA": "completada",
    }

    def __init__(self, id_comanda, estat=ESTATS["PENDENT"]):
        self.id_comanda = id_comanda
        self.productes = {}
        self.estat = estat

    def __repr__(self):
        return (
            f"Comanda {self.id_comanda} [{self.estat}]"
            f" productes={self.productes} )"
        )

    def afegir_producte(self, producte, quantitat=1):
        if producte.id_producte in self.productes:
            self.productes[producte.id_producte].quantitat += quantitat
        else:
            producte.quantitat = quantitat
            self.productes[producte.id_producte] = producte

    def total_productes(self):
        return sum(producte.quantitat for producte in self.productes.values())

    def resum_comanda(self):
        resum = f"Resum de la Comanda ID: {self.id_comanda}\n"
        resum += f"Estat: {self.estat}\n"
        resum += "Productes:\n"
        for producte in self.productes.values():
            resum += f"- {producte.nom_producte}: {producte.quantitat} unitats \n"
        resum += f"Total de productes: {self.total_productes()}\n"
        return resum

    def modificar_estat(self, nou_estat):
        if nou_estat in self.ESTATS.values():
            self.estat = nou_estat
        else:
            raise ValueError(f"Estat no vàlid: {nou_estat}")

