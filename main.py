import csv

FILENAME = "listes.csv"


def read_data(filename):
    """Retourne le contenu du fichier <filename> sous forme de liste de listes d'entiers.

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 liste par ligne)
    """
    data = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                int_row = list(map(int, row))
                data.append(int_row)
    except FileNotFoundError:
        print(f"Erreur : le fichier {filename} est introuvable.")
    except ValueError:
        print(f"Erreur : le fichier {filename} contient des valeurs non entières.")
    return data

def get_list_k(data, k):
    """Retourne la k-ième liste dans <data>.

    Args:
        data (list): liste de listes d'entiers
        k (int): indice de la liste à retourner

    Returns:
        list: la k-ième liste si elle existe, sinon None
    """
    if 0 <= k < len(data):
        return data[k]
    else:
        print(f"Erreur : indice {k} hors de portée.")
        return None

def get_first(l):
    """Retourne le premier élément de la liste <l>.

    Args:
        l (list): liste d'entiers

    Returns:
        int: premier élément de <l>
    """
    return l[0] if l else None

def get_last(l):
    """Retourne le dernier élément de la liste <l>.

    Args:
        l (list): liste d'entiers

    Returns:
        int: dernier élément de <l>
    """
    return l[-1] if l else None

def get_max(l):
    """Retourne le maximum de la liste <l>.

    Args:
        l (list): liste d'entiers

    Returns:
        int: valeur maximale de <l>
    """
    return max(l) if l else None

def get_min(l):
    """Retourne le minimum de la liste <l>.

    Args:
        l (list): liste d'entiers

    Returns:
        int: valeur minimale de <l>
    """
    return min(l) if l else None

def get_sum(l):
    """Retourne la somme des éléments de la liste <l>.

    Args:
        l (list): liste d'entiers

    Returns:
        int: somme des éléments de <l>
    """
    return sum(l) if l else None



def main():
    data = read_data(FILENAME)
    if not data:
        print("Aucune donnée n'a été lue.")
        return

    print("Données lues depuis le fichier :")
    for i, l in enumerate(data):
        print(f"Ligne {i}: {l}")

    k = 1
    if len(data) > k:
        print(f"\nListe à l'indice {k} :", get_list_k(data, k))
        print("Premier élément :", get_first(data[k]))
        print("Dernier élément :", get_last(data[k]))
        print("Max :", get_max(data[k]))
        print("Min :", get_min(data[k]))
        print("Somme :", get_sum(data[k]))
    else:
        print(f"Aucune liste disponible à l'indice {k}.")

if __name__ == "__main__":
    main()
