# -*- coding: utf-8 -*-
"""
@autors:
    Eng(S). Juan David Tovar Ramos
    Eng(S). Juan Manuel Puentes Sayo
    Eng(S). Maria Jose Gonzales Ruiz
"""

import numpy as np

def MeanDataFrame(DataIn1, DataIn2):
    DataOut = []
    if DataIn1.tolist() == DataIn2.tolist():
        for x in range(DataIn1.shape[0]-1):
            DataOut.append(DataIn1[x+1]-DataIn1[x])
        DataOut = np.array(DataOut)
    else:
        for x in range(DataIn1.shape[0]-1):
            DataOut.append(DataIn1[x]-DataIn2[x])
        DataOut = np.array(DataOut)
    return DataOut

def MeanData(DataIn1, DataIn2, DatoReal):
    DataOut = (abs(np.mean(MeanDataFrame(DataIn1,DataIn2))))/100
    Error = abs((DataOut-DatoReal)/DatoReal)*100
    return DataOut, Error

def Concatenar(DataIn1, DataIn2):
    Temp = []
    if (DataIn1.shape[0]-DataIn2.shape[0])<0:
        DataIn2 = DataIn2[0:(DataIn1.shape[0]-1)]
    elif (DataIn1.shape[0]-DataIn2.shape[0])>0:
        DataIn1 = DataIn1[0:(DataIn2.shape[0]-1)]
    else:
        DataIn1 = DataIn1
        DataIn2 = DataIn2

    if DataIn1[0]-DataIn2[0]<0:
        for x in range(DataIn1.shape[0]-1):
            Temp.append(DataIn1[x])
            Temp.append(DataIn2[x])
    else:
        for x in range(DataIn1.shape[0]-1):
            Temp.append(DataIn2[x])
            Temp.append(DataIn1[x])
    Temp = np.array(Temp)
    return Temp

def ParameterCorrection(DataIn):
    if DataIn[0,1] < 0:
        x=-1
    else:
        x=1
    return x

def Correction(DataIn,Parameter):
    DataIn = np.array(DataIn)
    DataOut = DataIn*Parameter
    return DataOut

def StringToChart(string):
    list1=[]
    list1[:0]=string
    return list1

def FixEvents(DataIn, ff):
    DataOut = [vc - ff for vc in DataIn]
    return DataOut

def sumalista(listaNumeros):
    laSuma = 0
    for i in listaNumeros:
        laSuma = laSuma + i
    return laSuma

def Recorrer(DataIn):
  Suma = []
  x = int((DataIn.shape[0]/2))
  for vc in range (x):
    Suma.append((DataIn[vc] - DataIn[vc+x])**2)
  Suma = (np.sqrt(sumalista(Suma)))/1000
  return Suma
def StrideLenght(DataIn, DatoReal):
  Parameter = DataIn.shape[0]
  DataOut = []
  for vc in range (Parameter-1):
    DataOut.append(Recorrer(np.concatenate((DataIn[vc,:],DataIn[(vc+1),:]),axis=0)))
  DataOut = np.mean(np.array(DataOut))
  Error = abs((DataOut-DatoReal)/DatoReal)*100
  return DataOut, Error

def MatrixCorrection(DataIn1,DataIn2):
  if DataIn1.shape[0]!=DataIn2.shape[0]:
    if DataIn1.shape[0]<DataIn2.shape[0]:
      DataIn2 = DataIn2[0:DataIn1.shape[0],:]
    else:
      DataIn1 = DataIn1[0:DataIn2.shape[0],:]
  if DataIn1.shape[1]!=DataIn2.shape[1]:
    if DataIn1.shape[1]<DataIn2.shape[1]:
      DataIn2 = DataIn2[:,0:DataIn1.shape[1]]
    else:
      DataIn1 = DataIn1[:,0:DataIn2.shape[1]]
  return DataIn1,DataIn2

def StepLenght(DataIn1,DataIn2,DatoReal):
  DataOut = []
  aux = DataIn1.shape[0]
  for vc in range(aux-1):
    aux1 = DataIn1[vc+1] - DataIn1[vc]
    aux2 = DataIn1[vc] - DataIn2[vc]
    aux = np.dot(aux1,aux2)/np.linalg.norm(aux1)
    DataOut.append(abs(aux)/1000)
  DataOut = np.mean(np.array(DataOut))
  Error = abs((DataOut-DatoReal)/DatoReal)*100
  return DataOut, Error

def StepWidth(DataIn,DatoReal):
    DataOut = DataIn/4
    Error = abs((DataOut-DatoReal)/DatoReal)*100
    return DataOut, Error
