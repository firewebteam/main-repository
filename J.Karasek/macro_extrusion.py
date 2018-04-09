# -*- coding: utf-8 -*-

# Macro Begin: C:\Users\Jakub\Desktop\FreeCAD_macro\macro_extrusion.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
import FreeCAD
import DraftTools
import Draft
import Part

pl = FreeCAD.Placement()
pl.Rotation.Q = (0.0,0.0,1.53080849893e-17,1.0)
pl.Base = FreeCAD.Vector(-4.77938747406,0.862944841385,0.0)
Draft.makeRectangle(length=2.60211086273,height=-1.80554616451,placement=pl,face=False,support=None)
#Gui.activateWorkbench("PartWorkbench")
FreeCAD.getDocument("Nienazwany").addObject("Part::Extrusion","Extrude")
FreeCAD.getDocument("Nienazwany").Extrude.Base = FreeCAD.getDocument("Nienazwany").Rectangle
FreeCAD.getDocument("Nienazwany").Extrude.Dir = (0,0,5)
FreeCAD.getDocument("Nienazwany").Extrude.Solid = (False)
FreeCAD.getDocument("Nienazwany").Extrude.TaperAngle = (0)
FreeCADGui.getDocument("Nienazwany").Rectangle.Visibility = False
FreeCAD.getDocument("Nienazwany").Extrude.Label = 'Extrude'

#Gui.ActiveDocument.Extrude.ShapeColor=Gui.ActiveDocument.Rectangle.ShapeColor
#Gui.ActiveDocument.Extrude.LineColor=Gui.ActiveDocument.Rectangle.LineColor
#Gui.ActiveDocument.Extrude.PointColor=Gui.ActiveDocument.Rectangle.PointColor
# Macro End: C:\Users\Jakub\Desktop\FreeCAD_macro\macro_extrusion.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
