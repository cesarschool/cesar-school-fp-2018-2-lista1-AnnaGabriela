## QUESTÃO 5 ##
# Escreva um programa para calcular a redução do tempo de vida de um fumante. 
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
# Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule 
# quantos dias de vida um fumante perderá. Exiba o total em dias. 
##

def main():
    dayInMinutes = 1440
    minutesLostPerCigarette = 10
    daysPerYear = 365

    cigarettesPerDay = int(input("How many cigarettes do you smoke per day? "))
    yearsOfSmoking = int(input("For how many years have you been smoking? "))

    daysOfSmoking = yearsOfSmoking * daysPerYear
    totalCigarettesSmoked = cigarettesPerDay * daysOfSmoking
    daysLost = (totalCigarettesSmoked * minutesLostPerCigarette) // dayInMinutes

    print("By smoking {} cigarettes per day for {} years, you have lost approximately {} day(s) of your life."
        .format(cigarettesPerDay, yearsOfSmoking, daysLost))


    
if __name__ == '__main__':
    main()
