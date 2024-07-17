## Script (Python) "getTVBrNCP"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=data
##title=
##

data = DateTime(data,datefmt='international')

fim = DateTime(data.strftime("%d/%m/%Y 23:59:59"),datefmt='international')

tipos = [
    'Boletim',
    'Nota',
    'Destaque'
]

folder_path = '/'.join(context.getPhysicalPath())

solicitacoes = context.portal_catalog.searchResults(meta_type=tipos, sort_on="created", sort_order="reverse", path={'query': folder_path}, modified={"query": [data,fim], "range": "min:max"})

return solicitacoes
