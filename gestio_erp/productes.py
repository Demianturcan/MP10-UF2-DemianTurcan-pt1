class Producte:
    def __init__(self, id_producte, nom_producte):
        self.nom_producte = nom_producte,
        self.id_producte = id_producte

    def __repr__(self):
        return (
                f"Producte ("
                f"id={self.id_producte}, "
                f"nom={self.nom_producte},)"
                )


