import numpy as np
from numpy import pi

# Physical constants
h = 6.62607015e-34   # Planck constant [Js]
hbar = h/(2*pi)      # Reduced Planck constant [Js]
c = 299792458        # Speed of light [m/s]
kB = 1.380649e-23    # Boltzmann constant [J/K]
NA = 6.02214076e-23  # Avagadro number [1/mol]
mu = 1.660539069e-27 # Atomic mass unit [kg]

# Neutron things
d002 = 3.354e-10   # 002 spacing in Graphite [m]
mn = 1.6749275e-27 # Neutron mass [kg]

# Helium things
mHe = 4.002602*mu   # Mass of He-4 [kg]
mHe3 = 3.0160293*mu # Mass of He-3 [kg]

# Conversion factors
meV2J = 1.6021892*1E-22  # Convert from meV to J

# Conversion functions
