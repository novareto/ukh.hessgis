import grok
import uvcsite

from zope.interface import Interface


grok.templatedir('templates')


class IHessGis(Interface):
    pass


class HessGisComponent(object):
    pass


class HessGis(uvcsite.ProductFolder):
    grok.implements(IHessGis)
    uvcsite.contenttype(HessGisComponent)


class HessGisView(uvcsite.Page):
    grok.context(IHessGis)
    grok.name('index')
