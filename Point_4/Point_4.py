# Integrante 1: Juan Fernando Jimenez Garcia - 202459394
# Docente: Luis Germán Toro Pareja.
# Número de grupo:52
# Final Quiz
import re


def validate_credentials(username, password):
    validation = 0
    if len(username) == 7 and re.fullmatch(r"^([0-1]\d{6}|2[0-5]\d{5})",
                                           username):
        return validation + 1
    else:
        return validation
    if len(password) == 9 and re.match(r"^([a-zA-Z]{2})" +
                                       re.escape(username) + "$", password):
        return validation + 1
    if validation == 2:
        return True
    else:
        return False


if __name__ == "__main__":
    pass
