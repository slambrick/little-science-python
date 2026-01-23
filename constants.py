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
# Species identification and mass lookup

def get_species_mass(species):
    """
    Get the mass of a particle species from a string identifier
    
    Parameters
    ----------
    species : str
        Species identifier (e.g., 'n', 'neutron', 'He-3', 'he4', etc.)
    
    Returns
    -------
    mass : float
        Particle mass [kg]
    """
    species_lower = species.lower().replace(' ', '').replace('-', '')
    
    # Neutron
    if species_lower in ['n', 'neutron']:
        return mn
    
    # Helium-3
    elif species_lower in ['he3', 'helium3', '3he', '3helium']:
        return mHe3
    
    # Helium-4
    elif species_lower in ['he4', 'helium4', '4he', '4helium']:
        return mHe
    
    # Generic helium (defaults to He-4)
    elif species_lower in ['he', 'helium']:
        print("Warning: 'He' specified without isotope, defaulting to He-4")
        return mHe
    
    else:
        raise ValueError(f"Unknown species: {species}. Use 'n', 'He-3', 'He-4'")


# Conversion functions
def lambda_to_E(wavelength, species='n'):
    """
    Convert wavelength to energy
    
    Parameters
    ----------
    wavelength : float or array
        Wavelength [m]
    species : str, optional
        Particle species (default: 'n')
    
    Returns
    -------
    energy : float or array
        Energy [meV]
    """
    m = get_species_mass(species)
    energy = (h**2 / (2 * m * wavelength**2)) / meV2J
    return energy

def E_to_lambda(energy, species='n'):
    """
    Convert energy to wavelength
    
    Parameters
    ----------
    energy : float or array
        Energy [meV]
    species : str, optional
        Particle species (default: 'n')
    
    Returns
    -------
    wavelength : float or array
        Wavelength [m]
    """
    m = get_species_mass(species)
    wavelength = h / np.sqrt(2 * m * energy * meV2J)
    return wavelength

def lambda_to_p(wavelength, species='n'):
    """
    Convert wavelength to momentum
    
    Parameters
    ----------
    wavelength : float or array
        Wavelength [m]
    species : str, optional
        Particle species (default: 'n')
    
    Returns
    -------
    momentum : float or array
        Momentum [kg⋅m/s]
    """
    momentum = h / wavelength
    return momentum

def p_to_lambda(momentum, species='n'):
    """
    Convert momentum to wavelength
    
    Parameters
    ----------
    momentum : float or array
        Momentum [kg⋅m/s]
    species : str, optional
        Particle species (default: 'n')
    
    Returns
    -------
    wavelength : float or array
        Wavelength [m]
    """
    wavelength = h / momentum
    return wavelength

def E_to_p(energy, species='n'):
    """
    Convert energy to momentum
    
    Parameters
    ----------
    energy : float or array
        Energy [meV]
    species : str, optional
        Particle species (default: 'n')
    
    Returns
    -------
    momentum : float or array
        Momentum [kg⋅m/s]
    """
    m = get_species_mass(species)
    momentum = np.sqrt(2 * m * energy * meV2J)
    return momentum

def p_to_E(momentum, species='n'):
    """
    Convert momentum to energy
    
    Parameters
    ----------
    momentum : float or array
        Momentum [kg⋅m/s]
    species : str, optional
        Particle species (default: 'n')
    
    Returns
    -------
    energy : float or array
        Energy [meV]
    """
    m = get_species_mass(species)
    energy = (momentum**2 / (2 * m)) / meV2J
    return energy

def v_to_E(velocity, species='n'):
    """
    Convert velocity to energy
    
    Parameters
    ----------
    velocity : float or array
        Velocity [m/s]
    species : str, optional
        Particle species (default: 'n')
    
    Returns
    -------
    energy : float or array
        Energy [meV]
    """
    m = get_species_mass(species)
    energy = (0.5 * m * velocity**2) / meV2J
    return energy

def E_to_v(energy, species='n'):
    """
    Convert energy to velocity
    
    Parameters
    ----------
    energy : float or array
        Energy [meV]
    species : str, optional
        Particle species (default: 'n')
    
    Returns
    -------
    velocity : float or array
        Velocity [m/s]
    """
    m = get_species_mass(species)
    velocity = np.sqrt(2 * energy * meV2J / m)
    return velocity
