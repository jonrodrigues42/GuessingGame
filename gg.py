import random as rd

def main_game():
    win = False
    attemps = 1
    min = 0

    difin = (input(""""Escolha a dificuldade\n
        0 = Easy (0 - 10)
        1 = Normal (0 - 50)
        2 = Hard (0 - 100)
        3 = Insane (0 - 1.000)
        6 = Doom Slayer (0 - 100.000)\n"""))
    
    if difin.isdigit():
        dif = int(difin)
        if dif == 0:
            max = 10
        elif dif == 1:
            max = 50
        elif dif == 2:
            max = 100
        elif dif == 3:
            max = 1000
        elif dif == 6:
            max = 100000
        else:
            print("Difculdade inválida\n\n\n")
            main_game()
    else:
        print("Entrada inválida")
        main_game()

    print(f"Será sorteado um número de {min} a {max}. Você consegue acertar?")
    print("---------------------------------\n")
    generated_number = rd.randint(min, max)

    while not win:
        usernin = input("\nQual é o número? ")
        if usernin.isdigit():
            usern = int(usernin)
            if (usern >= min) and (usern <= max):
                if generated_number == usern:
                    print("\nParabéns, você ganhou!")
                    print(f"Você acertou o número '{generated_number}' em {attemps} tentativas.\n")
                    win = True
                elif generated_number < usern:
                    print("Ainda não, o número é << MENOR <<")
                    attemps += 1
                elif generated_number > usern:
                    print("Ainda não, o número é >> MAIOR >>")
                    attemps += 1
            else:
                print("Número inválido")
        else:
            print("Entrada inválida\n\n")
    
    again = input("\n\nJogar novamente? (S/N) ")
    if again.lower() == 's':
        main_game()
    else:
        print("Até mais!")
# end main game
    
main_game()
