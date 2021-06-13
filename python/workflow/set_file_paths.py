'''
RUN THIS SCRIPT TO SET ALL FILE PATHS IN SCRIPT TO RELATIVE (USING ROOT DIRECTORY)
'''

import nuke


read_nodes = ['Read', 'ReadGeo2', 'Camera2', 'OCIOFileTransform']

def set_file_paths():
	z = nuke.toNode('root').knob('project_directory').getValue()

	for j in read_nodes:
	    for i in nuke.allNodes(j):
	        x = str(i['file'].value())
	        if z in x:
	            y = x.replace(z, '')
	            i['file'].setValue(y)

nuke.menu("Nuke").addCommand("Workflow/Set File Paths to Relative", 'set_file_paths/set_file_paths()')