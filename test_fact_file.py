from ogadf_schema.events import EVENTS
from astropy.io import fits
import logging

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(levelname)s| %(message)s'))
logging.getLogger().addHandler(handler)

f = fits.open('resources/fact/20131103_103_dl3.fits')
EVENTS.validate_hdu(f['EVENTS'], onerror='log')
