import numpy as np
import matplotlib.pyplot as plt
import math as math
from scipy.interpolate import lagrange

def puntoEnTriangulo (P1, P2, P3):
    return (P1[0] - P3[0]) * (P2[1] - P3[1]) - (P2[0] - P3[0]) * (P1[1] - P3[1]);
#endPuntoEnTriangulo

def calcularSegmentosAux(S1, S2, S, P1, P2, P3):

  for P4 in S:

    b1 = puntoEnTriangulo(P4, P1, P2) < 0.0;
    b2 = puntoEnTriangulo(P4, P2, P3) < 0.0;
    b3 = puntoEnTriangulo(P4, P3, P1) < 0.0;


    if (P1[0]!=P4[0] and P1[1]!=P4[1]) or (P2[0]!=P4[0] and P2[1]!=P4[1]) or (P3[0]!=P4[0] and P3[1]!=P4[1]):
      if not b1 and b2 and b3:
        S1.append(P4)
      elif not b2 and b1 and b3:
        S2.append(P4)


#endCalcularSegmentoS

def calcularSegmentos(S1, S2, puntos, x1, y1, x2, y2):
  if abs(x2-x1)>0:
    m=(y2-y1)/(x2-x1)
    b=y1-(m*x1)
    for punto in puntos:
      x=punto[0]
      y=punto[1]
      y_recta=m*x+b
      #w = "("+str(x)+", "+str(y)+"); y_recta: "+str(y_recta)
      #print(w)
      if y>=y_recta:
        S1.append(punto)
      else:
        S2.append(punto)
#endCalcularSegmentos
def algoritmoDividirConquistarAux(S, P, Q, R):

  if len(S)>0:
    area_max = -math.inf
    C  = []
    S1 = []
    S2 = []

    for c in S:
      PQ = []
      PC = []
      nPC = []
      x=c[0]
      y=c[1]

      PC.append(P[0]-x)
      PC.append(P[1]-y)
      PQ.append(P[0]-Q[0])
      PQ.append(P[1]-Q[1])

      nPC.append(PC[1])
      nPC.append(-PC[0])

      area_C = 0.5*abs((nPC[0]*PQ[0])+(nPC[1]*PQ[1]))

      #u = "C("+str(x)+", "+str(y)+"), area="+str(area_C)
      #print (u)
      if area_C > area_max:
        C = c
        area_max = area_C

    calcularSegmentosAux(S1, S2, S, P, C, Q)
    #w = str(S1) + " --- "+str(S2)
    #print(w)

    algoritmoDividirConquistarAux(S1, P, C, R)
    algoritmoDividirConquistarAux(S2, C, Q, R)

    if(len(C)>1):
      R.append(C)

#endDividirConquistarAux

def algoritmoDividirConquistar(puntos):
  if len(puntos)<=3:
      return puntos
  x_min = math.inf
  y_min = math.inf
  x_max = -math.inf
  y_max = -math.inf
  S1 = []
  S2 = []
  R  = []
  A = []
  B = []

  for punto in puntos:
    x=punto[0]
    y=punto[1]
    if x<=x_min and y<y_min:
      x_min = x
      y_min = y
    if x>=x_max and y>y_max:
      x_max = x
      y_max = y

  calcularSegmentos(S1, S2, puntos, x_min, y_min,x_max,y_max)

  A.append(x_min)
  A.append(y_min)
  B.append(x_max)
  B.append(y_max)
  R.append(A)
  R.append(B)

  #a = "\nmin("+str(x_min)+", "+str(y_min)+")\nmax("+str(x_max)+", "+str(y_max)+")\nS1="+str(S1)+"\nS2="+str(S2)
  #print(a)

  algoritmoDividirConquistarAux(S1, A, B, R)
  algoritmoDividirConquistarAux(S2, B, A, R)

  return R
#endDividirConquistar
def puntosCurva10():
    puntos=[]
    punto=[]
    punto.append(27.2)
    punto.append(2)
    puntos.append(punto)

    punto=[]
    punto.append(29)
    punto.append(2.13)
    puntos.append(punto)

    punto=[]
    punto.append(30)
    punto.append(3)
    puntos.append(punto)

    return puntos
#endPuntosCurva10
def puntosCurva9():
    puntos=[]
    punto=[]
    punto.append(19)
    punto.append(1.4)
    puntos.append(punto)
    punto=[]
    punto.append(26)
    punto.append(1.2)
    puntos.append(punto)

    punto=[]
    punto.append(27.2)
    punto.append(2)
    puntos.append(punto)

    return puntos
