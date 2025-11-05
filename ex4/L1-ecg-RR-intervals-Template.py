# Programming Exercise 1 - Extraction of R-R Interval from ECG signal
# =============================================================================
# 2024-08-27 Reto Wildhaber   
# -----------------------------------------------------------------------------


import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks, decimate


#%% Cell (1): loading test signal
file_name = 'data/apnea-ecg-a01er-data.csv'
fs = 100  # sampling rate [Hz] of recorded signal
# -- LOAD TEST SIGNAL --
y = np.genfromtxt(file_name, usecols=(1,4), delimiter=r',', skip_header=1, )
y_ecg = y[:,0]
y_resp = y[:,1]
K = len(y)
k = np.arange(K)


# plot signal
fig, axs = plt.subplots(1, 1, sharex='all', figsize=(10, 2))
fig.tight_layout()
axs.plot(k, y_ecg)

print("Filename:", file_name)
print("Number of loaded samples: ",K)
print("Total signal duration [s]: ", K/fs)
print("Signal shape and samples "+str(y_ecg.shape)+" : "+str(y))


#%% Cell (2) : Find QRS Peaks and compute R-R Intervals
# **to do 1** (dummy code) --
ind_peaks = [111,222,456,789] # QRS peaks in ecg signal
nof_peaks = 4 # number of peaks found
# ------------------------------


print("Indices of minima: ",ind_peaks)
print("Total number of peaks found: ",nof_peaks)
if nof_peaks == 0:
    print("No maxima found. Exit.")
    exit()
    
# -- **to do 2**  (dummy code) --
t_rr = np.ones(nof_peaks-1)  # RR-time intervals
y_QRS = np.ones(nof_peaks-1) # QRS amplitudes at R wave
# -------------------------------
print("R-R Intervals [s]: ",t_rr)


#%% Cell (3): Plotting of the ECG signal and the R-R intervals
fig, axs = plt.subplots(3, 1, sharex='all', figsize=(10, 6))
axs[0].plot(k, y_ecg, lw=1.0, color='gray')
axs[0].scatter(ind_peaks, y_ecg[ind_peaks], c='b', marker='+')
axs[0].set_title("ECG Signal")
axs[0].set_ylabel('ECG [mV]')

axs[1].plot(k, y_resp, 'g-', label='Respiration')
axs[1].set_ylabel('Respiration (Flow)')

axs[2].plot(ind_peaks[1:], t_rr, '.-', label='R-R interval [s]')
axs[2].plot(ind_peaks[1:], y_QRS, '.-', label='R-Peak Amplitude [mV]')
axs[2].set_ylabel('R-R [s]')
axs[2].legend()

plt.show()

#%% Cell (4): Plotting of the ECG signal vs. Respiration

# -- **to do 3**  --







