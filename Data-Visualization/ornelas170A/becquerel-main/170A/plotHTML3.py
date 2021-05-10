"""Not functional example:
    -Read in SPE file
    -Store in dataframe
    -Plot Spectrum
        This example plots the spectrum while showing
        capabilities of including error bars
    -Export to html file and display on local host
"""

import becquerel as bq
import numpy as np
import matplotlib.pyplot as plt
import mpld3
from becquerel import SpectrumPlotter

spec1 = bq.Spectrum.from_file('../tests/samples/1110C NAA cave pottery.Spe')

sp = SpectrumPlotter(spec1, xmode='channel', ymode='counts', xlim=(3000,3100), ylim=(0,100))
sp.plot(color='black', label='Spectrum')
sp.errorband(color='green', label='Error band')
plt.legend(loc=2)


sp = SpectrumPlotter(spec1, xmode='channel', ymode='counts', xlim=(3000,3030), ylim=(0,50))
sp.plot(color='black', label='Spectrum')
sp.errorbar(color='green', capsize=4, fmt='x', label='Error bars')
plt.legend(loc=3)

mpld3.show()