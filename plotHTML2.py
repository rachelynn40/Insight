"""Not functional example:
    -Read in SPE file
    -Store in dataframe
    -Plot Spectrum
        Cannot display advanced plotting techniques in the HTML file
        This prevents us from binning using linear thresholds and must
        use logarithmic scales, preventing correct binning of values
    -Export to HTML and display on local host
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
plt.yscale('log')
plt.xlim(sp.xlim)
plt.ylim(sp.ylim)
mpld3.show()