#Nuke
import nuke
import platform
import nukescripts


#Define Nuke directory when switching between OS's
Win_Dir = 'C:/Users/bogob/.nuke'
MacOSX_Dir = ''
Linux_Dir = '/home/noaht/.nuke'

#Set Global Directory
if platform.system() == "Windows":
	dir = Win_Dir
elif platform.system() == "Darwin":
	dir = MacOSX_Dir
elif platform.system() == "Linux":
	dir = Linux_Dir
else:
	dir = None



#-------------------------------------------------------------------
#	KNOB DEFAULTS	::::::::::::::::::::::::::::::::::::::::::::::::
#-------------------------------------------------------------------

#2D Tracker Defaults
nuke.knobDefault('Tracker4.shutteroffset', "centered")
nuke.knobDefault('Tracker4.label', "Motion: [value transform]\nRef: [value reference_frame]")

nuke.addOnUserCreate(lambda:nuke.thisNode()['reference_frame'].setValue(nuke.frame()), nodeClass='Tracker4')


#Framehold Defaults
nuke.addOnUserCreate(lambda:nuke.thisNode()['first_frame'].setValue(nuke.frame()), nodeClass='FrameHold')


#Blur Defaults
nuke.knobDefault('Blur.label', "Size: [value size]")

# ----- Center Shutter ---------------------------
nuke.knobDefault('Tracker4.shutteroffset', "centered")
nuke.knobDefault('TimeBlur.shutteroffset', "centered")
nuke.knobDefault('Transform.shutteroffset', "centered")
nuke.knobDefault('TransformMasked.shutteroffset', "centered")
nuke.knobDefault('CornerPin2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur3D.shutteroffset', "centered")
nuke.knobDefault('ScanlineRender.shutteroffset', "centered")
nuke.knobDefault('Card3D.shutteroffset', "centered")



#-------------------------------------------------------------------
#	GIZMOS 	        ::::::::::::::::::::::::::::::::::::::::::::::::
#-------------------------------------------------------------------


#Nukepedia Gizmos
nukepediaMenu = nuke.menu('Nodes').addMenu('Nukepedia')

nukepediaMenu.addCommand("L_Grain", "nuke.createNode('l_grain')")
nukepediaMenu.addCommand("ChannelContactSheet", "nuke.createNode('ChannelContactSheet')")
nukepediaMenu.addCommand("DasGrain", "nuke.createNode('DasGrain')")
nukepediaMenu.addCommand('apDespill', 'nuke.createNode("apDespill")')
nukepediaMenu.addCommand('DespillMadness', 'nuke.createNode("DespillMadness")')
nukepediaMenu.addCommand('X_Denoise', 'nuke.createNode("X_Denoise")')
nukepediaMenu.addCommand('AlphaEdge', 'nuke.createNode("AlphaEdge")')
nukepediaMenu.addCommand('AlphaOutline', 'nuke.createNode("alpha_outline")')
nukepediaMenu.addCommand('OpticalZDefocus', 'nuke.createNode("OpticalZDefocus")')
nukepediaMenu.addCommand('Frame_Repair', 'nuke.createNode("Frame_Repair")')
nukepediaMenu.addCommand('RainMaker4', 'nuke.createNode("RainMaker4")')
nukepediaMenu.addCommand('MagicDefocus', 'nuke.createNode("MagicDefocus")')
nukepediaMenu.addCommand('FrameFix_v3', 'nuke.createNode("FrameFix_v3")')
nukepediaMenu.addCommand('GradMagic', 'nuke.createNode("GradMagic")')


#SpinVfxGizmos
spinGizmosMenu = nuke.menu('Nodes').addMenu('SpinVfx', icon = "spin_vfx.jpg")

spinGizmosMenu.addCommand('spinVfx_EdgeExpand', 'nuke.createNode("Edge_Expand")', icon="edge_expand.png")
spinGizmosMenu.addCommand('spinVfx_ErodeFine', 'nuke.createNode("Erode_Fine")', icon="edge_expand.png")


#Pixel Fudger Gizmos
pxfMenu = nuke.menu('Nodes').addMenu('Pxf', icon = "PxF_Menu.png")

pxfMenu.addCommand('PxF_Bandpass', 'nuke.createNode("PxF_Bandpass")', icon = "Pxf_Bandpass.png")
pxfMenu.addCommand('PxF_ChromaBlur', 'nuke.createNode("PxF_ChromaBlur")', icon = "PxF_ChromaBlur.png")
pxfMenu.addCommand('PxF_Distort', 'nuke.createNode("PxF_Distort")', icon = "PxF_Distort.png")
pxfMenu.addCommand('PxF_Erode', 'nuke.createNode("PxF_Erode")', icon = "PxF_Erode.png")
pxfMenu.addCommand('PxF_Filler', 'nuke.createNode("PxF_Filler")', icon = "PxF_Filler.png")
pxfMenu.addCommand('PxF_Grain', 'nuke.createNode("PxF_Grain")', icon = "PxF_Grain.png")
pxfMenu.addCommand('PxF_HueSat', 'nuke.createNode("PxF_HueSat")', icon = "PxF_HueSat.png")
pxfMenu.addCommand('PxF_IDefocus', 'nuke.createNode("PxF_IDefocus")', icon = "PxF_IDefocus.png")
pxfMenu.addCommand('PxF_KillSpill', 'nuke.createNode("PxF_KillSpill")', icon = "PxF_KillSpill.png")
pxfMenu.addCommand('PxF_Line', 'nuke.createNode("PxF_Line")', icon = "PxF_Line.png")
pxfMenu.addCommand('PxF_MergeWrap', 'nuke.createNode("PxF_MergeWrap")', icon = "PxF_MergeWrap.png")
pxfMenu.addCommand('PxF_ScreenClean', 'nuke.createNode("PxF_ScreenClean")', icon = "PxF_ScreenClean.png")


#-------------------------------------------------------------------
#	KEYBOARD SHORTCUTS	::::::::::::::::::::::::::::::::::::::::::::
#-------------------------------------------------------------------

#TRACKER
nuke.menu('Nodes').addCommand("Transform/Tracker", "nuke.createNode('Tracker4')", "ctrl+alt+t", icon="Tracker.png", shortcutContext = 2)


#---------- Merge Shortcuts ----------------------------

mergeMenu = nuke.menu('Nodes').findItem("Merge/Merges")

mergeMenu.addCommand('Stencil', 'nuke.createNode("Merge2", "operation stencil bbox B")', "alt+o", icon="Out.png", shortcutContext = 2)
mergeMenu.addCommand('Mask', 'nuke.createNode("Merge2", "operation mask bbox A")', "alt+i", icon="Out.png", shortcutContext = 2)
mergeMenu.addCommand('Plus', 'nuke.createNode("Merge2", "operation plus")', "alt+]", icon="Out.png", shortcutContext = 2)
mergeMenu.addCommand('From', 'nuke.createNode("Merge2", "operation from bbox B")', "alt+[", icon="Out.png", shortcutContext = 2)


#-------------------------------------------------------------------
#	PYTHON	::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#-------------------------------------------------------------------


#Simple WORKFLOW python scripts
workflow_menu = nuke.menu('Nuke').addMenu("Workflow")

#Make backdrops setter more efficent
import backdrops_setter
import set_file_paths
import relative_cornerpins

#PIPELINE
pipeline_menu = nuke.menu('Nuke').addMenu("Pipeline")
import shot_launcher