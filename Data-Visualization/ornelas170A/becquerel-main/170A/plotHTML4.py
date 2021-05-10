"""Partionally functional fit line example:
    -Read in SPE file
    -Store in dataframe
    -Plot Spectrum
        This example plots the best fit lines as determined by the code
        below the plot of the lines is the residuals from the best fit.
        Analytics about the fit line are supposed to be displayed, as
        seen in the printout, but currently cannot display them with the
        graphs (although it should be possible)
    -Export to html file and display on local host
"""

import becquerel as bq
import numpy as np
import matplotlib.pyplot as plt
import mpld3


plt.rcParams['figure.facecolor'] = 'white'
np.random.seed(0)
spec1 = bq.Spectrum.from_file('../tests/samples/digibase_5min_30_1.spe')
model = (bq.fitting.GaussModel(prefix='gauss0_') + bq.fitting.LineModel(prefix='linear_'))
fitter = bq.Fitter(
    model,
    x=spec1.bin_indices,
    y=spec1.counts_vals,
    y_unc=spec1.counts_uncs,
    roi=(350, 450)
)

fitter.fit()
fitter.custom_plot()
mpld3.show()