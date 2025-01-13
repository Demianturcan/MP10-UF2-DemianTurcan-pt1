# gestio_erp/productes.py
class Producte:
    def __init__(self, id_producte, nom_producte, quantitat=0):
        self.id_producte = id_producte
        self.nom_producte = nom_producte
        self.quantitat = quantitat

    def __repr__(self):
        return (
            f"Producte ("
            f"id={self.id_producte}, "
            f"nom={self.nom_producte}, "
            f"quantitat={self.quantitat})"
        )