"""
@autors:
    Eng(S). Juan David Tovar Ramos
    Eng(S). Juan Manuel Puentes Sayo
    Eng(S). Maria Jose Gonzales Ruiz
"""

import sys
import numpy as np
import pandas as pd
from Parametros import *

DatosReales = np.array(pd.read_csv('Participante44.csv', sep=',',header=None))
registro = "02" #Poner el NUMERO de REGISTRO
prueba = "Participante44_"+registro+".c3d"

Nombres = []
## Load data
if __name__ == '__main__':
    for vc in sys.argv:
        Nombres.append(vc)
for vc in range(len(Nombres)-1):
    prueba = Nombres[vc+1]
    [StrideTime_Left, StrideTime_Right, StepTime_Left, StepTime_Right, StanceTime_Left,
    StanceTime_Right, SwingTime_Left, SwingTime_Right, StrideLenght_Left, StrideLenght_Right,
    StepLenght_Left, StepLenght_Right, StepWidth_Left, StepWidth_Right,
    ErrorGeneral] = Principal(prueba, DatosReales)
    print("--------------------------------------------")
    print("|    Parametros espaciales y temporales    |")
    print("--------------------------------------------")
    print("|           "+prueba+"          |")
    print("--------------------------------------------")
    print("Parameter - Left - Right  - Units - Error(%)")
    print("--------------------------------------------")
    print("............................................")
    print('Stride Time - '+str(round(StrideTime_Left,3))+' - '+str(round(StrideTime_Right,3))+' - Seg - '+str(round((ErrorGeneral[0]+ErrorGeneral[1])/2,1)))
    print("............................................")
    print('Step Time - '+str(round(StepTime_Left,3))+' - '+str(round(StepTime_Right,3))+' - Seg - '+str(round((ErrorGeneral[2]+ErrorGeneral[3])/2,1)))
    print("............................................")
    print('Stance Time - '+str(round(StanceTime_Left,3))+' - '+str(round(StanceTime_Right,3))+' - Seg - /')
    print("............................................")
    print('Swing Time - '+str(round(SwingTime_Left,3))+' - '+str(round(SwingTime_Right,3))+' - Seg - /')
    print("............................................")
    print('Swing Lenght - '+str(round(StrideLenght_Left,3))+' - '+str(round(StrideLenght_Right,3))+' - m - '+str(round((ErrorGeneral[4]+ErrorGeneral[5])/2,1)))
    print("............................................")
    print('Step Lenght - '+str(round(StepLenght_Left,3))+' - '+str(round(StepLenght_Right,3))+' - m - '+str(round((ErrorGeneral[6]+ErrorGeneral[7])/2,1)))
    print("............................................")
    print('Step Width - '+str(round(StepWidth_Left,3))+' - '+str(round(StepWidth_Right,3))+' - m - '+str(round((ErrorGeneral[8]+ErrorGeneral[9])/2,1)))
    print("--------------------------------------------")
    print("|     El error promedio fue de: "+str(round((np.mean(np.array(ErrorGeneral))),2))+" %     |")
    print("--------------------------------------------")
