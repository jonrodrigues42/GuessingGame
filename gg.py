import random as rd

min = 0
max = 10



def main_game(min, max):
    attemps = 1
    win = False

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
    

main_game(min, max)
again = input("Jogar novamente? (S/N) ")
if again.lower() == 's':
    main_game(min, max)
else:
    print("Até mais!")