# -*- coding: utf-8 -*-
"""Definition of the Nota content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from beat.automate import automateMessageFactory as _

from beat.automate.interfaces import INota
from beat.automate.config import PROJECTNAME

from DateTime.DateTime import *
from Products.CMFPlone.utils import getToolByName
from string import join
import json

NotaSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'titulo',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Título"),
            maxlength=40,
        ),
    ),

    atapi.StringField(
        'descricao',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Descrição"),
            maxlength=175,
        ),
    ),

    atapi.StringField(
        'texto',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Texto"),
            maxlength=350,
        ),
    ),

    atapi.StringField(
        'link',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Link"),
            maxlength=40,
        ),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

NotaSchema['title'].storage = atapi.AnnotationStorage()
NotaSchema['title'].widget.label = _(u"Identificação")
NotaSchema['description'].storage = atapi.AnnotationStorage()
NotaSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
NotaSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
NotaSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
NotaSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
NotaSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
NotaSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
NotaSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
NotaSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
NotaSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
NotaSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
NotaSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
NotaSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}


schemata.finalizeATCTSchema(NotaSchema, moveDiscussion=False)


class Nota(base.ATCTContent):
    """Description of the Example Type"""
    implements(INota)

    meta_type = "Nota"
    schema = NotaSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    titulo = atapi.ATFieldProperty('titulo')
    descricao = atapi.ATFieldProperty('descricao')
    texto = atapi.ATFieldProperty('texto')
    link = atapi.ATFieldProperty('link')


    def getAutomator(self):
        novoProjeto =  DateTime().strftime("%Y%m%d%H%M%S") + '_' + self.meta_type
        identificador = self.Title()
        identificador = identificador.replace('"', '\"' )

        titulo = self.getTitulo().replace('"', '\"').strip()
        descricao = self.getDescricao().replace('"', '\"').strip()
        texto = self.getTexto().replace('"', '\"').strip()
        link = self.getLink().replace('"', '\"').strip()

        variaveis = {
            "titulo": titulo,
            "descricao": descricao,
            "texto": texto,
            "link": link
        }

        dados = {
            "novo_projeto": novoProjeto,
            "tipo": "Nota",
            "identificador": identificador,
            "variaveis": variaveis,
        }
        return json.dumps(dados)




atapi.registerType(Nota, PROJECTNAME)
