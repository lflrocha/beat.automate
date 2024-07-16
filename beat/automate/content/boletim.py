# -*- coding: utf-8 -*-
"""Definition of the Boletim content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from beat.automate import automateMessageFactory as _

from beat.automate.interfaces import IBoletim
from beat.automate.config import PROJECTNAME

from DateTime.DateTime import *
from Products.CMFPlone.utils import getToolByName
from string import join
import json

BoletimSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    atapi.DateTimeField(
        'datainicio',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"Data inicio"),
            show_hm=False
        ),
        validators=('isValidDate'),
        required=True
    ),

    atapi.DateTimeField(
        'datafim',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"Data Fim"),
            show_hm=False
        ),
        validators=('isValidDate'),
        required=True
    ),

    atapi.ImageField(
        'foto1',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ImageWidget(
            label=_(u"Foto 1"),
        ),
        pil_quality=100,
        sizes = {'square' : (1000, 1000)},
        validators=('isNonEmptyFile'),
        required=True
    ),

    atapi.StringField(
        'legenda1',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Legenda 1"),
            maxlength=120,
        ),
        required=True
    ),

    atapi.ImageField(
        'foto2',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ImageWidget(
            label=_(u"Foto 2"),
        ),
        pil_quality=100,
        sizes = {'square' : (1000, 1000)},
        validators=('isNonEmptyFile'),
        required=True
    ),

    atapi.StringField(
        'legenda2',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Legenda 2"),
            maxlength=120,
        ),
        required=True
    ),


    atapi.ImageField(
        'foto3',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ImageWidget(
            label=_(u"Foto 3"),
        ),
        pil_quality=100,
        sizes = {'square' : (1000, 1000)},
        validators=('isNonEmptyFile'),
    ),

    atapi.StringField(
        'legenda3',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Legenda 3"),
            maxlength=120,
        ),
    ),

    atapi.ImageField(
        'foto4',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ImageWidget(
            label=_(u"Foto 4"),
        ),
        pil_quality=100,
        sizes = {'square' : (1000, 1000)},
        validators=('isNonEmptyFile'),
    ),

    atapi.StringField(
        'legenda4',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Legenda 4"),
            maxlength=120,
        ),
    ),

    atapi.ImageField(
        'foto5',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ImageWidget(
            label=_(u"Foto 5"),
        ),
        pil_quality=100,
        sizes = {'square' : (1000, 1000)},
        validators=('isNonEmptyFile'),
    ),

    atapi.StringField(
        'legenda5',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Legenda 5"),
            maxlength=120,
        ),
    ),

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

BoletimSchema['title'].storage = atapi.AnnotationStorage()
BoletimSchema['title'].widget.label = _(u"Identificação")
BoletimSchema['description'].storage = atapi.AnnotationStorage()
BoletimSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
BoletimSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
BoletimSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
BoletimSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
BoletimSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
BoletimSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
BoletimSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
BoletimSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
BoletimSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
BoletimSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
BoletimSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
BoletimSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}


schemata.finalizeATCTSchema(BoletimSchema, moveDiscussion=False)


class Boletim(base.ATCTContent):
    """Description of the Example Type"""
    implements(IBoletim)

    meta_type = "Boletim"
    schema = BoletimSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    datainicio = atapi.ATFieldProperty('datainicio')
    datafim = atapi.ATFieldProperty('datafim')
    foto1 = atapi.ATFieldProperty('foto1')
    legenda1 = atapi.ATFieldProperty('legenda1')
    foto2 = atapi.ATFieldProperty('foto2')
    legenda2 = atapi.ATFieldProperty('legenda2')
    foto3 = atapi.ATFieldProperty('foto3')
    legenda3 = atapi.ATFieldProperty('legenda3')
    foto4 = atapi.ATFieldProperty('foto4')
    legenda4 = atapi.ATFieldProperty('legenda4')
    foto5 = atapi.ATFieldProperty('foto5')
    legenda5 = atapi.ATFieldProperty('legenda5')


    def getAutomator(self):
        novoProjeto =  DateTime().strftime("%Y%m%d%H%M%S") + '_' + self.meta_type
        identificador = self.Title()
        identificador = identificador.replace('"', '\"' )

        datainicio = self.getDatainicio()
        datainicio = datainicio.strftime("%d/%m")
        datafim = self.getDatafim()
        datafim = datafim.strftime("%d/%m")

        filename1 = self.getFilename('foto1')
        endereco1 = self.absolute_url() + "/@@images/foto1/square"
        legenda1 = self.getLegenda1().replace('"', '\"').strip()

        filename2 = self.getFilename('foto2')
        endereco2 = self.absolute_url() + "/@@images/foto2/square"
        legenda2 = self.getLegenda2().replace('"', '\"').strip()

        filename3 = self.getFilename('foto3')
        endereco3 = self.absolute_url() + "/@@images/foto3/square"
        legenda3 = self.getLegenda3().replace('"', '\"').strip()

        filename4 = self.getFilename('foto4')
        endereco4 = self.absolute_url() + "/@@images/foto4/square"
        legenda4 = self.getLegenda4().replace('"', '\"').strip()

        filename5 = self.getFilename('foto5')
        endereco5 = self.absolute_url() + "/@@images/foto5/square"
        legenda5 = self.getLegenda5().replace('"', '\"').strip()


        variaveis = {
            "datainicio": datainicio,
            "datafim": datafim,
            "filename1": filename1,
            "endereco1": endereco1,
            "legenda1": legenda1,

            "filename2": filename2,
            "endereco2": endereco2,
            "legenda2": legenda2,

            "filename3": filename3,
            "endereco3": endereco3,
            "legenda3": legenda3,

            "filename4": filename4,
            "endereco4": endereco4,
            "legenda4": legenda4,

            "filename5": filename5,
            "endereco5": endereco5,
            "legenda5": legenda5,
        }

        dados = {
            "novo_projeto": novoProjeto,
            "tipo": "Boletim",
            "identificador": identificador,
            "variaveis": variaveis,
        }
        return json.dumps(dados)




atapi.registerType(Boletim, PROJECTNAME)
