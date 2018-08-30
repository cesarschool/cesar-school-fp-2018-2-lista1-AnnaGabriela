## QUESTÃO 3 ##
# Escreva um programa que calcule a área de um círculo, o diâmetro e o comprimento 
# da circunferência. Solicite que o usuário insira o raio e imprima uma mensagem 
# agradável de volta para o usuário com a resposta. 
##

def main():
    PI = 3.14
    
    radius = float(input('Please input the circle radius: '))

    circleArea = PI * radius**2
    diameter = radius*2
    circunferenceLenght = 2*PI*radius

    print('With a radius of {}:'.format(radius))
    print('The circle area is {}'.format(circleArea))
    print('The diameter is {}'.format(diameter))
    print('The circunference lenght is {}'.format(circunferenceLenght))
    
    
if __name__ == '__main__':
    main()
