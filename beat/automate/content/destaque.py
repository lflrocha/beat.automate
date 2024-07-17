# -*- coding: utf-8 -*-
"""Definition of the Destaque content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from beat.automate import automateMessageFactory as _

from beat.automate.interfaces import IDestaque
from beat.automate.config import PROJECTNAME

from DateTime.DateTime import *
from Products.CMFPlone.utils import getToolByName
from string import join
import json

DestaqueSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'link',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Link da notícia"),
        ),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

DestaqueSchema['title'].storage = atapi.AnnotationStorage()
DestaqueSchema['title'].widget.label = _(u"Identificação")
DestaqueSchema['description'].storage = atapi.AnnotationStorage()
DestaqueSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaqueSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaqueSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaqueSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaqueSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaqueSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaqueSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaqueSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaqueSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaqueSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaqueSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaqueSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}

schemata.finalizeATCTSchema(DestaqueSchema, moveDiscussion=False)


class Destaque(base.ATCTContent):
    """Description of the Example Type"""
    implements(IDestaque)

    meta_type = "Destaque"
    schema = DestaqueSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    link = atapi.ATFieldProperty('link')

    def getAutomator(self):
        novoProjeto =  DateTime().strftime("%Y%m%d%H%M%S") + '_' + self.meta_type
        identificador = self.Title()
        identificador = identificador.replace('"', '\"' )

        link = self.getLink()

        variaveis = {
            "link": link,
        }

        dados = {
            "novo_projeto": novoProjeto,
            "tipo": "Destaque",
            "identificador": identificador,
            "variaveis": variaveis,
        }
        return json.dumps(dados)




atapi.registerType(Destaque, PROJECTNAME)
