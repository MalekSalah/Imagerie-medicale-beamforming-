def beamforming(RF_data, fs, c, pitch, Depth):
    """
    Beamforming algorithm for ultrasound imaging
    Input:
        RF_data: RF data in time domain (2D array)
        fs: sampling frequency (float)
        c: speed of sound (float)
        pitch: pitch of the transducer (float)
        Imaging_domain: the domain of imaging (2 element tuple)
    Output:
        image: ultrasound image
    """
    import numpy as np

    # Set domain parameters 
    dx = pitch
    X = np.arange(0,np.size(RF_data,1)) * dx
    X_elts = X.copy()
    Z = (c * np.arange(0,np.size(RF_data,0)))/(2 * fs)
    Domain  = Z[(Z >= Depth[0]) & (Z <= Depth[1])]

    # Intialize the image
    S = np.zeros((len(Domain), len(X)))

    for i in range(len(Domain)):
        for j in range(len(X)):
            x, z = X[j], Domain[i]

            Tau_discrete = np.round(((z + np.sqrt((x - x1)**2 + z**2)) / c) * fs).astype(int) # Discretize the time
            contribution_indices = (Tau_discrete, np.arange(len(X_elts))) # Indices of the RF data that contribute to the imaging point
            
            S[i,j] = np.sum(RF_data[contribution_indices])
    
    return (np.abs(S)/np.max(np.abs(S)))