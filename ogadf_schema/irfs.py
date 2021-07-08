import astropy.units as u
from fits_schema.binary_table import BinaryTable, Double
from fits_schema.header import HeaderCard
from .common_headers import HDUClass


class AEFF_2D(BinaryTable):
    '''
    Radially effective area table in
    bins of true energy and field of view offset
    '''
    ENERG_LO = Double(ndim=1, unit=u.TeV)
    ENERG_HI = Double(ndim=1, unit=u.TeV)
    THETA_LO = Double(ndim=1, unit=u.deg)
    THETA_HI = Double(ndim=1, unit=u.deg)
    EFFAREA  = Double(ndim=2, unit=u.m**2)

    class __header__(HDUClass):
        HDUCLAS1 = HeaderCard(allowed_values='RESPONSE')
        HDUCLAS2 = HeaderCard(allowed_values='EFF_AREA')
        HDUCLAS3 = HeaderCard(allowed_values={'FULL-ENCLOSURE', 'POINT-LIKE'})
        HDUCLAS4 = HeaderCard(allowed_values='AEFF_2D')
        RAD_MAX  = HeaderCard(type_=float, required=False)
        OBS_ID   = HeaderCard(type_=int, required=False)
        LO_THRES = HeaderCard(type_=float, required=False)
        HI_THRES = HeaderCard(type_=float, required=False)


class EDISP_2D(BinaryTable):
    '''
    Energy dispersion as relative energy migration in bins of
    true energy and field of view offset
    '''
    ENERG_LO = Double(ndim=1, unit=u.TeV)
    ENERG_HI = Double(ndim=1, unit=u.TeV)
    MIGRA_LO = Double(ndim=1, unit=u.one)
    MIGRA_HI = Double(ndim=1, unit=u.one)
    THETA_LO = Double(ndim=1, unit=u.deg)
    THETA_HI = Double(ndim=1, unit=u.deg)
    MATRIX   = Double(ndim=3, unit=u.one)

    class __header__(HDUClass):
        HDUCLAS1 = HeaderCard(allowed_values='RESPONSE')
        HDUCLAS2 = HeaderCard(allowed_values='EDISP')
        HDUCLAS3 = HeaderCard(allowed_values={'FULL-ENCLOSURE', 'POINT-LIKE'})
        HDUCLAS4 = HeaderCard(allowed_values='EDISP_2D')
        RAD_MAX = HeaderCard(type_=float, required=False)
        OBS_ID   = HeaderCard(type_=int, required=False)
        LO_THRES = HeaderCard(type_=float, required=False)
        HI_THRES = HeaderCard(type_=float, required=False)


class RAD_MAX(BinaryTable):
    '''
    Table with radius of the selection are for point-like irfs in bins
    of true energy and field of view offset.
    '''
    ENERG_LO = Double(ndim=1, unit=u.TeV)
    ENERG_HI = Double(ndim=1, unit=u.TeV)
    THETA_LO = Double(ndim=1, unit=u.deg)
    THETA_HI = Double(ndim=1, unit=u.deg)
    RAD_MAX  = Double(ndim=2, unit=u.deg)

    class __header__(HDUClass):
        HDUCLAS1 = HeaderCard(allowed_values='RESPONSE')
        HDUCLAS2 = HeaderCard(allowed_values='RAD_MAX')
        HDUCLAS3 = HeaderCard(allowed_values='POINT-LIKE')
        HDUCLAS4 = HeaderCard(allowed_values='RAD_MAX_2D')


class PSF_TABLE(BinaryTable):
    '''
    Point Spread Function as tabulated probability density
    in bins of energy, field of view offset and offset from the point-source
    position
    '''
    ENERG_LO = Double(ndim=1, unit=u.TeV)
    ENERG_HI = Double(ndim=1, unit=u.TeV)
    THETA_LO = Double(ndim=1, unit=u.deg)
    THETA_HI = Double(ndim=1, unit=u.deg)
    RAD_LO   = Double(ndim=1, unit=u.deg)
    RAD_HI   = Double(ndim=1, unit=u.deg)
    RPSF     = Double(ndim=3, unit=1 / u.sr)

    class __header__(HDUClass):
        HDUCLAS1 = HeaderCard(allowed_values='RESPONSE')
        HDUCLAS2 = HeaderCard(allowed_values='PSF')
        HDUCLAS3 = HeaderCard(allowed_values='FULL-ENCLOSURE')
        HDUCLAS4 = HeaderCard(allowed_values='PSF_TABLE')


