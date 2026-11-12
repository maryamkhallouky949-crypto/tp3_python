
class Document:
    def __init__(self, titre, annee):
        self.titre = titre
        self.annee = annee

    def afficher(self):
        print(f"{self.titre} ({self.annee})")

    def est_recent(self):
        return self.annee >= 2020


class Livre(Document):
    def __init__(self, titre, annee, auteur):
        super().__init__(titre, annee)
        self.auteur = auteur

    def afficher(self):
        print(
            f"Livre: {self.titre} par {self.auteur} "
            f"({self.annee})"
        )


class Magazine(Document):
    def __init__(self, titre, annee, numero):
        super().__init__(titre, annee)
        self.numero = numero

    def afficher(self):
        print(
            f"Magazine: {self.titre} No. {self.numero} "
            f"({self.annee})"
        )


if __name__ == "__main__":
    docs = [
        Livre("1984", 1948, "George Orwell"),
        Magazine("Science & Vie", 2025, 455),
        Livre("Le Petit Prince", 1943, "Antoine de Saint-Exupéry")
    ]

    for d in docs:
        d.afficher()

    print("Vérification des documents récents :")

    for d in docs:
        print(d.titre, ":", d.est_recent())
