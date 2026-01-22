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

# Neutron conversion functions
def n_lambda_to_E(wavelength):
    """
    Convert neutron wavelength to energy
    
    Parameters
    ----------
    wavelength : float or array
        Neutron wavelength [m]
    
    Returns
    -------
    energy : float or array
        Neutron energy [meV]
    """
    energy = (h**2 / (2 * mn * wavelength**2)) / meV2J
    return energy

def n_E_to_lambda(energy):
    """
    Convert neutron energy to wavelength
    
    Parameters
    ----------
    energy : float or array
        Neutron energy [meV]
    
    Returns
    -------
    wavelength : float or array
        Neutron wavelength [m]
    """
    wavelength = h / np.sqrt(2 * mn * energy * meV2J)
    return wavelength

def n_lambda_to_p(wavelength):
    """
    Convert neutron wavelength to momentum
    
    Parameters
    ----------
    wavelength : float or array
        Neutron wavelength [m]
    
    Returns
    -------
    momentum : float or array
        Neutron momentum [kg⋅m/s]
    """
    momentum = h / wavelength
    return momentum

def n_p_to_lambda(momentum):
    """
    Convert neutron momentum to wavelength
    
    Parameters
    ----------
    momentum : float or array
        Neutron momentum [kg⋅m/s]
    
    Returns
    -------
    wavelength : float or array
        Neutron wavelength [m]
    """
    wavelength = h / momentum
    return wavelength

def n_E_to_p(energy):
    """
    Convert neutron energy to momentum
    
    Parameters
    ----------
    energy : float or array
        Neutron energy [meV]
    
    Returns
    -------
    momentum : float or array
        Neutron momentum [kg⋅m/s]
    """
    momentum = np.sqrt(2 * mn * energy * meV2J)
    return momentum

def n_p_to_E(momentum):
    """
    Convert neutron momentum to energy
    
    Parameters
    ----------
    momentum : float or array
        Neutron momentum [kg⋅m/s]
    
    Returns
    -------
    energy : float or array
        Neutron energy [meV]
    """
    energy = (momentum**2 / (2 * mn)) / meV2J
    return energy

def n_v_to_E(velocity):
    """
    Convert neutron velocity to energy
    
    Parameters
    ----------
    velocity : float or array
        Neutron velocity [m/s]
    
    Returns
    -------
    energy : float or array
        Neutron energy [meV]
    """
    energy = (0.5 * mn * velocity**2) / meV2J
    return energy

def n_E_to_v(energy):
    """
    Convert neutron energy to velocity
    
    Parameters
    ----------
    energy : float or array
        Neutron energy [meV]
    
    Returns
    -------
    velocity : float or array
        Neutron velocity [m/s]
    """
    velocity = np.sqrt(2 * energy * meV2J / mn)
    return velocity
