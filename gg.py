import random as rd

def main_game():
    win = False
    attemps = 1
    min = 0

    dif = int(input(""""Escolha a dificuldade\n
        0 = Easy (0 - 10)
        1 = Normal (0 - 20)
        2 = Hard (0 - 50)
        3 = Insane (0 - 100)\n
    """))
    if dif == 0:
        max = 10
    elif dif == 1:
        max = 20
    elif dif == 2:
        max = 50
    elif dif == 3:
        max = 100
    else:
        print("Difculdade inválida")
        main_game()

    print(f"Será sorteado um número de {min} a {max}. Você consegue acertar?")
    print("---------------------------------\n\n")
    generated_number = rd.randint(min, max)

    while not win:
        usern = int(input("Qual é o número? "))
        if (usern >= min) and (usern <= max):
            if generated_number == usern:
                print("Parabéns, você ganhou!")
                print(f"Você acertou o número '{generated_number}' em {attemps} tentativas.")
                win = True
            elif generated_number < usern:
                print("Ainda não, o número é MENOR")
                attemps += 1
            elif generated_number > usern:
                print("Ainda não, o número é MAIOR")
                attemps += 1
        else:
            print("Número inválido")
    
    again = input("Jogar novamente? (S/N) ")
    if again.lower() == 's':
        main_game()
    else:
        print("Até mais!")
    
main_game()
