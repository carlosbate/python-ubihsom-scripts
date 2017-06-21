import hsom_service as h

hsom = h.createhsom('iris')
hsomid = hsom['id']
print('HSOM %s created.' % hsomid)


#dssepals = h.createrandomds('iris', 1, 50, 'sepal_length,sepal_width')
dssepals = h.createseqds('seqiris', 100, 'sepal_length,sepal_width')
print('Sepal data streamer created %s.' % dssepals['id'])
dspetals = h.createseqds('seqiris', 100, 'petal_length,petal_width')
print('Petal data streamer created %s.'% dspetals['id'])


sepalsnode = h.createhsomnode(hsomid,
                              [dssepals['id']],
                              25,
                              'Sepals',
                              ["Sepal Length", "Sepal Width"],
                              2)
print('Sepal HSOM Node created %s.' % sepalsnode['id'])


#dspetals = h.createrandomds('iris', 1, 50, 'petal_length,petal_width')
petalsnode = h.createhsomnode(hsomid,
                              [dspetals['id']],
                              25,
                              'Petals',
                              ["Petal Length", "Petal Width"],
                              2)
print('Petal HSOM Node created %s.' % petalsnode['id'])

globalnode = h.createhsomnode(hsomid,
                              [sepalsnode['id'], petalsnode['id']],
                              100,
                              'Global',
                              ["Sepals X", "Sepals Y",
                               "Petals X", "Petals Y"],
                              4)
print('Global HSOM Node created %s.' % globalnode['id'])

h.linknode(hsomid, sepalsnode['id'], globalnode['id'])
print('Linked Petal Sepals Node with Global HSOM Node...')
h.linknode(hsomid, petalsnode['id'], globalnode['id'])
print('Linked Petal HSOM Node with Global HSOM Node...')
h.linkdatasource(dspetals['id'], petalsnode['zipper'])
print('Linked Sepal data source with Sepal HSOM Node...')
h.linkdatasource(dssepals['id'], sepalsnode['zipper'])
print('Linked Petal data source with Petal HSOM Node...')
print('Complete')

