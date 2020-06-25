"""Top-level package for sentinel2."""

__author__ = """Cesar Aybar Camacho"""
__email__ = 'csaybar@gmail.com'
__version__ = '0.0.1'

import ee
from .Sentinel2 import Sentinel2

ee.Algorithms.Sentinel2 = Sentinel2

def ee_Initialize():
    """Authenticates Earth Engine and initialize an Earth Engine session
    """
    if ee.Algorithms:
        pass
    else:
        try:
            ee.Initialize()
        except:
            ee.Authenticate()
            ee.Initialize()
