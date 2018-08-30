## QUESTÃO 2 ##
# Escreva um programa que converta uma temperatura digitada em °C (graus celsius) 
# para °F (graus fahrenheit). 
##

def main():
    celsius = int(input('Please input temperature in Celsius: '))

    fahrenheit = ((9*celsius)/5) + 32

    print('{}°C is {}°F'.format(celsius, fahrenheit))



if __name__ == '__main__':
    main()
