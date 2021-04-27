Attribute VB_Name = "Modul1"
Sub Kravatte()
Attribute Kravatte.VB_ProcData.VB_Invoke_Func = "K\n14"
'
' Kravatte Makro
'
' Tastenkombination: Strg+Umschalt+K
'
vx = Worksheets("Kravatte").Range("B1")
vy = Worksheets("Kravatte").Range("B2")
sx = Worksheets("Kravatte").Range("B3")
sy = Worksheets("Kravatte").Range("B4")
r = Worksheets("Kravatte").Range("B5")
g = Worksheets("Kravatte").Range("B6")
b = Worksheets("Kravatte").Range("B7")
d = Worksheets("Kravatte").Range("B8")



    With ActiveSheet.Shapes.BuildFreeform(msoEditingAuto, vx + sx * 0, vy + sy * 0)
        .AddNodes msoSegmentLine, msoEditingAuto, vx + sx * 0, vy + sy * 1
        .AddNodes msoSegmentLine, msoEditingAuto, vx + sx * 0.93, vy + sy * 0.53
        .AddNodes msoSegmentLine, msoEditingAuto, vx + sx * 1.07, vy + sy * 0.53
        .AddNodes msoSegmentLine, msoEditingAuto, vx + sx * 2, vy + sy * 1
        .AddNodes msoSegmentLine, msoEditingAuto, vx + sx * 2, vy + sy * 0
        .AddNodes msoSegmentLine, msoEditingAuto, vx + sx * 1.07, vy + sy * 0.47
        .AddNodes msoSegmentLine, msoEditingAuto, vx + sx * 0.93, vy + sy * 0.47
        .AddNodes msoSegmentLine, msoEditingAuto, vx + sx * 0, vy + sy * 0
        .ConvertToShape.Select
    End With
    With Selection.ShapeRange.Fill
        .Visible = msoTrue
        .ForeColor.RGB = RGB(r, g, b)
        .Transparency = 0.09
        .Solid
    End With
    With Selection.ShapeRange.Line
        .Visible = msoTrue
        .Weight = d
    End With
End Sub