#endPuntosCurva
def puntosCurva8():
    puntos = []


    punto=[]
    punto.append(11)
    punto.append(1.8)
    puntos.append(punto)

    punto=[]
    punto.append(19)
    punto.append(1.4)
    puntos.append(punto)

    #print(puntos)
    return puntos

#endPuntosCurva8
def puntosCurva7():
    puntos = []


    punto=[]
    punto.append(7)
    punto.append(2.8)
    puntos.append(punto)

    punto=[]
    punto.append(8)
    punto.append(1.8)
    puntos.append(punto)

    punto=[]
    punto.append(9)
    punto.append(1.5)
    puntos.append(punto)

    punto=[]
    punto.append(11)
    punto.append(1.8)
    puntos.append(punto)

    #print("puntos7")
    #print(puntos)
    return puntos

#endPuntosCurva7
def puntosCurva6():
    puntos = []


    punto=[]
    punto.append(1)
    punto.append(3)
    puntos.append(punto)

    punto=[]
    punto.append(5)
    punto.append(2.9)
    puntos.append(punto)

    punto=[]
    punto.append(7)
    punto.append(2.8)
    puntos.append(punto)


    #print(puntos)
    return puntos

#endPuntosCurva6
def puntosCurva5():
    puntos = []
    punto=[]
    punto.append(27.5)
    punto.append(4.1)
    puntos.append(punto)

    punto=[]
    punto.append(28)
    punto.append(4.3)
    puntos.append(punto)

    punto=[]
    punto.append(29)
    punto.append(4.1)
    puntos.append(punto)


    punto=[]
    punto.append(30)
    punto.append(3)
    puntos.append(punto)

    #print(puntos)
    return puntos
#endPuntosCurva5
def puntosCurva4():
    puntos = []
    punto=[]
    punto.append(24.5)
    punto.append(5.97)
    puntos.append(punto)

    punto=[]
    punto.append(23.5)
    punto.append(5.85)
    puntos.append(punto)


    punto=[]
    punto.append(25)
    punto.append(6)
    puntos.append(punto)

    punto=[]
    punto.append(26.5)
    punto.append(5.58)
    puntos.append(punto)


    punto=[]
    punto.append(27.5)
    punto.append(4.1)
    puntos.append(punto)

    punto=[]
    punto.append(25.84)
    punto.append(5.9)
    puntos.append(punto)

    punto=[]
    punto.append(27.15)
    punto.append(4.97)
    puntos.append(punto)

    #print(puntos)
    return puntos
#endPuntosCurva4
def puntosCurva3():
    puntos = []
    punto=[]
    punto.append(20)
    punto.append(7.48)
    puntos.append(punto)

    punto=[]
    punto.append(16.65)
    punto.append(4.82)
    puntos.append(punto)

    punto=[]
    punto.append(23.5)
    punto.append(5.85)
    puntos.append(punto)

    punto=[]
    punto.append(17.36)
    punto.append(5.80)
    puntos.append(punto)

    punto=[]
    punto.append(18.15)
    punto.append(6.61)
    puntos.append(punto)

    punto=[]
    punto.append(19.06)
    punto.append(7.25)
    puntos.append(punto)

    punto=[]
    punto.append(21.11)
    punto.append(7.32)
    puntos.append(punto)

    punto=[]
    punto.append(22.02)
    punto.append(6.71)
    puntos.append(punto)
    #punto=[]
    #punto.append(24.5)
    #punto.append(5.97)
    #puntos.append(punto)

    #print(puntos)
    return puntos

#endPuntosCurva3
def puntosCurva2():
    puntos = []


    punto=[]
    punto.append(5)
    punto.append(3.9)
    puntos.append(punto)

    punto=[]
    punto.append(6)
    punto.append(4.5)
    puntos.append(punto)

    punto=[]
    punto.append(7.5)
    punto.append(6.19)
    puntos.append(punto)

    punto=[]
    punto.append(8.10)
    punto.append(6.69)
    puntos.append(punto)

    punto=[]
    punto.append(10)
    punto.append(7.40)
    puntos.append(punto)

    punto=[]
    punto.append(13)
    punto.append(6.7)
    puntos.append(punto)

    punto=[]
    punto.append(16.65)
    punto.append(4.82)
    puntos.append(punto)

    punto=[]
    punto.append(5.62)
    punto.append(4.16)
    puntos.append(punto)

    punto=[]
    punto.append(6.87)
    punto.append(5.43)
    puntos.append(punto)

    punto=[]
    punto.append(11.78)
    punto.append(7.24)
    puntos.append(punto)

    punto=[]
    punto.append(9.03)
    punto.append(7.13)
    puntos.append(punto)

    punto=[]
    punto.append(14.92)
    punto.append(5.78)
    puntos.append(punto)



    #print(puntos)
    return puntos

