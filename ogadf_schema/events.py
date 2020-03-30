from fits_schema.binary_table import BinaryTable, Int64, Double, Int16
from fits_schema.header import HeaderCard
import astropy.units as u

from .common_headers import (
    EarthLocation, TimeDefinition, Object, HDUClass, CoordinateSystem
)


class EVENTS(BinaryTable):
    '''
    The ``EVENTS`` extension is a binary FITS table containing an event list.
    Each row of the table provides information that characterises one event.
    The mandatory and optional columns of the table are defined.
    In addition, a list of header keywords providing metadata is specified.
    Also here there are mandatory and optional keywords.
    The recommended extension name of the binary table is EVENTS.
    '''
    # Mandatory
    EVENT_ID = Int64()
    TIME     = Double(unit=u.s)
    RA       = Double(unit=u.deg)
    DEC      = Double(unit=u.deg)
    ENERGY   = Double(unit=u.TeV)

    # Optional
    MULTIP      = Int16(required=False)
    GLON        = Double(unit=u.deg, required=False)
    GLAT        = Double(unit=u.deg, required=False)
    ALT         = Double(unit=u.deg, required=False)
    AZ          = Double(unit=u.deg, required=False)
    DETX        = Double(unit=u.deg, required=False)
    DETY        = Double(unit=u.deg, required=False)
    THETA       = Double(unit=u.deg, required=False)
    PHI         = Double(unit=u.deg, required=False)
    DIR_ERR     = Double(unit=u.deg, required=False)
    ENERGY_ERR  = Double(unit=u.TeV, required=False)
    COREX       = Double(unit=u.m, required=False)
    COREY       = Double(unit=u.m, required=False)
    CORE_ERR    = Double(unit=u.m, required=False)
    XMAX        = Double(unit=u.g / u.cm**2, required=False)
    XMAX_ERR    = Double(unit=u.g / u.cm**2, required=False)
    HIL_MSW     = Double(required=False)
    HIL_MSL     = Double(required=False)
    HIL_MSL_ERR = Double(required=False)

    class __header__(HDUClass, TimeDefinition, EarthLocation, Object, CoordinateSystem):
        # Mandatory
        HDUCLAS1 = HeaderCard(allowed_values='EVENTS')
        OBS_ID   = HeaderCard(type_=int)
        TSTART   = HeaderCard(type_=float)
        TSTOP    = HeaderCard(type_=float)
        ONTIME   = HeaderCard(type_=float)
        LIVETIME = HeaderCard(type_=float)
        DEADC    = HeaderCard(type_=float)
        RA_PNT   = HeaderCard(type_=float)
        DEC_PNT  = HeaderCard(type_=float)
        ORIGIN   = HeaderCard(type_=str)
        TELESCOP = HeaderCard(type_=str)
        INSTRUME = HeaderCard(type_=str)
        CREATOR  = HeaderCard(type_=str)

        # Optional
        HDUCLAS1 = HeaderCard(type_=str, required=False)
        TELLIST  = HeaderCard(type_=str, required=False)
        N_TELS   = HeaderCard(type_=int, required=False)
        TASSIGN  = HeaderCard(type_=str, required=False)


class GTI(BinaryTable):
    '''
    The ``GTI`` extension is a binary FITS table that contains the Good Time
    Intervals ('GTIs') for the event list.
    A general description of GTIs can be found in the `OGIP GTI`_ standard.

    This HDU contains two mandatory columns named ``START`` and ``STOP``.
    At least one row is containing the start and end time of the observation must
    be present.
    The values are in units of seconds with respect to the reference
    time defined in the header (keywords MJDREFI and MJDREFF).
    This extension allows for a detailed handling of good time intervals
    (i.e. excluding periods with cloud cover or lightning during one observation).

    High-level Science tools could modify the GTIs according to user parameter.
    See e.g. `gtmktime`_ for an application example from the Fermi Science Tools.
    '''
    # Mandatory
    START = Double(unit=u.s)
    STOP  = Double(unit=u.s)

    class __header__(HDUClass, TimeDefinition, EarthLocation):
        HDUCLAS1 = HeaderCard(allowed_values='GTI')
