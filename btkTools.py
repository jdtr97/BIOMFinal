# -*- coding: utf-8 -*-
"""
@autor: Eng. Alexander Sierra, Assistant Professor
"""
import numpy as np
import logging
import btk


# ----- acquisition -----
def smartReader(filename):
    """
    Function to read a c3d file with BTK.
    :param filename: (str) path and filename of the c3d
    :return: (btkAcquisition) btk Acquisition instance
    """
    reader = btk.btkAcquisitionFileReader()
    reader.SetFilename(filename)
    reader.Update()
    acq = reader.GetOutput()
    return acq


def smartWriter(acq, filename):
    """Function to write a c3d file with BTK.
        :parameters:
            `acq` : (btkAcquisition) a btk Acquisition instance
            `filename` : path and filename of the c3d
        :return:
            None
        """
    writer = btk.btkAcquisitionFileWriter()
    writer.SetInput(acq)
    writer.SetFilename(str(filename))
    writer.Update()


def GetMarkerNames(acq):
    """Function to show point's label on acquisition.
            :parameter:
                `acq` : (btkAcquisition) a btk acquisition instance
            :return:
                `marker_names` : (list) marker names
            :todo: regex
    """
    marker_names = list()
    for it in btk.Iterate(acq.GetPoints()):
        if it.GetType() == btk.btkPoint.Marker and it.GetLabel()[0] != "*":
            marker_names.append(it.GetLabel())
    return marker_names


def isGap(acq, markerLabel):
    """ Helper function to check if is there a gap.
        :parameters:
            `acq` : (btkAcquisition) a btk acquisition instance
            `markerLabel` : (str) marker's label
        :return:
            True : (bool) if there is a gap on specific marker
    """
    residual_values = acq.GetPoint(markerLabel).GetResiduals()
    if np.any(residual_values == -1.0):
        logging.warning("Gap found for marker (%s)" % markerLabel)
        return True
    else:
        return False


def findMarkerGap(acq):
    """
    Function to find markers with Gap in a list of markers
    :param acq: (btkAcquisition) btk acquisition instance
    :return: list of markers with gaps
    """
    gaps = list()
    markerNames = GetMarkerNames(acq)
    for marker in markerNames:
        if isGap(acq, marker):
            gaps.append(marker)
    return gaps


def smartAppendPoint(acq, label, values,
                     pointType=btk.btkPoint.Marker, desc="",
                     residuals=None):
    """
    Function to append a point into an acquisition object.
    :param acq: (btkAcquisition) btk Acquisition instance
    :param label: (str) point's label
    :param values: (ndarray(n, 3)) point's values
    :param pointType: (enums of btkPoint) type of Point
    :param residuals:
    :return: None
    """
    values = np.nan_to_num(values)

    if residuals is None:
        residuals = np.zeros((values.shape[0], 1))
        for i in np.arange(values.shape[0]):
            if np.all(values[i, :] == 0.0):
                residuals[i] = -1.0

    new_btkPoint = btk.btkPoint(label, acq.GetPointFrameNumber())
    new_btkPoint.SetValues(values)
    new_btkPoint.SetDescription(desc)
    new_btkPoint.SetType(pointType)
    new_btkPoint.SetResiduals(residuals)
    acq.AppendPoint(new_btkPoint)


def constructEmptyMarker(acq, label, desc=""):
    """
    Function to build an empty marker.
    :param acq: (btkAcquisition) btk Acquisition instance
    :param label: (str) marker's label
    :param desc: (str) "short description"
    :return: None
    """
    nFrames = acq.GetPointFrameNumber()
    values = np.zeros((nFrames, 3))
    residualValues = np.full((nFrames, 1), -1.0)
    smartAppendPoint(acq, label, values, desc=desc, residuals=residualValues)
    logging.debug("built " + label)


# ----- Events -----

def _GetEvents(acq):
    """
    Helper function to read and sort the event collection from an acq object
    :param acq: (btkAcquisition)
    :return: (list) List of btkEvent objects
    """
    event_list = [event for event in btk.Iterate(acq.GetEvents())]
    event_list.sort(key=lambda i:i.GetFrame())
    return  event_list

def get_events(acq, context):
    """
    Function to read the event's frame by context
    :param acq: (btkAcquisition) btk Acquisition instance
    :param context: (string) 'Right', 'Left' or 'General'
    :return: (tuple) Foot Strike list and Foot Off list
    """
    footStrike = []
    footOff =  []

    for e in _GetEvents(acq):
        if e.GetContext() == context:
            if e.GetLabel() == 'Foot Strike':
                footStrike.append(e.GetFrame())
            if e.GetLabel() == 'Foot Off':
                footOff.append(e.GetFrame())
    return (footStrike, footOff)
