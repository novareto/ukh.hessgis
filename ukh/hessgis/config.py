import grok
import uvcsite

class HessGisPR(uvcsite.ProductRegistration):
    grok.name('HessGis')
    grok.title('HessGISS')
    grok.description('Hess Gis Lorem Ipsoum')
    uvcsite.productfolder('ukh.hessgis.components.HessGis')
