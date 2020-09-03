menu = """ Menu calculadora escoje una de las operacione
1 Sumar
2 Restar
3 Multiplicar
4 Dividir """
print (menu)
op = int(input("Digite el numero correspondiente a la operacion   :"))
numero1 = int(input("Digite numero 1 :"))
numero2 = int(input("Digite numero 2 :"))

def sumar():
    resultadosuma = numero1 + numero2
    print("el resultado es : ",resultadosuma)	
def restar():
    resultadorestar = numero1 - numero2
    print("el resultado es : ",resultadorestar)
def Multiplicacion():
    resultadomultiplica = numero1 * numero2
    print("el resultado es : ",resultadomultiplica)
def Division():
    if (numero1 == 0):
        print("error la Division con cero no se puede hacer")
    else:
        resultadodivision = numero1 / numero2
        print("el resultado es : ",resultadodivision)
		
def calculadorapython():	
    if(op == 1):
        sumar()
    elif(op == 2):
        restar()
    elif(op == 3):
        Multiplicacion()
    elif(op == 4):
        Division()

calculadorapython()
