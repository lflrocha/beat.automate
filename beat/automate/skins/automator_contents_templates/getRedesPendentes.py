## Script (Python) "getAgenciaVaiSerNoticiaPendentes"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##

tipos = [
    'Boletim',
    'Nota',
]

solicitacoes = context.portal_catalog.searchResults(meta_type=tipos, sort_on="created", review_state="solicitado")

aux = []
for s in solicitacoes:
    aux.append( { 'tipo': s.Type, 'endereco': s.getURL(), 'titulo': s.Title }  )

return aux