#endPuntosCurva2
def puntosCurva1():
    puntos = []

    punto=[]
    punto.append(5)
    punto.append(3.9)
    puntos.append(punto)

    punto=[]
    punto.append(1)
    punto.append(3)
    puntos.append(punto)

    punto=[]
    punto.append(2)
    punto.append(3.82)
    puntos.append(punto)

    punto=[]
    punto.append(1.14)
    punto.append(3.33)
    puntos.append(punto)

    punto=[]
    punto.append(1.49)
    punto.append(3.73)
    puntos.append(punto)

    punto=[]
    punto.append(2.41)
    punto.append(3.84)
    puntos.append(punto)

    punto=[]
    punto.append(2.88)
    punto.append(3.84)
    puntos.append(punto)

    punto=[]
    punto.append(3.36)
    punto.append(3.85)
    puntos.append(punto)

    punto=[]
    punto.append(3.75)
    punto.append(3.86)
    puntos.append(punto)

    punto=[]
    punto.append(4.42)
    punto.append(3.87)
    puntos.append(punto)



    #print(puntos)
    return puntos

#endPuntosCurva1
def limpiarPuntos(puntos):
    lista_nueva = []
    for i in puntos:
        if i not in lista_nueva:
            lista_nueva.append(i)
    return lista_nueva
    #print(str(len(puntos)))
#endInterpolacion
def graficar(puntosI1,puntosI2,puntosI3,puntosI4,puntosI5,puntosI6,puntosI7,puntosI8,puntosI9,puntosI10,puntosC1,puntosC2,puntosC3,puntosC4,puntosC5,puntosC6,puntosC7,puntosC8,puntosC9,puntosC10):
    #print("Inicia GRAFICAR")
    plt.figure(figsize=(13.5,2.5))
    plt.title('ejemplo perrito')
    x = []
    y = []
    for i in range(0,len(puntosC1)):
        x.append(puntosC1[i][0])
        y.append(puntosC1[i][1])

    #print("igualdad")
    p=lagrange(x,y)
    #print("despues de asignacion \n")
    print("-------------------------Errores Curva 1------------------------------")
    print("\n")
    print(p)
    print("\n")
    #print("--------")


    plt.plot(x,y,"+")
    x=np.linspace(1,5)
    plt.plot(x,p(x))
    for i in range(0,len(puntosI1)):
        error=((math.fabs(p(puntosI1[i][0])-puntosI1[i][1]))/(puntosI1[i][1]))*100
        print(puntosI1[i])
        print(round(error,4))
        print("\n")

    #x1=[5,8.1,10,13,17.6]
    #y1=[3.9,6.69,7.12,6.7,4.45]
    x1 = []
    y1 = []
    for i in range(0,len(puntosC2)):
        x1.append(puntosC2[i][0])
        y1.append(puntosC2[i][1])

    p1=lagrange(x1,y1)
    print("\nf(x):")
    print("-------------------------Errores Curva 2------------------------------")
    print("\n")
    print(p1)
    print("\n")

    plt.plot(x1,y1,"+")
    x1=np.linspace(5,16.65)
    plt.plot(x1,p1(x1))
    for i in range(0,len(puntosI2)):
        error=((math.fabs(p1(puntosI2[i][0])-puntosI2[i][1]))/(puntosI2[i][1]))*100
        print(puntosI2[i])
        print(round(error,4))
        print("\n")



    x2 = []
    y2 = []
    for i in range(0,len(puntosC3)):
        x2.append(puntosC3[i][0])
        y2.append(puntosC3[i][1])

    #x2=[17.6,20,23.5,24.5]
    #y2=[4.45,7,6.10,5.60]

    p2=lagrange(x2,y2)
    plt.plot(x2,y2,"+")
    x2=np.linspace(16.65,23.5)
    plt.plot(x2,p2(x2))
    print("-------------------------Errores Curva 3------------------------------")
    print("\n")
    print(p2)
    print("\n")
    for i in range(0,len(puntosI3)):
        error=((math.fabs(p2(puntosI3[i][0])-puntosI3[i][1]))/(puntosI3[i][1]))*100
        print(puntosI3[i])
        print(round(error,2))
        print("\n")



    x3 = []
    y3 = []
    #x3=[24.5,25,26.5,27.5]
    #y3=[5.6,5.87,5.15,4.10]
    for i in range(0,len(puntosC4)):
        x3.append(puntosC4[i][0])
        y3.append(puntosC4[i][1])

    p3=lagrange(x3,y3)
    plt.plot(x3,y3,"+")
    x3=np.linspace(23.5,27.5)
    plt.plot(x3,p3(x3))
    print("-------------------------Errores Curva 4------------------------------")
    print("\n")
    print(p3)
    print("\n")
    for i in range(0,len(puntosI4)):
        error=((math.fabs(p3(puntosI4[i][0])-puntosI4[i][1]))/(puntosI4[i][1]))*100
        print(puntosI4[i])
        print(round(error,2))
        print("\n")




    x4 = []
    y4 = []
    #x4=[27.5,28,29,30]
    #y4=[4.1,4.3,4.1,3]
    for i in range(0,len(puntosC5)):
        x4.append(puntosC5[i][0])
        y4.append(puntosC5[i][1])

    p4=lagrange(x4,y4)
    plt.plot(x4,y4,"+")
    x4=np.linspace(27.5,30)
    plt.plot(x4,p4(x4))
    print("-------------------------Errores Curva 5------------------------------")
    print("\n")
    print(p4)
    print("\n")
    for i in range(0,len(puntosI5)):
        error=((math.fabs(p4(puntosI5[i][0])-puntosI5[i][1]))/(puntosI5[i][1]))*100
        print(puntosI5[i])
        print(round(error,2))
        print("\n")
