import becquerel as bq
import mpld3
from spectrumLocal import *
from plottingLocal import *
from fittingLocal import *

plot = "..\\assets\\plot"
linThresh = "..\\assets\\linearThreshold"
errorBar = "..\\assets\\errorBar"
bestFit = "..\\assets\\bestFit"

counter = 0
dir = os.listdir(plot)

if os.path.exists(plot) and not os.path.isfile(plot):
    if len(dir) != 0:
        for file in dir:
                spec = Spectrum.from_file(os.path.join(plot, file))
                figure, _ = spec.plot()
                if file == '1110C NAA cave pottery.Spe':
                    output = ".\\output\\plot.html"
                elif file == 'Mendocino_07-10-13_Acq-10-10-13.Spe':
                    output = ".\\output\\plot2.html"
                else:
                    counter += 1
                    output = ".\\output\\addedFileOutput\\plot" + str(counter) + ".html"

                print(output)
                mpld3.save_html(figure, output)




dir = os.listdir(linThresh)
if os.path.exists(linThresh) and not os.path.isfile(linThresh):
    if len(dir) != 0:
        for file in dir:
            spec1 = Spectrum.from_file(os.path.join(linThresh, file))
            figure = plt.figure()
            sp = SpectrumPlotter(spec1, xmode='energy', ymode='cpskev', yscale='symlog')
            xcorners, ycorners = sp.get_corners()
            plt.plot(xcorners, ycorners)
            plt.xlabel(sp.xlabel)
            plt.ylabel(sp.ylabel)
            plt.yscale('log')
            plt.xlim(sp.xlim)
            plt.ylim(sp.ylim)
            if file == '1110C NAA cave pottery.Spe':
                output = ".\\output\\plot3.html"
            else:
                counter += 1
                output = ".\\output\\addedFileOutput\\plot" + str(counter) + ".html"
            mpld3.save_html(figure, output)



dir = os.listdir(errorBar)
print('error')
if os.path.exists(errorBar) and not os.path.isfile(errorBar):
    if len(dir) != 0:
        for file in dir:

            spec1 = Spectrum.from_file(os.path.join(errorBar, file))


            sp = SpectrumPlotter(spec1, xmode='channel', ymode='counts', xlim=(3000, 3100), ylim=(0, 100))
            figure, _ = sp.plot(color='black', label='Spectrum')
            sp.errorband(color='green', label='Error band')
            plt.legend(loc=2)

            if file == '1110C NAA cave pottery.Spe':
                output = ".\\output\\plot4.html"
            else:
                counter += 1
                output = ".\\output\\addedFileOutput\\plot" + str(counter) + ".html"

            mpld3.save_html(figure, output)

            sp = SpectrumPlotter(spec1, xmode='channel', ymode='counts', xlim=(3000, 3030), ylim=(0, 50))
            figure, _ = sp.plot(color='black', label='Spectrum')
            sp.errorbar(color='green', capsize=4, fmt='x', label='Error bars')
            plt.legend(loc=3)

            if file == '1110C NAA cave pottery.Spe':
                output = ".\\output\\plot5.html"
            else:
                counter += 1
                output = ".\\output\\addedFileOutput\\plot" + str(counter) + ".html"

            mpld3.save_html(figure, output)



dir = os.listdir(bestFit)
if os.path.exists(bestFit) and not os.path.isfile(bestFit):
    if len(dir) != 0:
        for file in dir:
            counter += 1
            plt.rcParams['figure.facecolor'] = 'white'
            np.random.seed(0)
            spec1 = bq.Spectrum.from_file(os.path.join(bestFit, file))
            model = (bq.fitting.GaussModel(prefix='gauss0_') + bq.fitting.LineModel(prefix='linear_'))
            fitter = bq.Fitter(
                model,
                x=spec1.bin_indices,
                y=spec1.counts_vals,
                y_unc=spec1.counts_uncs,
                roi=(350, 450)
            )

            fitter.fit()
            figure = fitter.custom_plot()
            if file == 'digibase_5min_30_1.spe':
                output = ".\\output\\plot6.html"
            else:
                counter += 1
                output = ".\\output\\addedFileOutput\\plot" + str(counter) + ".html"

            mpld3.save_html(figure, output)
