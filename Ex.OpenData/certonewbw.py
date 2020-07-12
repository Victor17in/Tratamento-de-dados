"""
Relativistic Breit-Wigner.
"""

import numpy as np
from numpy import pi
from scipy.stats import rv_continuous

import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('Zmumu_Run2011A_masses.csv')

cond1 = 1.52 #Era 1.52
cond2 = 0.45 #Era 0.45

# Create two DataFrames. Select to "large_etas" events where the pseudorapidities
# of the both muons are larger than "cond1". Select to "small_etas" events where
# the pseudorapidities of the both muons are smaller than "cond2".
large_etas = dataset[(np.absolute(dataset.eta1) > cond1) & (np.absolute(dataset.eta2) > cond1)]
small_etas = dataset[(np.absolute(dataset.eta1) < cond2) & (np.absolute(dataset.eta2) < cond2)]

# Print two empty lines for better design.
print('\n' * 2)

print('The amount of all events = %d' % len(dataset))
print('The amount of events where the pseudorapidity of both muons has been large = %d' %len(large_etas))
print('The amount of events where the pseudorapidity of both muons has been small = %d' %len(small_etas))

###########################################################################################################################

# Save the invariant masses to variable "inv_mass1".
inv_mass1 = large_etas['M']
inv_mass2 = small_etas['M']
# Jupyter Notebook uses "magic functions". With this function it is possible to plot
# the histogram straight to notebook.
#% matplotlib inline

# Create the histogram from data in variable "inv_mass1". Set bins and range.
plt.hist(inv_mass1, bins=120, range=(60,120))

# Set y-axis range from 0 to 60.
axes = plt.gca()
axes.set_ylim([0,60])

# Name the axises and give a title.
plt.xlabel('Invariant mass [GeV]')
plt.ylabel('Number of events per bin')
plt.title('Histogram of invariant masses for the events where the\n pseudorapidity of both of the muons has been large\n')
plt.show()

###########################################################################################################################

class breit_wigner_gen(rv_continuous):
    """
    Probability density function for relativistic Breit-Wigner distribution [1]_.
    
    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Relativistic_Breit-Wigner_distribution
    
    Notes
    -----
    
    Plot a Breit-Wigner distribution and random samples
    ---------------------------------------------------
    >>> import matplotlib.pyplot as plt
    >>> BW = breit_wigner(mass=91.33, width=3.87)  #ou (mass=91.45, width=6.4416)
    
    >>> mass = np.linspace(0., 200., 500)
    >>> pdf = [BW.pdf(m) for m in mass]
    >>> pdf_plot = plt.plot(mass, pdf)
    
    >>> samples = inv_mass2 #ou inv_mass1
    >>> hist_plot = plt.hist(samples, normed=True, bins=100, range=[0, 200])
    
    >>> plt.show()
    
    Statistics of a Breit-Wigner distribution
    -----------------------------------------
    
    Mean and variance:
    
    >>> BW.stats()
   
    
    Median:
    
    >>> BW.median()
    
    
    Variance and standard deviation:
    
    >>> BW.var(), BW.std()
    
    
    95 per cent interval:
    
    >>> BW.interval(0.95)
    
    
    Moments:
    
    >>> [BW.moment(n) for n in range(1, 6)]
    [122.11538219739913, 15674.920254744189, inf, 244138132.80994478, 80583978992.641495]
    
    """
    def _argcheck(self, mass, width):
        """
        We require mass > 0 and width > 0.
        The width -> 0 limit is well-defined mathematically - it's proportional
        to a Dirac function. In the m -> 0 limit, the pdf vanishes.
        Parameters
        ----------
        mass : float
            Mass of resonance        
        width : float
            Width of resonance
        Returns
        -------
        _argcheck :  bool
            Whether shape parameters are legitimate
        """
        return (mass > 0) & (width > 0)

    def _pdf(self, m, mass, width):
        """
        Parameters
        ----------
        mass : float
            Mass of resonance        
        width : float
            Width of resonance
        Returns
        -------
        pdf :  float
            PDF of Breit-Wigner distribution
        >>> breit_wigner(mass=125., width=0.05).pdf(125.)
        12.732396211295313
        """
        alpha = width / mass
        gamma = mass**2 * (1. + alpha**2)**0.5
        k = 2.**(3. / 2.) * mass**2 * alpha * gamma / (pi * (mass**2 + gamma)**0.5)

        return k / ((m**2 - mass**2)**2 + mass**4 * alpha**2)

    def _cdf(self, m, mass, width):
        """
        Parameters
        ----------
        mass : float
            Mass of resonance        
        width : float
            Width of resonance
        Returns
        -------
        cdf :  float
            CDF of Breit-Wigner distribution
        The CDf was found by Mathematica:
        pdf = k/((m^2 - mass^2)^2 + mass^4*alpha^2)
        cdf = Integrate[pdf, m]
        >>> BW = breit_wigner(mass=125., width=0.05)
        >>> BW.cdf(125.)
        0.50052268648248666
        >>> BW.cdf(1E10)
        1.0000000000000004
        >>> BW.cdf(0.)
        0.0
        """
        alpha = width / mass
        gamma = mass**2 * (1. + alpha**2)**0.5
        k = 2.**(3. / 2.) * mass**2 * alpha * gamma / (pi * (mass**2 + gamma)**0.5)
        
        arg_1 = complex(-1)**(1. / 4.) / (-1j + alpha)**0.5 * m / mass
        arg_2 = complex(-1)**(3. / 4.) / (1j + alpha)**0.5 * m / mass

        shape = -1j * np.arctan(arg_1) / (-1j + alpha)**0.5 - np.arctan(arg_2) / (1j + alpha)**0.5
        norm = complex(-1)**(1. / 4.) * k / (2. * alpha * mass**3)

        cdf_ = shape * norm
        cdf_ = cdf_.real

        return cdf_


breit_wigner = breit_wigner_gen(a=0, b=np.inf, name='Breit-Wigner', shapes='mass, width')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
#######################################################################################################
x1 = 88.3065
x2 = 94.7581
width = 6.4416*10**9
h_cortado = 6.582*10**-16
lifetime=h_cortado/width
print 'A meia vida do Z e(s): '
print lifetime
#Propagando os erros nessa equação lifetime=h_cortado/width, sendo o erro de width dado por BW.std e assumindo o erro de h muito pequeno, temos:
sigmat = h_cortado*14.83/(width)**2
print 'O erro da meia vida e(s): '
print sigmat
print 'Entao a estimativa da meia vida do Z e: '
print '(1.02 +- 2.35)*10**-25 s'
print 'E esta dentro de 3*10**-25 s'