#A1ui inician las curvas inferiores
    x5 = []
    y5 = []
    #x5=[1,5,7]
    #y5=[3,2.9,2.8]
    for i in range(0,len(puntosC6)):
        x5.append(puntosC6[i][0])
        y5.append(puntosC6[i][1])

    p5=lagrange(x5,y5)
    plt.plot(x5,y5,"+")
    x5=np.linspace(1,7)
    plt.plot(x5,p5(x5))
    print("-------------------------Errores Curva 6------------------------------")
    print("\n")
    print(p5)
    print("\n")
    for i in range(0,len(puntosI6)):
        error=((math.fabs(p5(puntosI6[i][0])-puntosI6[i][1]))/(puntosI6[i][1]))*100
        print(puntosI6[i])
        print(round(error,2))
        print("\n")


    x6 = []
    y6 = []
    #x6=[7,8,9,11]
    #y6=[2.8,1.8,1.5,1.8]
    for i in range(0,len(puntosC7)):
        x6.append(puntosC7[i][0])
        y6.append(puntosC7[i][1])

    p6=lagrange(x6,y6)
    plt.plot(x6,y6,"+")
    x6=np.linspace(7,11)
    plt.plot(x6,p6(x6))
    print("-------------------------Errores Curva 7------------------------------")
    print("\n")
    print(p6)
    print("\n")
    for i in range(0,len(puntosI7)):
        error=((math.fabs(p6(puntosI7[i][0])-puntosI7[i][1]))/(puntosI7[i][1]))*100
        print(puntosI7[i])
        print(round(error,2))
        print("\n")


    x7 = []
    y7 = []
    #x7=[11,19]
    #y7=[1.8,1.4]
    for i in range(0,len(puntosC8)):
        x7.append(puntosC8[i][0])
        y7.append(puntosC8[i][1])

    p7=lagrange(x7,y7)
    plt.plot(x7,y7,"+")
    x7=np.linspace(11,19)
    plt.plot(x7,p7(x7))
    print("-------------------------Errores Curva 8------------------------------")
    print("\n")
    print(p7)
    print("\n")
    for i in range(0,len(puntosI8)):
        error=((math.fabs(p7(puntosI8[i][0])-puntosI8[i][1]))/(puntosI8[i][1]))*100
        print(puntosI8[i])
        print(round(error,2))
        print("\n")


    x8 = []
    y8 = []
    #x8=[19,26,27.2]
    #y8=[1.4,1.2,2]
    for i in range(0,len(puntosC9)):
        x8.append(puntosC9[i][0])
        y8.append(puntosC9[i][1])

    p8=lagrange(x8,y8)
    plt.plot(x8,y8,"+")
    x8=np.linspace(19,27.2)
    plt.plot(x8,p8(x8))
    print("-------------------------Errores Curva 9------------------------------")
    print("\n")
    print(p8)
    print("\n")
    for i in range(0,len(puntosI9)):
        error=((math.fabs(p8(puntosI9[i][0])-puntosI9[i][1]))/(puntosI9[i][1]))*100
        print(puntosI9[i])
        print(round(error,2))
        print("\n")


    x9 = []
    y9 = []
    #x9=[27.2,29,30]
    #y9=[2,2.13,3]
    for i in range(0,len(puntosC10)):
        x9.append(puntosC10[i][0])
        y9.append(puntosC10[i][1])

    p9=lagrange(x9,y9)
    plt.plot(x9,y9,"+")
    x9=np.linspace(27.2,30)
    plt.plot(x9,p9(x9))
    print("-------------------------Errores Curva 10------------------------------")
    print(p9)
    print("\n")
    for i in range(0,len(puntosI10)):
        error=((math.fabs(p9(puntosI10[i][0])-puntosI10[i][1]))/(puntosI10[i][1]))*100
        print(puntosI10[i])
        print(round(error,2))
        print("\n")

    plt.show()
