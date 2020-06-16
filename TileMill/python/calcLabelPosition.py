# import libraries (not needed if running running the script from ArcMap's Python interpreter)
import arcpy

def generateLabelPolygon(polygon, width, height, sr):
    return arcpy.Polygon(arcpy.Array([arcpy.Point(polygon.trueCentroid.X - width/2,polygon.trueCentroid.Y + height/2),arcpy.Point(polygon.trueCentroid.X - width/2, polygon.trueCentroid.Y - height/2),arcpy.Point(polygon.trueCentroid.X + width/2,polygon.trueCentroid.Y - height/2),arcpy.Point(polygon.trueCentroid.X + width/2,polygon.trueCentroid.Y + height/2)]),sr)

def calculateLabelPostion(featureClassPath, columnName, horizontalWidth, horizontalHeight):
    arcpy.AddError("calculateLabelPostion - start")
    # get spatial reference
    sr = arcpy.Describe(featureClassPath).spatialReference
    rows = arcpy.da.UpdateCursor(featureClassPath, ["SHAPE@",columnName])  
    for row in rows:
        feature = row[0]
        boundary = arcpy.Polygon(feature.boundary().getPart(0),sr)
        # horizontal label field width
        horizontalLabel = generateLabelPolygon(feature, horizontalWidth, horizontalHeight, sr)
        # vertical label field width (flip h & w)
        verticalLabel = generateLabelPolygon(feature, horizontalHeight, horizontalWidth, sr)
        # contains check
        if boundary.contains(horizontalLabel):
            row[1] = "horizontal"
            rows.updateRow(row)
        elif boundary.contains(verticalLabel):
            row[1] =  "vertical"
            rows.updateRow(row)
        else:
            row[1] = "none"
            rows.updateRow(row)
    arcpy.AddError("calculateLabelPostion - end")

try:
    # path to township shapefile feature class (use name if running from arcmap)
    path = "Townships"
    # tileMap zoom level 10 (~ scale in ArcMap 1:600,000)
    arcpy.AddField_management(path, "twpzoom10", "TEXT")
    calculateLabelPostion(path, "twpzoom10", 9000, 2000)

    # tileMap zoom level 11 (~ scale in ArcMap 1:300,000)
    arcpy.AddField_management(path, "twpzoom11", "TEXT")
    calculateLabelPostion(path, "twpzoom11", 6000, 1500)

    # tileMap zoom level 12 (~ scale in ArcMap 1:450,000)
    arcpy.AddField_management(path, "twpzoom12", "TEXT")
    calculateLabelPostion(path, "twpzoom12", 5000, 900)

    # tileMap zoom level 13 (~ scale in ArcMap 1:55,000)
    arcpy.AddField_management(path, "twpzoom13", "TEXT")
    calculateLabelPostion(path, "twpzoom13", 2200, 500)

    # tileMap zoom level 14
    arcpy.AddField_management(path, "twpzoom14", "TEXT")
    calculateLabelPostion(path, "twpzoom14", 1800, 230)

    # tileMap zoom level 15
    arcpy.AddField_management(path, "twpzoom15", "TEXT")
    calculateLabelPostion(path, "twpzoom15", 925, 130)

    # tileMap zoom level 16
    arcpy.AddField_management(path, "twpzoom16", "TEXT")
    calculateLabelPostion(path, "twpzoom16", 420, 60)

    # path to sections shapefile feature class (use name if running from arcmap)
    path = "Sections"
    # tileMap zoom level 13
    arcpy.AddField_management(path, "seczoom13", "TEXT")
    calculateLabelPostion(path, "seczoom13", 407, 407)

    # tileMap zoom level 14
    arcpy.AddField_management(path, "seczoom14", "TEXT")
    calculateLabelPostion(path, "seczoom14", 285, 285)

    # tileMap zoom level 15
    arcpy.AddField_management(path, "seczoom15", "TEXT")
    calculateLabelPostion(path, "seczoom15", 145, 145)

    # tileMap zoom level 16
    arcpy.AddField_management(path, "seczoom16", "TEXT")
    calculateLabelPostion(path, "seczoom16", 60, 60)

    # path to quarters shapefile feature class (use name if running from arcmap)
    path = "Quarters"
    # tileMap zoom level 13
    arcpy.AddField_management(path, "qrtzoom13", "TEXT")
    calculateLabelPostion(path, "qrtzoom13", 380, 380)

    # tileMap zoom level 14
    arcpy.AddField_management(path, "qrtzoom14", "TEXT")
    calculateLabelPostion(path, "qrtzoom14", 285, 285)

    # tileMap zoom level 15
    arcpy.AddField_management(path, "qrtzoom15", "TEXT")
    calculateLabelPostion(path, "qrtzoom15", 145, 145)

except Exception as e:
    print str(e)
