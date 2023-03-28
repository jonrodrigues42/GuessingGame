import random as rd

min = 0
max = 10
generated_number = rd.randint(min, max)
print("Será sorteado um número de 0 a 10. Você consegue acertar?")
print("---------------------------------")





# usernum = int(input("Qual é o número?"))
def main_game(n):
    attemps = 1
    win = False

    while not win:
        usern = int(input("Qual é o número?" ))
        if (usern >= min) and (usern <= max):
            if n == usern:
                print("Parabéns, você ganhou!")
                print(f"Você acertou o número {n} em {attemps} tentativas.")
                win = True
            elif n < usern:
                print("Ainda não, o número é MENOR")
                attemps += 1
            elif n > usern:
                print("Ainda não, o número é MAIOR")
                attemps += 1
        else:
            print("Número inválido")
    

main_game(generated_number)