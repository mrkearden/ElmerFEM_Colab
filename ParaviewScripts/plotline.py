import sys
name_of_the_script=sys.argv[0]
xvalue=float(sys.argv[1])
y1=float(sys.argv[2])
y2=float(sys.argv[3])
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

# find source
step_t0001vtu = FindSource('Step_t0001.vtu')

# create a new 'Plot Over Line'
print("xvalue=", xvalue)
plotOverLine1 = PlotOverLine(registrationName='PlotOverLine1', Input=step_t0001vtu)
plotOverLine1.Point1 = [xvalue, y1, 0.0]
plotOverLine1.Point2 = [xvalue, y2, 0.0]


# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
plotOverLine1Display = Show(plotOverLine1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'velocity'
velocityLUT = GetColorTransferFunction('velocity')

# trace defaults for the display properties.
plotOverLine1Display.Representation = 'Surface'
plotOverLine1Display.ColorArrayName = ['POINTS', 'velocity']
plotOverLine1Display.LookupTable = velocityLUT
plotOverLine1Display.SelectTCoordArray = 'None'
plotOverLine1Display.SelectNormalArray = 'None'
plotOverLine1Display.SelectTangentArray = 'None'
plotOverLine1Display.OSPRayScaleArray = 'GeometryIds'
plotOverLine1Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display.SelectOrientationVectors = 'None'
plotOverLine1Display.ScaleFactor = 0.011021714843809606
plotOverLine1Display.SelectScaleArray = 'GeometryIds'
plotOverLine1Display.GlyphType = 'Arrow'
plotOverLine1Display.GlyphTableIndexArray = 'GeometryIds'
plotOverLine1Display.GaussianRadius = 0.0005510857421904803
plotOverLine1Display.SetScaleArray = ['POINTS', 'GeometryIds']
plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.OpacityArray = ['POINTS', 'GeometryIds']
plotOverLine1Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1Display.SelectInputVectors = ['POINTS', 'velocity']
plotOverLine1Display.WriteLog = ''

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1Display_1.UseIndexForXAxis = 0
plotOverLine1Display_1.XArrayName = 'arc_length'
plotOverLine1Display_1.SeriesVisibility = ['GeometryIds', 'kinetic dissipation', 'kinetic energy', 'pressure', 'velocity_Magnitude']
plotOverLine1Display_1.SeriesLabel = ['arc_length', 'arc_length', 'GeometryIds', 'GeometryIds', 'kinetic dissipation', 'kinetic dissipation', 'kinetic energy', 'kinetic energy', 'pressure', 'pressure', 'velocity_X', 'velocity_X', 'velocity_Y', 'velocity_Y', 'velocity_Z', 'velocity_Z', 'velocity_Magnitude', 'velocity_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'GeometryIds', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'kinetic dissipation', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'kinetic energy', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'pressure', '0.6', '0.3100022888532845', '0.6399938963912413', 'velocity_X', '1', '0.5000076295109483', '0', 'velocity_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'velocity_Z', '0', '0', '0', 'velocity_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'vtkValidPointMask', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_X', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Points_Y', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_Z', '1', '0.5000076295109483', '0', 'Points_Magnitude', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867']
plotOverLine1Display_1.SeriesOpacity = ['arc_length', '1.0', 'GeometryIds', '1.0', 'kinetic dissipation', '1.0', 'kinetic energy', '1.0', 'pressure', '1.0', 'velocity_X', '1.0', 'velocity_Y', '1.0', 'velocity_Z', '1.0', 'velocity_Magnitude', '1.0', 'vtkValidPointMask', '1.0', 'Points_X', '1.0', 'Points_Y', '1.0', 'Points_Z', '1.0', 'Points_Magnitude', '1.0']
plotOverLine1Display_1.SeriesPlotCorner = ['arc_length', '0', 'GeometryIds', '0', 'kinetic dissipation', '0', 'kinetic energy', '0', 'pressure', '0', 'velocity_X', '0', 'velocity_Y', '0', 'velocity_Z', '0', 'velocity_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesLabelPrefix = ''
plotOverLine1Display_1.SeriesLineStyle = ['arc_length', '1', 'GeometryIds', '1', 'kinetic dissipation', '1', 'kinetic energy', '1', 'pressure', '1', 'velocity_X', '1', 'velocity_Y', '1', 'velocity_Z', '1', 'velocity_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesLineThickness = ['arc_length', '2', 'GeometryIds', '2', 'kinetic dissipation', '2', 'kinetic energy', '2', 'pressure', '2', 'velocity_X', '2', 'velocity_Y', '2', 'velocity_Z', '2', 'velocity_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['arc_length', '0', 'GeometryIds', '0', 'kinetic dissipation', '0', 'kinetic energy', '0', 'pressure', '0', 'velocity_X', '0', 'velocity_Y', '0', 'velocity_Z', '0', 'velocity_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['arc_length', '4', 'GeometryIds', '4', 'kinetic dissipation', '4', 'kinetic energy', '4', 'pressure', '4', 'velocity_X', '4', 'velocity_Y', '4', 'velocity_Z', '4', 'velocity_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesOpacity = ['arc_length', '1', 'GeometryIds', '1', 'kinetic dissipation', '1', 'kinetic energy', '1', 'pressure', '1', 'velocity_X', '1', 'velocity_Y', '1', 'velocity_Z', '1', 'velocity_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesPlotCorner = ['GeometryIds', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'kinetic dissipation', '0', 'kinetic energy', '0', 'pressure', '0', 'velocity_Magnitude', '0', 'velocity_X', '0', 'velocity_Y', '0', 'velocity_Z', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesLineStyle = ['GeometryIds', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'kinetic dissipation', '1', 'kinetic energy', '1', 'pressure', '1', 'velocity_Magnitude', '1', 'velocity_X', '1', 'velocity_Y', '1', 'velocity_Z', '1', 'vtkValidPointMask', '1']
plotOverLine1Display_1.SeriesLineThickness = ['GeometryIds', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'kinetic dissipation', '2', 'kinetic energy', '2', 'pressure', '2', 'velocity_Magnitude', '2', 'velocity_X', '2', 'velocity_Y', '2', 'velocity_Z', '2', 'vtkValidPointMask', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['GeometryIds', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'kinetic dissipation', '0', 'kinetic energy', '0', 'pressure', '0', 'velocity_Magnitude', '0', 'velocity_X', '0', 'velocity_Y', '0', 'velocity_Z', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['GeometryIds', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'kinetic dissipation', '4', 'kinetic energy', '4', 'pressure', '4', 'velocity_Magnitude', '4', 'velocity_X', '4', 'velocity_Y', '4', 'velocity_Z', '4', 'vtkValidPointMask', '4']

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['kinetic dissipation', 'kinetic energy', 'pressure', 'velocity_Magnitude']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['kinetic energy', 'pressure', 'velocity_Magnitude']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['pressure', 'velocity_Magnitude']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['velocity_Magnitude']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = []

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['velocity_X']

# save screenshot
SaveScreenshot('plotline.png', lineChartView1, ImageResolution=[795, 748])

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