import hsom_service as hsom

h = hsom.createhsom('financialHSOM')
hsomid = h['id']
print('Created HSOM: %s' %hsomid)

dstechoil = hsom.createseqds('pricesnorm', 100, 'Apple,IBM,Microsoft,Statoil,Exxon')#50
print('Created sequential data source: %s' % dstechoil['id'])
dsweb = hsom.createseqds('pricesnorm', 100, 'Facebook,Google,Amazon')#50
print('Created sequential data source: %s' % dsweb['id'])

technode = hsom.createhsomnode(hsomid,
                               [dstechoil['id']],
                               25,#60
                               'TechOil',
                               ["Apple", "IBM", "Microsoft", "Statoil", "Exxon"],
                               5)
print('Created TechOil HSOM node: %s' % technode['id'])
hsom.linkdatasource(dstechoil['id'], technode['zipper'])
print('Linked Tech data source with Tech HSOM Node...')

webnode = hsom.createhsomnode(hsomid,
                              [dsweb['id']],
                              25,#60
                              'Web',
                              ["Facebook", "Google", "Amazon"],
                              3)
print('Created Web HSOM node: %s' % webnode['id'])
hsom.linkdatasource(dsweb['id'], webnode['zipper'])
print('Linked Web data source with Web HSOM Node...')

globalnode = hsom.createhsomnode(hsomid,
                    [technode['id'], webnode['id']],
                    100,#70
                    'Global',
                    ["TechOilX", "TechOilY", "WebX", "WebY"],
                    4)
print('Created Global HSOM node: %s' % globalnode['id'])
hsom.linknode(hsomid, technode['id'], globalnode['id'])
print('Linked TechOil HSOM node with Global HSOM node')
hsom.linknode(hsomid, webnode['id'], globalnode['id'])
print('Linked Web HSOM node with Global HSOM node')
print('Complete')
