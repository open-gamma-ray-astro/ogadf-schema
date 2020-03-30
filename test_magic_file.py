from ogadf_schema.events import EVENTS, GTI
from ogadf_schema.irfs import AEFF_2D, EDISP_2D
from astropy.io import fits
import logging

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(levelname)s| %(message)s'))
logging.getLogger().addHandler(handler)

f = fits.open('resources/magic/run_05029747_DL3.fits')
print(*[repr(hdu.header['EXTNAME']) for hdu in f[1:]])

print('Checking EVENTS HDU')
EVENTS.validate_hdu(f['EVENTS'], onerror='log')

print('Checking GTI HDU')
GTI.validate_hdu(f['GTI'], onerror='log')

print('Checking effective area HDU')
AEFF_2D.validate_hdu(f['EFFECTIVE AREA'], onerror='log')

print('Checking energy dispersion HDU')
EDISP_2D.validate_hdu(f['ENERGY DISPERSION'], onerror='log')
