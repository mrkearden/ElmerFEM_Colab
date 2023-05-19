# trace generated using paraview version 5.11.0
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
step_t0001vtu = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get display properties
step_t0001vtuDisplay = GetDisplayProperties(step_t0001vtu, view=renderView1)

# set scalar coloring
ColorBy(step_t0001vtuDisplay, ('POINTS', 'pressure'))

# rescale color and/or opacity maps used to include current data range
step_t0001vtuDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
step_t0001vtuDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'pressure'
pressureLUT = GetColorTransferFunction('pressure')

# get opacity transfer function/opacity map for 'pressure'
pressurePWF = GetOpacityTransferFunction('pressure')

# get 2D transfer function for 'pressure'
pressureTF2D = GetTransferFunction2D('pressure')

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1600, 749)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.048, 10000.0]
renderView1.CameraFocalPoint = [0.0, 0.048, 0.0]
renderView1.CameraParallelScale = 0.11092339699089639

# save screenshot
SaveScreenshot('C:\featest\ElmerFEM_Colab\ParaviewScripts\pressure.png', renderView1, ImageResolution=[1600, 749])

# turn off scalar coloring
ColorBy(step_t0001vtuDisplay, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pressureLUT, renderView1)

# change representation type
step_t0001vtuDisplay.SetRepresentationType('Wireframe')

# layout/tab size in pixels
layout1.SetSize(1600, 749)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.048, 10000.0]
renderView1.CameraFocalPoint = [0.0, 0.048, 0.0]
renderView1.CameraParallelScale = 0.11092339699089639

# save screenshot
SaveScreenshot('C:\featest\ElmerFEM_Colab\ParaviewScripts\wireframe.png', renderView1, ImageResolution=[1600, 749])

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1600, 749)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.048, 10000.0]
renderView1.CameraFocalPoint = [0.0, 0.048, 0.0]
renderView1.CameraParallelScale = 0.11092339699089639

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).