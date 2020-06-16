# import libraries (not needed if running from ArcMap's Python interpreter) 
import arcpy 

def calculateLabelPolygonInMemory(featureClassPath, inMemoryFeatureClassName, w, h):
    polygons = []
    sr = arcpy.Describe(featureClassPath).spatialReference
    with arcpy.da.SearchCursor(featureClassPath,"SHAPE@",spatial_reference=sr) as cursor:
        for row in cursor:
            centroid = row[0].trueCentroid
            polygon = arcpy.Polygon(arcpy.Array([arcpy.Point(centroid.X - w/2,centroid.Y + h/2),arcpy.Point(centroid.X - w/2,centroid.Y - h/2),arcpy.Point(centroid.X + w/2,centroid.Y - h/2),arcpy.Point(centroid.X + w/2,centroid.Y + h/2)]),sr)
            polygons.append(polygon)

    arcpy.CopyFeatures_management(polygons,inMemoryFeatureClassName)

path = "Townships"
# tileMap zoom level 10 (~ scale in ArcMap 1:600,000)
calculateLabelPolygonInMemory(path, r'in_memory\horizontal10', 9000, 2000)
calculateLabelPolygonInMemory(path, r'in_memory\vertical10', 2000, 9000)

# tileMap zoom level 11 (~ scale in ArcMap 1:300,000)
calculateLabelPolygonInMemory(path, r'in_memory\horizontal11', 6000, 1500)
calculateLabelPolygonInMemory(path, r'in_memory\vertical11', 1500, 6000)

# tileMap zoom level 12 (~ scale in ArcMap 1:145,000)
calculateLabelPolygonInMemory(path, r'in_memory\horizontal12', 5000, 900)
calculateLabelPolygonInMemory(path, r'in_memory\vertical12', 900, 5000)

# tileMap zoom level 13 (~ scale in ArcMap 1:55,000)
calculateLabelPolygonInMemory(path, r'in_memory\horizontal13', 2200, 500)
calculateLabelPolygonInMemory(path, r'in_memory\vertical13', 900, 2200)

path = "Sections"
# tileMap zoom level 15 (~ scale in ArcMap 1:18,000)
calculateLabelPolygonInMemory(path, r'in_memory\horizontal15', 1000, 120)
calculateLabelPolygonInMemory(path, r'in_memory\vertical15', 120, 1000)

# tileMap zoom level 16 (~ scale in ArcMap 1:9,000)
calculateLabelPolygonInMemory(path, r'in_memory\horizontal16', 500, 100)
calculateLabelPolygonInMemory(path, r'in_memory\vertical16', 100, 500)