import numpy as np

def calculate_PC(data, gain, change_positions):
    """
    Function that given input data returns the photocurrent spectra calculated
    with each 

    Parameters
    ----------
    data : 
        input data of photocurrent
    gain : float
        vector with gains used
    change_positions : float
        vector with positions at which the gain has been changed

    Returns
    -------
    Amp: float
        calculated amplitude photocurrent

    """
    
    Amps = [] #vector of amplitudes
    sens = data.s[0] #sensitivity 
    p = 0 # counter for initial position
    for i, j in enumerate(change_positions):
        amp = data.Amp[p:j+1] #take that part of spectrum
        amp = amp*sens*1e-4 /gain[i] #adjust with gain and sens
        Amps.append(amp) #append
    #Now concatenate all the spectra to a single one
    Amp = np.stack(Amps)
    return Amp