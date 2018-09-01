## QUESTÃO 1 ## 
# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o 
# valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do 
# novo salário. 
##

def main():
    salary = float(input("Type your salary: "))
    payrise = float(input("Type the pay rise percentage: "))

    newSalary = salary + (salary*(payrise/100))

    print("Your pay rise was {}% and your new salary is ${}".format(payrise, newSalary))
    


if __name__ == '__main__':
    main()