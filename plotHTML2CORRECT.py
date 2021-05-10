"""Not functional example:
    -Read in SPE file
    -Store in dataframe
    -Plot Spectrum
        This example correctly bins using linear thresholds
        but is too complex for exporting to HTML
"""

import becquerel as bq
import numpy as np
import matplotlib.pyplot as plt
import mpld3
from becquerel import SpectrumPlotter

spec1 = bq.Spectrum.from_file('../tests/samples/1110C NAA cave pottery.Spe')
plt.figure()


sp = SpectrumPlotter(spec1, xmode='energy', ymode='cpskev', yscale='symlog')
xcorners, ycorners = sp.get_corners()
plt.plot(xcorners, ycorners)
plt.xlabel(sp.xlabel)
plt.ylabel(sp.ylabel)
plt.yscale('symlog', linthreshy = sp.linthreshy)
plt.xlim(sp.xlim)
plt.ylim(sp.ylim)
plt.show()