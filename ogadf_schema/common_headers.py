from fits_schema.header import HeaderSchema, HeaderCard


class HDUClass(HeaderSchema):
    '''Minimum HDU* headers for this standard'''
    HDUCLASS = HeaderCard(allowed_values='GADF')
    HDUDOC   = HeaderCard(allowed_values='https://gamma-astro-data-formats.readthedocs.io')
    HDUVERS  = HeaderCard(allowed_values=['v0.2', '0.2'])


class EarthLocation(HeaderSchema):
    '''
    Header cards for the observatory location,
    optional as it might be a sattelite
    '''
    GEOLON = HeaderCard(required=False, type_=float)
    GEOLAT = HeaderCard(required=False, type_=float)
    ALTITUDE = HeaderCard(required=False, type_=float)


class TimeDefinition(HeaderSchema):
    '''
    Header keywords for the definition of time columns.
    All keywords are requred here.
    Add this to the headerschema when a table contains a time column
    '''
    MJDREFI = HeaderCard(required=True, type_=int)
    MJDREFF = HeaderCard(required=True, type_=float)
    TIMEUNIT = HeaderCard(required=True, type_=str, allowed_values=['s'])
    TIMESYS = HeaderCard(
        required=True, type_=str, allowed_values=['UT1', 'UTC', 'TAI', 'TT']
    )
    TIMEREF = HeaderCard(required=True, type_=str, allowed_values=[
        'LOCAL', 'SOLARSYSTEM', 'HELIOCENTRIC', 'GEOCENTRIC',
    ])


class Object(HeaderSchema):
    '''Name and coordinates of observerd object, if any'''
    OBJECT = HeaderCard(required=False, type_=str)
    RA_OBJ = HeaderCard(required=False, type_=float)
    DEC_OBJ = HeaderCard(required=False, type_=float)
