import re


def check_name(name: str):
    """ retourne True si name contient des caractères de ponctuation,
    des chiffres ou des caractères spéciaux ou un seul caractère"""
    if re.search(r"^[A-Za-z '-éèàîïùç]{2,}$", name):
        return True
