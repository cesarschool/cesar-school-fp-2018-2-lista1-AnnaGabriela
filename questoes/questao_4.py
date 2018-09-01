## QUESTÃO 4 ##
# Escreva um programa que pergunte a quantidade de km percorridos por um carro 
# alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi 
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e 
# R$ 0,15 por km rodado.

def main():
    costPerDay = 60
    costPerKm = 0.15

    kmTravelled = float(input("How many km have been travelled? "))
    daysOfRent = int(input("How many days have been used? "))

    price = (daysOfRent * costPerDay) + (kmTravelled * costPerKm)

    print("For travelling {} km for {} days, you have spent ${}".format(kmTravelled, daysOfRent, price))


    
if __name__ == '__main__':
    main()
