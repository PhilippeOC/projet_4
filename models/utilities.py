import re


def check_name(name):
    """ retourne True si name contient des caractères de ponctuation,
    des chiffres ou des caractères spéciaux"""
    if re.search(r"[^A-Za-zàâäéèêëïîôöùûüÿç-]", name):
        return True


def main():
    tst = check_name('tot2_o')
    if tst:
        print("not ok:", tst)
    else:
        print("ok:", tst)


if __name__ == "__main__":
    main()
