import re


def check_name(name: str):
    """ retourne False si name contient des caractères de ponctuation,
    des chiffres ou des caractères spéciaux"""
    if re.search(r"^[A-Za-z '-éèàîïùç]{2,}$", name):
        return False

