# -*- coding: utf-8 -*-
"""Definition of the Congresso Programacao content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from beat.automate import automateMessageFactory as _

from beat.automate.interfaces import ICongressoProgramacao
from beat.automate.config import PROJECTNAME

from DateTime.DateTime import *
from Products.CMFPlone.utils import getToolByName
from string import join
import json

CongressoProgramacaoSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'data',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Data"),
        ),
        required=True,
        vocabulary=["12/07", "13/07", "14/07", "15/07"],
    ),


    atapi.StringField(
        'dia',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Dia"),
        ),
        required=True,
        vocabulary=["1º dia", "2º dia", "3º dia", "4º dia"],
    ),

    atapi.StringField(
        'hora',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Hora"),
            description=_(u"No formato HH:MM - HH:MM"),
            maxlength=13,
        ),
        required=True,
    ),


    atapi.StringField(
        'tipo',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Tipo"),
            maxlength=25,
        ),
        required=True,
    ),


    atapi.StringField(
        'evento',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Evento"),
            maxlength=70,
        ),
        required=True,
    ),


    atapi.StringField(
        'local',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Local"),
            maxlength=30,
        ),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

CongressoProgramacaoSchema['title'].storage = atapi.AnnotationStorage()
CongressoProgramacaoSchema['title'].widget.label = _(u"Identificação")
CongressoProgramacaoSchema['description'].storage = atapi.AnnotationStorage()
CongressoProgramacaoSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
CongressoProgramacaoSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
CongressoProgramacaoSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
CongressoProgramacaoSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
CongressoProgramacaoSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
CongressoProgramacaoSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
CongressoProgramacaoSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
CongressoProgramacaoSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
CongressoProgramacaoSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
CongressoProgramacaoSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
CongressoProgramacaoSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
CongressoProgramacaoSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}


schemata.finalizeATCTSchema(CongressoProgramacaoSchema, moveDiscussion=False)


class CongressoProgramacao(base.ATCTContent):
    """Description of the Example Type"""
    implements(ICongressoProgramacao)

    meta_type = "CongressoProgramacao"
    schema = CongressoProgramacaoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    hora = atapi.ATFieldProperty('hora')
    data = atapi.ATFieldProperty('data')
    dia = atapi.ATFieldProperty('dia')
    tipo = atapi.ATFieldProperty('tipo')
    evento = atapi.ATFieldProperty('evento')
    local = atapi.ATFieldProperty('local')

    def getAutomator(self):
        novoProjeto =  DateTime().strftime("%Y%m%d%H%M%S") + '_' + self.meta_type
        identificador = self.Title()
        identificador = identificador.replace('"', '\"' )

        hora = self.getHora().replace('"', '\"').strip()
        data = self.getData().replace('"', '\"').strip()
        dia = self.getDia().replace('"', '\"').strip()
        tipo = self.getTipo().replace('"', '\"').strip()
        evento = self.getEvento().replace('"', '\"').strip()
        local = self.getLocal().replace('"', '\"').strip()

        variaveis = {
            "hora": hora,
            "data": data,
            "dia": dia,
            "texto_tipo": tipo,
            "evento": evento,
            "local": local
        }

        dados = {
            "novo_projeto": novoProjeto,
            "tipo": "Programacao",
            "identificador": identificador,
            "variaveis": variaveis,
        }
        return json.dumps(dados)





atapi.registerType(CongressoProgramacao, PROJECTNAME)
