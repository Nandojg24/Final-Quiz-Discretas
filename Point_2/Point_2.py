# Integrante 1: Juan Fernando Jimenez Garcia - 202459394
# Docente: Luis Germán Toro Pareja.
# Número de grupo:52
# Final Quiz
import re


# Function to read the file
def read_file():
    global content
    # We use global to make content accessible for all functions
    with (open("Point_2/Rules.txt", mode="r", encoding="utf-8")
          as file):
        content = file.read()


def words_1(txt):
    # This pattern searches for any word that starts with "ac"
    # and ends with "a" or "s"
    pattern = r"\bac\w*(?:a|s)\b"
    first_rule = re.findall(pattern, txt, flags=re.IGNORECASE)
    return first_rule


def words_2(txt):
    # Words ending with "n" or "s" or "d"
    pattern = r"\b\w*[nsd]\b"
    second_rule = re.findall(pattern, txt, flags=re.IGNORECASE)
    return second_rule


def words_3(txt):
    # Words starting with capital letter and having at least one vowel
    pattern = r"\b[A-Z]\w*[aeiouáéíóíú]\w*\b"
    third_rule = re.findall(pattern, txt)
    return third_rule


def words_4(txt):
    # Words that have all the vowels with or without accents
    pattern = r"\b(?=\w*[aá])(?=\w*[eé])(?=\w*[ií])(?=\w*[oó])(?=\w*[uú])\w+\b"
    fourth_rule = re.findall(pattern, txt, flags=re.IGNORECASE)
    return fourth_rule


def words_5(txt):
    # Words that have any vowel with an accents
    pattern = r"\b\w*[áéíóúÁÉÍÓÚ]\w*\b"
    fifth_rule = re.findall(pattern, txt, flags=re.IGNORECASE)
    return fifth_rule


def there_is_something_6(txt):
    # Sentences that have an exclamation or interrogative mark
    pattern = r"(\¡.+?\!)|(\¿.+?\?)|(?:[¿¡]{1,2}.+?[!?]{1,2})"
    sixth_rule = re.findall(pattern, txt, flags=re.IGNORECASE)
    return sixth_rule


def abbreviations_7(txt):
    # Abbreviations in general
    pattern = r"\b(?:[A-Za-z]{1,4}\.)\b"
    seventh_rule = re.findall(pattern, txt, flags=re.IGNORECASE)
    return seventh_rule


def words_8(txt):
    # Words that use the @ symbol
    pattern = r"\b\w*@\w*\b"
    eighth_rule = re.findall(pattern, txt, flags=re.IGNORECASE)
    return eighth_rule


def what_we_found():
    # This function will use the functions to get the lens
    # of all the other, and start the program
    read_file()
    words1 = words_1(content)
    words2 = words_2(content)
    words3 = words_3(content)
    words4 = words_4(content)
    words5 = words_5(content)
    sentences6 = there_is_something_6(content)
    words7 = abbreviations_7(content)
    words8 = words_8(content)

    print("########################### " "Results that what we fund "
          "###########################\n")

    if len(words1) > 0:
        print("Words that start with 'ac' and end with 'a' or 's':"
              f"{len(words1)}")
        print("Words found:")
        for word in words1:
            print(word)
    else:
        print("-----"*20)
        print("No words found that start with 'ac' and end with 'a' or 's'.")

    if len(words2) > 0:
        print("-----"*20)
        print("\nWords that end with 'n', 's' or 'd':"
              f"{len(words2)}")
        print("Words found:")
        for word in words2:
            print(word)
    else:
        print("-----"*20)
        print("No words found that end with 'n', 's' or 'd'.")

    if len(words3) > 0:
        print("-----"*20)
        print("\nWords that start with a capital "
              "letter and have at least one vowel:"
              f"{len(words3)}")
        print("Words found:")
        for word in words3:
            print(word)
    else:
        print("-----"*20)
        print("No words found that start with a capital "
              "letter and have at least one vowel.")

    if len(words4) > 0:
        print("-----"*20)
        print("\nWords that have all the vowels with or without accents:"
              f"{len(words4)}")
        print("Words found:")
        for word in words4:
            print(word)
    else:
        print("-----"*20)
        print("No words found that have all "
              "the vowels with or without accents.")

    if len(words5) > 0:
        print("-----"*20)
        print("\nWords that have any vowel with an accent:"
              f"{len(words5)}")
        print("Words found:")
        for word in words5:
            print(word)
    else:
        print("-----"*20)
        print("No words found that have any vowel with an accent.")

    if len(sentences6) > 0:
        print("-----"*20)
        print("\nSentences that have an exclamation or interrogative mark:"
              f"{len(sentences6)}")
        print("Sentences found:")
        for sentence in sentences6:
            print(sentence[0] if sentence[0] else sentence[1])
    else:
        print("-----"*20)
        print("No sentences found that have an exclamation "
              "or interrogative mark.")

    if len(words7) > 0:
        print("-----"*20)
        print("\nAbbreviations found:"
              f"{len(words7)}")
        print("Abbreviations found:")
        for abbreviation in words7:
            print(abbreviation)
    else:
        print("-----"*20)
        print("No abbreviations found in the text.")

    if len(words8) > 0:
        print("-----"*20)
        print("\nWords that use the @ symbol:"
              f"{len(words8)}")
        print("Words found:")
        for word in words8:
            print(word)
            print("\n")
    else:
        print("-----"*20)
        print("No words found that use the @ symbol.")
        print("-----"*20)


if __name__ == "__main__":
    what_we_found()
