import arcpy  # import libraries (not needed if running from ArcMap's Python interpreter)


def generateLabelPolygon(polygon, width, height, sr):
    return arcpy.Polygon(arcpy.Array(
        [arcpy.Point(polygon.trueCentroid.X - width / 2, polygon.trueCentroid.Y + height / 2),
         arcpy.Point(polygon.trueCentroid.X - width / 2, polygon.trueCentroid.Y - height / 2),
         arcpy.Point(polygon.trueCentroid.X + width / 2, polygon.trueCentroid.Y - height / 2),
         arcpy.Point(polygon.trueCentroid.X + width / 2, polygon.trueCentroid.Y + height / 2)]), sr)


def addFields(featureClassPath, inDimensions):
    columns = ["SHAPE@"]
    lstFields = arcpy.ListFields(featureClassPath)
    fieldNames = [f.name for f in lstFields]
    for item in inDimensions:
        column = item[0]
        columns.append(column)
        if column in fieldNames:
            print "Column: " + column + ", exists."
        else:
            print "Column: " + column + ", does not exist. Adding..."
            arcpy.AddField_management(featureClassPath, column, "TEXT")
    return columns


def calculateLabelPosition(featureClassPath, inDimensions, inColumnArray):
    print "Calculating label positions for " + featureClassPath
    # get spatial reference
    sr = arcpy.Describe(featureClassPath).spatialReference
    rows = arcpy.da.UpdateCursor(featureClassPath, inColumnArray)
    for row in rows:
        feature = row[0]
        boundary = arcpy.Polygon(feature.boundary().getPart(0), sr)
        i = 1
        for item in inDimensions:
            horizontalWidth = item[1]
            horizontalHeight = item[2]

            # horizontal label field width
            horizontalLabel = generateLabelPolygon(feature, horizontalWidth, horizontalHeight, sr)
            # vertical label field width (flip h & w)
            verticalLabel = generateLabelPolygon(feature, horizontalHeight, horizontalWidth, sr)
            # contains check
            if boundary.contains(horizontalLabel):
                row[i] = "horizontal"
                rows.updateRow(row)
            elif boundary.contains(verticalLabel):
                row[i] = "vertical"
                rows.updateRow(row)
            else:
                row[i] = "none"
                rows.updateRow(row)
            i = i + 1
    print "Done."


# path to township shapefile feature class (use name if running from ArcMap)
path = r"E:\localShapeFiles\forTileLayers\ByStates-5-28-2020\AL-1\Townships.shp"

# tileMap zoom level 10 (~ scale in ArcMap 1:600,000)
# tileMap zoom level 11 (~ scale in ArcMap 1:300,000)
# tileMap zoom level 12 (~ scale in ArcMap 1:450,000)
# tileMap zoom level 13 (~ scale in ArcMap 1:55,000)
# tileMap zoom level 14 (~ scale in ArcMap 1:36,000)
# tileMap zoom level 15 (~ scale in ArcMap 1:18,000)
# tileMap zoom level 16 (~ scale in ArcMap 1:9,000)
dimensions = (("twpzoom10", 9000, 2000),
              ("twpzoom11", 6000, 1500),
              ("twpzoom12", 5000, 900),
              ("twpzoom13", 2200, 500),
              ("twpzoom14", 1800, 230),
              ("twpzoom15", 925, 130),
              ("twpzoom16", 420, 60))

columnArray = addFields(path, dimensions)
calculateLabelPosition(path, dimensions, columnArray)

# path to sections shapefile feature class (use name if running from ArcMap)
path = r"E:\localShapeFiles\forTileLayers\ByStates-5-28-2020\AL-1\Sections.shp"
dimensions = (("seczoom13", 407, 407),
              ("seczoom14", 285, 285),
              ("seczoom15", 145, 145),
              ("seczoom16", 60, 60))

columnArray = addFields(path, dimensions)
calculateLabelPosition(path, dimensions, columnArray)

# path to quarters shapefile feature class (use name if running from ArcMap)
path = r"E:\localShapeFiles\forTileLayers\ByStates-5-28-2020\AL-1\Quarters.shp"

dimensions = (("qrtzoom13", 380, 380),
              ("qrtzoom14", 285, 285),
              ("qrtzoom15", 145, 145),
              ("qrtzoom16", 60, 60))

columnArray = addFields(path, dimensions)
calculateLabelPosition(path, dimensions, columnArray)