class PSF_3GAUSS(BinaryTable):
    '''
    Point Spread Function parameterized by a sum of three Gaussian
    distributions in bins of true energy and field of view offset.
    '''
    ENERG_LO = Double(ndim=1, unit=u.TeV)
    ENERG_HI = Double(ndim=1, unit=u.TeV)
    THETA_LO = Double(ndim=1, unit=u.deg)
    THETA_HI = Double(ndim=1, unit=u.deg)
    SCALE    = Double(ndim=2, unit=1 / u.sr)
    SIGMA_1  = Double(ndim=2, unit=u.deg)
    SIGMA_2  = Double(ndim=2, unit=u.deg)
    SIGMA_3  = Double(ndim=2, unit=u.deg)
    AMPL_2   = Double(ndim=2, unit=u.one)
    AMPL_3   = Double(ndim=2, unit=u.one)

    class __header__(HDUClass):
        HDUCLAS1 = HeaderCard(allowed_values='RESPONSE')
        HDUCLAS2 = HeaderCard(allowed_values='PSF')
        HDUCLAS3 = HeaderCard(allowed_values='FULL-ENCLOSURE')
        HDUCLAS4 = HeaderCard(allowed_values='PSF_3GAUSS')


class PSF_KING(BinaryTable):
    '''
    Point Spread Function parameterized by the King function
    '''
    ENERG_LO = Double(ndim=1, unit=u.TeV)
    ENERG_HI = Double(ndim=1, unit=u.TeV)
    THETA_LO = Double(ndim=1, unit=u.deg)
    THETA_HI = Double(ndim=1, unit=u.deg)
    GAMMA    = Double(ndim=2, unit=u.one)
    SIGMA    = Double(ndim=2, unit=u.deg)

    class __header__(HDUClass):
        HDUCLAS1 = HeaderCard(allowed_values='RESPONSE')
        HDUCLAS2 = HeaderCard(allowed_values='PSF')
        HDUCLAS3 = HeaderCard(allowed_values='FULL-ENCLOSURE')
        HDUCLAS4 = HeaderCard(allowed_values='PSF_KING')


class BKG_2D(BinaryTable):
    '''
    Background radially symmetric in the field of view
    '''
    ENERG_LO = Double(ndim=1, unit=u.TeV)
    ENERG_HI = Double(ndim=1, unit=u.TeV)
    THETA_LO = Double(ndim=1, unit=u.deg)
    THETA_HI = Double(ndim=1, unit=u.deg)
    BKG      = Double(ndim=2, unit=u.Unit('MeV-1 s-1 sr-1'))

    class __header__(HDUClass):
        HDUCLAS1 = HeaderCard(allowed_values='RESPONSE')
        HDUCLAS2 = HeaderCard(allowed_values='BKG')
        HDUCLAS3 = HeaderCard(allowed_values='FULL-ENCLOSURE')
        HDUCLAS4 = HeaderCard(allowed_values='BKG_2D')


class BKG_3D(BinaryTable):
    '''
    Background in two dimensional field of view coordinates
    '''
    ENERG_LO = Double(ndim=1, unit=u.TeV)
    ENERG_HI = Double(ndim=1, unit=u.TeV)
    DETX_LO  = Double(ndim=1, unit=u.deg)
    DETX_HI  = Double(ndim=1, unit=u.deg)
    DETY_LO  = Double(ndim=1, unit=u.deg)
    DETY_HI  = Double(ndim=1, unit=u.deg)
    BKG      = Double(ndim=3, unit=u.Unit('MeV-1 s-1 sr-1'))

    class __header__(HDUClass):
        HDUCLAS1 = HeaderCard(allowed_values='RESPONSE')
        HDUCLAS2 = HeaderCard(allowed_values='BKG')
        HDUCLAS3 = HeaderCard(allowed_values='FULL-ENCLOSURE')
        HDUCLAS4 = HeaderCard(allowed_values='BKG_3D')
        FOVALIGN = HeaderCard(allowed_values={'ALTAZ', 'RADEC'})
