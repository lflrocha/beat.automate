from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from beat.automate import automateMessageFactory as _



class IDestaque(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    link = schema.TextLine(
        title=_(u"New Field"),
        required=False,
        description=_(u"Field description"),
    )
#