#endGraficar
def invocarAlgoritmos():
    puntosI1 = puntosCurva1()
    puntosI2 = puntosCurva2()
    puntosI3 = puntosCurva3()
    puntosI4 = puntosCurva4()
    puntosI5 = puntosCurva5()
    puntosI6 = puntosCurva6()
    puntosI7 = puntosCurva7()
    puntosI8 = puntosCurva8()
    puntosI9 = puntosCurva9()
    puntosI10 = puntosCurva10()

    puntosC1 = algoritmoDividirConquistar(puntosCurva1())
    #puntosC1 = algoritmoDividirConquistar(puntosCurva1())
    #puntosC1 = puntosCurva1()
    #puntosC2 = puntosCurva2()
    puntosC3 = puntosCurva3()
    puntosC4 = puntosCurva4()
    #puntosC5 = puntosCurva5()
    puntosC2 = algoritmoDividirConquistar(puntosCurva2())
    #puntosC3 = algoritmoDividirConquistar(puntosCurva3())
    #puntosC4 = algoritmoDividirConquistar(puntosCurva4())
    puntosC5 = algoritmoDividirConquistar(puntosCurva5())
    puntosC6 = algoritmoDividirConquistar(puntosCurva6())
    puntosC7 = algoritmoDividirConquistar(puntosCurva7())
    puntosC7 =puntosCurva7()
    puntosC8 = algoritmoDividirConquistar(puntosCurva8())
    puntosC9 = algoritmoDividirConquistar(puntosCurva9())
    puntosC10 = algoritmoDividirConquistar(puntosCurva10())

    curva1 = "\nResultado Dividir y Conquistar:\n" + str(puntosC1)
    inicial1 = "\npuntos iniciales:\n"+str(puntosI1)
    #curva2 = "Resultado Dividir y Conquistar:\n" + str(puntosC2)
    #curva3 = "Resultado Dividir y Conquistar:\n" + str(puntosC3)
    #curva4 = "Resultado Dividir y Conquistar:\n" + str(puntosC4)
    #curva5 = "Resultado Dividir y conquistar:\n" + str(puntosC5)
    #print(curva1)
    #print(inicial1)
    #print(curva1)
    #print(curva2)
    #print(curva3)
    #print(curva4)
    #print(curva5)
    #print("desde aqui limpiar puntos")
    puntosC1=limpiarPuntos(puntosC1)
    puntosC2=limpiarPuntos(puntosC2)
    puntosC3=limpiarPuntos(puntosC3)
    puntosC4=limpiarPuntos(puntosC4)
    puntosC5=limpiarPuntos(puntosC5)
    puntosC6=limpiarPuntos(puntosC6)
    puntosC7=limpiarPuntos(puntosC7)
    puntosC8=limpiarPuntos(puntosC8)
    puntosC9=limpiarPuntos(puntosC9)
    puntosC10=limpiarPuntos(puntosC10)

    #print(puntosC1)
    #print(puntosC2)
    #print(puntosC3)
    #print(puntosC4)
    #print(puntosC5)
    graficar(puntosI1,puntosI2,puntosI3,puntosI4,puntosI5,puntosI6,puntosI7,puntosI8,puntosI9,puntosI10,puntosC1,puntosC2,puntosC3,puntosC4,puntosC5,puntosC6,puntosC7,puntosC8,puntosC9,puntosC10)


#endInvocarAlgoritmos

#x = np.linspace(0,15)
#y = np.piecewise(x, [x<5, x>=5 , x>10], [lambda x: x*x, lambda x: x, lambda x: x*x])

#plt.plot(x, y)
#plt.show()
invocarAlgoritmos()
