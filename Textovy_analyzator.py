'''
Textovy_analyzator.py: první projekt do Engeto Online Python Akademie
author: Miroslav Kalík
email: mira.kalik@seznam.cz
discord: mira_47271
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
##############################################################################
registrovani_uzivatele = {"bob": "123", "ann": "pass123",
                          "mike": "password123", "liz": "pass123"}
zadane_jmeno = input("username: ")
zadane_heslo = input("password: ")

if zadane_jmeno in registrovani_uzivatele.keys():
    if zadane_heslo == registrovani_uzivatele[zadane_jmeno]:
        print(40 * "-")
        print(f"Welcome to the app, {zadane_jmeno}")
        print("We have 3 texts to be analyzed.")
        print(40 * "-")
        vybrany_text = input("Enter a number btw. 1 and 3 to select: ")

        if vybrany_text.isdigit():
            schvalena_volba = int(vybrany_text)

            if schvalena_volba > 0 and schvalena_volba < 4:
                vybrany_text = TEXTS[schvalena_volba - 1]
                delky_slov = []
                jednotlive_delky = []
                slova_kapitalky = []
                slova_velka = []
                slova_mala = []
                cisla = []

                # pocet slov by samozrejme sel jednoduse pricitat do nejakeho
                # integeru,ale takto mi to prijde elegantnejsi a slova jsou
                # pripravena k dalsimu zpracovani :-)

                vybrany_text = vybrany_text.replace("\n", " ")
                vybrany_text = vybrany_text.strip()
                neprijatelne_znaky = [".", ",", "!", "?", "-"]
                for i in neprijatelne_znaky:
                    vybrany_text = vybrany_text.replace(i, "")

                seznam_slov = vybrany_text.split(" ")

                for slovo in seznam_slov:
                    delky_slov.append(len(slovo))
                    if slovo.istitle():
                        slova_kapitalky.append(slovo)
                    elif slovo.isupper():
                        slova_velka.append(slovo)
                    elif slovo.islower():
                        slova_mala.append(slovo)
                    elif slovo.isdigit():
                        cisla.append(int(slovo))

                print(40 * "-")
                print(f"There are {len(seznam_slov)} words in the selected "
                      f"text.")
                print(f"There are {len(slova_kapitalky)} titlecase words.")
                print(f"There are {len(slova_velka)} uppercase words.")
                print(f"There are {len(slova_mala)} lowercase words.")
                print(f"There are {len(cisla)} numeric strings.")
                print(f"The sum of all the numbers {sum(cisla)}")
                print(40 * "-")

                # GRAF
                for x in range(min(delky_slov), max(delky_slov) + 1):
                    jednotlive_delky.append(delky_slov.count(x))
                delka_radku = max(jednotlive_delky) + 2

                print("LEN|" + "  " + "OCCURENCES" + (delka_radku - 12) * " "
                      + "|NR.")
                print(40 * "-")

                for y in range(min(delky_slov), max(delky_slov) + 1):
                    mezera = delka_radku - delky_slov.count(y)
                    print((3 - len(str(y))) * " " + str(y) + "|" +
                          (delky_slov.count(y)) * "*" + mezera * " " + "|" +
                          str(delky_slov.count(y)))

            else:
                print("wrong select, terminating the program..")
        else:
            print("wrong select, terminating the program..")
    else:
        print("wrong password, terminating the program.. ")
else:
    print("unregistered user, terminating the program..")

