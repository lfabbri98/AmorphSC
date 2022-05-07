import pandas as pd
from scipy.integrate import cumtrapz
import numpy as np
import matplotlib.pyplot as plt

def calculate_capacitance(current, frequency, V_out, W, L, n_tft=500):
    """
    Function that calculates capacitance from I-V data recorded. Since data are
    acquired as AC signal then C = I/(2*pi*f*V_out)

    Parameters
    ----------
    current : float
        Current value registered from lock-in amplifier
    frequency : float
        DFrequency of acquisition
    V_out : float
        RMS of peak-to-peak value of base voltage in lock-in amplifier
    W : float
        Width of the transistor's channel in meters
    L : float
        Length of the transistor's channel in meters
    n_tft : int, optional
        Numer of trasistors in the sample. The default is 500.

    Returns
    -------
    C : float
        Values of capacitance

    """
    C = current /(2*3.1415*frequency*V_out)
    C = C-min(C) #remove parasite capacitance
    return C

def calculate_DOS(capacitance, oxide_capacitance, W, L, t):
    """
    Function that calculated density of states from capacitance data

    Parameters
    ----------
    capacitance : float
        Capacitance data
    oxide_capacitance : float
        Specific capacitance of oxide dielectric
    W : float
        Width of transistor channel in meters
    L : float
        Length of transistor channel in meteres
    t : float
        Thickness of dielectric

    Returns
    -------
    float
        Values of density of states

    """
    q0 = 1.6e-19 #electron charge
    CD = (capacitance*oxide_capacitance) / (oxide_capacitance-capacitance)
    return (CD /(q0*W*L*t))

def calculate_energy_range(capacitance, oxide_capacitance, voltage, correction=0, init = 0):
    """
    Function that calculates energy (or surface potential) from data

    Parameters
    ----------
    capacitance : float
        Values of measured capacitance
    oxide_capacitance : float
        Specific capacitance of oxide layer
    voltage : float
        Values of voltage offset used in CV measure
    correction : float, optional
        Optional correction to energy scale (account for flat band
                                             voltage). The default is 0.
    init : float, optional
        Initial value for integration. The default is 0.

    Returns
    -------
    E : float
        Values of energy range.

    """
    E = cumtrapz(1-capacitance/oxide_capacitance,voltage, initial = init)+correction
    return E

def find_fit_interval(E, g, FitLeft, FitRight):
    """
    Function that finds intervals for fitting of DOS vs Energy

    Parameters
    ----------
    E : float
        Energy values
    g : float
        DOS values
    FitLeft : float
        Left margin to fit data
    FitRight : float
        DRight margin to fit data

    Returns
    -------
    E : float
        Energy range between Left and Right
    g : float
        DOS range between Left and Right

    """
    fit_interval = np.where((E>=FitLeft) & (E<=FitRight))
    fit_interval = fit_interval[0]
    g = g[fit_interval]
    E = E[fit_interval]
    return E, g
