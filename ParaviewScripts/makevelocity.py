# trace generated using paraview version 5.11.0
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Unstructured Grid Reader'
step_t0001vtu = XMLUnstructuredGridReader(registrationName='Step_t0001.vtu', FileName=['Step_t0001.vtu'])
step_t0001vtu.CellArrayStatus = ['GeometryIds']
step_t0001vtu.PointArrayStatus = ['kinetic energy', 'kinetic dissipation', 'pressure', 'velocity']

# Properties modified on step_t0001vtu
step_t0001vtu.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
step_t0001vtuDisplay = Show(step_t0001vtu, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
step_t0001vtuDisplay.Representation = 'Surface'
step_t0001vtuDisplay.ColorArrayName = [None, '']
step_t0001vtuDisplay.SelectTCoordArray = 'None'
step_t0001vtuDisplay.SelectNormalArray = 'None'
step_t0001vtuDisplay.SelectTangentArray = 'None'
step_t0001vtuDisplay.OSPRayScaleArray = 'kinetic dissipation'
step_t0001vtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
step_t0001vtuDisplay.SelectOrientationVectors = 'None'
step_t0001vtuDisplay.ScaleFactor = 0.020000000000000004
step_t0001vtuDisplay.SelectScaleArray = 'None'
step_t0001vtuDisplay.GlyphType = 'Arrow'
step_t0001vtuDisplay.GlyphTableIndexArray = 'None'
step_t0001vtuDisplay.GaussianRadius = 0.001
step_t0001vtuDisplay.SetScaleArray = ['POINTS', 'kinetic dissipation']
step_t0001vtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
step_t0001vtuDisplay.OpacityArray = ['POINTS', 'kinetic dissipation']
step_t0001vtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
step_t0001vtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
step_t0001vtuDisplay.PolarAxes = 'PolarAxesRepresentation'
step_t0001vtuDisplay.ScalarOpacityUnitDistance = 0.009448273839846975
step_t0001vtuDisplay.OpacityArrayName = ['POINTS', 'kinetic dissipation']
step_t0001vtuDisplay.SelectInputVectors = ['POINTS', 'velocity']
step_t0001vtuDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
step_t0001vtuDisplay.ScaleTransferFunction.Points = [0.0002631517848743772, 0.0, 0.5, 0.0, 219.35611156213065, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
step_t0001vtuDisplay.OpacityTransferFunction.Points = [0.0002631517848743772, 0.0, 0.5, 0.0, 219.35611156213065, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera(False)

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.048, 10000.0]
renderView1.CameraFocalPoint = [0.0, 0.048, 0.0]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(step_t0001vtuDisplay, ('POINTS', 'velocity', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
step_t0001vtuDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
step_t0001vtuDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'velocity'
velocityLUT = GetColorTransferFunction('velocity')

# get opacity transfer function/opacity map for 'velocity'
velocityPWF = GetOpacityTransferFunction('velocity')

# get 2D transfer function for 'velocity'
velocityTF2D = GetTransferFunction2D('velocity')

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1600, 499)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.048, 10000.0]
renderView1.CameraFocalPoint = [0.0, 0.048, 0.0]
renderView1.CameraParallelScale = 0.11092339699089639

# save screenshot
SaveScreenshot('velocity.png', renderView1, ImageResolution=[1600, 499])

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1600, 499)

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