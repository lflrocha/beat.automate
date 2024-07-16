from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from beat.automate import automateMessageFactory as _



class IBoletim(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    legenda1 = schema.TextLine(
        title=_(u"Legenda 1"),
        required=False,
        description=_(u"Field description"),
    )
#
    foto1 = schema.Bytes(
        title=_(u"Foto 01"),
        required=False,
        description=_(u"Field description"),
    )
#
    datafim = schema.Date(
        title=_(u"Data Fim"),
        required=False,
        description=_(u"Field description"),
    )
#
    datainicio = schema.Date(
        title=_(u"Data inicio"),
        required=False,
        description=_(u"Field description"),
    )
#
