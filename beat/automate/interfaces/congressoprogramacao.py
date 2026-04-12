from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from beat.automate import automateMessageFactory as _



class ICongressoProgramacao(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    hora = schema.TextLine(
        title=_(u"Hora"),
        required=True,
        description=_(u"Field description"),
    )
#
    data = schema.TextLine(
        title=_(u"Data"),
        required=True,
        description=_(u"Field description"),
    )
#
    dia = schema.TextLine(
        title=_(u"Dia"),
        required=True,
        description=_(u"Field description"),
    )
#
    tipo = schema.TextLine(
        title=_(u"Tipo"),
        required=True,
        description=_(u"Field description"),
    )
#
    evento = schema.TextLine(
        title=_(u"Evento"),
        required=True,
        description=_(u"Field description"),
    )
#
    local = schema.TextLine(
        title=_(u"Local"),
        required=False,
        description=_(u"Field description"),
    )
#
