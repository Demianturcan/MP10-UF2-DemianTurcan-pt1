class Comanda:
    ESTATS = {
        "PENDENT": "pendent",
        "COMPLETADA": "completada",
    }

    def __init__(self, id_comanda, estat=ESTATS["PENDENT"]):
        self.id_comanda = id_comanda
        self.productes = {}
        self.quantitat = 0
        self.estat = estat

    def __repr__(self):
        return (
            f"Comanda {self.id_comanda} [{self.estat}]"
            f"quantitat={self.quantitat}, "
            f"productes={self.productes} )"
        )


    def afegir_producte(self, producte, quantitat=1):
        if producte in self.productes:
            self.productes[producte] += quantitat  # si el producte ja existeix augmentem la quantitat
        else:
            self.productes[producte] = quantitat  # si no afegim el producte amb la nova quantitat

    def total_productes(self):
        return sum(self.productes.values())  # retorna la quantitat total de productes a la comanda

    def resum_comanda(self):
        resum = f"Resum de la Comanda ID: {self.id_comanda}\n"
        resum += f"Estat: {self.estat}\n"
        resum += "Productes:\n"
        for producte, quantitat in self.productes.items():
            resum += f"- {producte.nom_producte}: {quantitat} unitats \n"
        resum += f"Total de productes: {self.total_productes()}\n"
        return resum

    def modificar_estat(self, nou_estat):
        if nou_estat in self.ESTATS.values():
            self.estat = nou_estat
        else:
            raise ValueError(f"Estat no vàlid: {nou_estat}")
