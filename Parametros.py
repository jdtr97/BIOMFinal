"""
@autors:
    Eng(S). Juan David Tovar Ramos
    Eng(S). Juan Manuel Puentes Sayo
    Eng(S). Maria Jose Gonzales Ruiz
"""

import btk
import numpy as np
from btkTools import *
from FuntionsBIOM import *

def Principal(DataIn, DatosReales):
    Reg = StringToChart(DataIn)
    Reg = int(Reg[16])
    DatosReales = DatosReales[:,Reg-1]
    acq = smartReader(DataIn)
    ff = acq.GetFirstFrame()
    ErrorGeneral = []
    left_fs = np.array(get_events(acq,'Left')[0])#[FS]
    left_to = np.array(get_events(acq,'Left')[1])#[TO]
    right_fs = np.array(get_events(acq,'Right')[0])#[FS]
    right_to = np.array(get_events(acq,'Right')[1])#[TO]
    lhee = acq.GetPoint("LHEE").GetValues() # Left heel strike
    ltoe = acq.GetPoint("LTOE").GetValues() # Left toe off
    rhee = acq.GetPoint("RHEE").GetValues() # adquisición del golpe de talón derecho
    rtoe = acq.GetPoint("RTOE").GetValues() # Right toe off
    x = ParameterCorrection(rhee)
    lhee = Correction(lhee,x)
    ltoe = Correction(ltoe,x)
    rhee = Correction(rhee,x)
    rtoe = Correction(rtoe,x)

    # Fix Events
    left_fs = np.array(FixEvents(left_fs, ff))
    left_to = np.array(FixEvents(left_to, ff))
    right_fs = np.array(FixEvents(right_fs, ff))
    right_to = np.array(FixEvents(right_to, ff))
    [lhsaux, rhsaux] = MatrixCorrection(lhee[left_fs], rhee[right_fs])
    #Stride Time -------------------------------------------------------------
    #left
    [StrideTime_Left, Error] = MeanData(left_fs, left_fs, DatosReales[0])
    ErrorGeneral.append(Error)
    #right
    [StrideTime_Right, Error] = MeanData(right_fs, right_fs, DatosReales[1])
    ErrorGeneral.append(Error)
    #Step Time ---------------------------------------------------------------
    #left
    [StepTime_Left, Error] = MeanData(right_fs, left_fs, DatosReales[2])
    ErrorGeneral.append(Error)
    #right
    [StepTime_Right, Error] = MeanData(left_fs, right_fs, DatosReales[3])
    ErrorGeneral.append(Error)
    #Stance Time -------------------------------------------------------------
    #left
    [StanceTime_Left, Error] = MeanData(Concatenar(left_fs,left_to),Concatenar(left_fs,left_to),1)
    #right
    [StanceTime_Righ, Error] = MeanData(Concatenar(right_fs,right_to),Concatenar(right_fs,right_to),1)
    #Swing Time --------------------------------------------------------------
    #left
    [SwingTime_Left, Error] = MeanData(left_fs, left_fs, 1)
    #right
    [SwingTime_Right, Error] = MeanData(right_fs, right_fs, 1)
    #Stride Lenght -----------------------------------------------------------
    #left
    [StrideLenght_Left, Error] = StrideLenght(lhsaux, DatosReales[4])
    ErrorGeneral.append(Error)
    #right
    [StrideLenght_Right, Error] = StrideLenght(rhsaux, DatosReales[5])
    ErrorGeneral.append(Error)
    #Step Lenght -------------------------------------------------------------
    #left
    [StepLenght_Left, Error] = StepLenght(lhsaux, rhsaux,DatosReales[6])
    ErrorGeneral.append(Error)
    #right
    [StepLenght_Right, Error] = StepLenght(rhsaux, lhsaux,DatosReales[7])
    ErrorGeneral.append(Error)
    #Step Width --------------------------------------------------------------
    #left
    [StepWidth_Left, Error] = StepWidth(StepLenght_Left,DatosReales[8])
    ErrorGeneral.append(Error)
    #right
    [StepWidth_Right, Error] = StepWidth(StepLenght_Right,DatosReales[9])
    ErrorGeneral.append(Error)
    return(StrideTime_Left, StrideTime_Right, StepTime_Left, StepTime_Right, StanceTime_Left,
    StanceTime_Righ, SwingTime_Left, SwingTime_Right, StrideLenght_Left, StrideLenght_Right,
    StepLenght_Left, StepLenght_Right, StepWidth_Left, StepWidth_Right, ErrorGeneral)
