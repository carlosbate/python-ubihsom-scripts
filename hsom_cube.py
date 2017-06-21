import hsom_service as h

hsom = h.createhsom('cube')
hsomid = hsom['id']
print('HSOM %s created.' % hsomid)

dsxy = h.createseqds('cube', 50, 'x,y')
#dsxy = h.createrandomds('cube', 50, 10, 'x,y')
print('XY data streamer created %s.' % dsxy['id'])
dsyz = h.createseqds('cube', 50, 'y,z')
#dsyz = h.createrandomds('cube', 50, 10, 'y,z')
print('YZ data streamer created %s.'% dsyz['id'])

xynode = h.createhsomnode(hsomid,
                              [dsxy['id']],
                              25,#70
                              'XY',
                              ["x", "y"],
                              2)
print('XY HSOM Node created %s.' % xynode['id'])
h.linkdatasource(dsxy['id'], xynode['zipper'])
print('Linked XY data source with XY HSOM Node...')

yznode = h.createhsomnode(hsomid,
                              [dsyz['id']],
                              25,#70
                              'YZ',
                              ["y", "z"],
                              2)
print('YZ HSOM Node created %s.' % yznode['id'])
h.linkdatasource(dsyz['id'], yznode['zipper'])
print('Linked YZ data source with YZ HSOM Node...')

globalnode = h.createhsomnode(hsomid,
                              [xynode['id'], yznode['id']],
                              50,#90
                              'Global',
                              ["XYx", "XYy",
                               "YZx", "YZy"],
                              4)
print('Global HSOM Node created %s.' % globalnode['id'])

h.linknode(hsomid, xynode['id'], globalnode['id'])
print('Linked XY Node with Global HSOM Node...')
h.linknode(hsomid, yznode['id'], globalnode['id'])
print('Linked YZ HSOM Node with Global HSOM Node...')
print('Complete')
