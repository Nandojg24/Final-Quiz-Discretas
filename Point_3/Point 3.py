# Integrante 1: Juan Fernando Jimenez Garcia - 202459394
# Docente: Luis Germán Toro Pareja.
# Número de grupo:52
# Final Quiz
import re


# Function to read the file
def read_file():
    global content
    # We use global to make content accessible for all functions
    with (open("Point_3/Cybercrime_Info.txt", mode="r", encoding="utf-8")
          as file):
        content = file.read()


def there_is_a_question(txt):
    # This pattern searches for any sentence that starts with ¿ and ends with ?
    # or any sentence that ends with a question mark.
    # With this we ensure that we gonna find questions in spanish and english.
    pattern = r"(\¿.+?\?)|(.+?\?)"
    matched_questions = re.findall(pattern, txt, flags=re.IGNORECASE)
    return matched_questions


def there_is_a_exclamation(txt):
    # This pattern searches for any sentence that starts with ¡ and ends with !
    # or any sentence that ends with an exclamation mark.
    # With this we ensure that we gonna find exclamations in
    # spanish and english.
    pattern = r"(\¡.+?\!)|(.+?!)"
    matched_exclamations = re.findall(pattern, txt, flags=re.IGNORECASE)
    return matched_exclamations


def there_is_a_abbreviation(txt):
    # With this pattern we gonna search for the abbreviation that
    # we know have in the text. For an abbreciation we consider
    # a word that starts with a capital letter, followed by any
    # other lowercase letter, then an apostrophe and then lowercase letters,
    # or common abbreviations like Mr. or Mrs.,
    # also we gonna consider the common abbreviations that start
    # with a lowercase letter and ends with and apostrophe and t
    pattern = r"\b(?:[A-Z][a-z]*’(?:t|s|re|ll|ve|d)|Mr\.|Mrs\.|[a-z]*’t)\b"
    matched_abbreviations = re.findall(pattern, txt, flags=re.IGNORECASE)
    return matched_abbreviations


def what_we_found():
    # This function will use the functions to get the lens
    # of all the other, and start the program
    questions = there_is_a_question(content)
    exclamations = there_is_a_exclamation(content)
    abbreviations = there_is_a_abbreviation(content)

    print("########################### " "Results that what we fund "
          "###########################\n")

    if len(questions) == 0:
        # If no questions are found, we print a message
        # indicating that there are no questions in the text.
        print("No questions found in the text.")
    else:
        # If questions are found, we print a message
        # showing the total number of questions found
        print(f"Total questions found in the text: {len(questions)}\n")

    print("Questions found:")
    # we print every question that we found in the text,
    # we got the questions in a list of tuples,
    # so we print the first element of the tuple if it exists,
    # otherwise we print the second element of the tuple.
    for q in questions:
        print(q[0] if q[0] else q[1])

    if len(exclamations) == 0:
        # If no exclamations are found, we print a message
        # indicating that there are no exclamations in the text.
        print("\nNo exclamations found in the text.")
    else:
        # If exclamations are found, we print a message
        # showing the total number of exclamation found
        print(f"Total exclamations found in the text: {len(exclamations)}\n")

    print("\nExclamations found:")
    # we print every exclamation that we found in the text,
    # we got the exclamation in a list of tuples,
    # so we print the first element of the tuple if it exists,
    # otherwise we print the second element of the tuple.
    for e in exclamations:
        print(e[0] if e[0] else e[1])

    if len(abbreviations) == 0:
        print("\nNo abbreviations found in the text.")
    else:
        print(f"Total abbreviations found in the text: {len(abbreviations)}\n")

    print("\nAbbreviations found:")
    for a in abbreviations:
        print(a)


if __name__ == "__main__":
    read_file()
    what_we_found()
    print("\n###########################"+" End of the program " +
          "###########################")
