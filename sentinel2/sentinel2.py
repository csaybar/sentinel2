"""
Sentinel2 Algorithms

This module contains a variety of pre-processing methods to:

- surface reflectance (SR).
- cloud score
- cloud-free composites.
"""

class _Sentinel2Container(dict):
    """A lightweight class that is used as a dictionary with dot notation.
    """

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        del self[name]


class Sentinel2(_Sentinel2Container):

    ee_Initialize()

    @classmethod
    def fmask4(cls,
               img,
               roi,
               erosion=1.5,
               dilation=3,
               cloud_thresh=0.2,
               shadow=True,
               shadow_ndviThresh=-0.1,
               shadow_irSumThresh=0.3,
               mosaic_roicloudthresh=5):
        pass

    @classmethod
    def cloudnet(cls, *args, **kwargs):
        pass

    @classmethod
    def s6(cls):
        pass
