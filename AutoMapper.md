# AutoMapper Business Logic.

Gets all the legal descriptions record for the job in question. 
LW_LEGAL_DESCRIPTION
LW_JOB_SCHEDULE

- Job types can be:
  - Township and range (TR)
  - Survey Abstract (SA)
  - Area Block (AB)
  - BLM Geographic Coordinate Data Base (GCDB)
  - Dominion Land Survey (DGS)
  - Lot Tract (LT)
  - League and Labour (LL)

AutoMapper gets all the layer information about the land grids connection, name, column mapping and spatial reference etc from Lpm db. 
See tables below:
- LW_GIS_CONNECTION
- LW_GIS_GROUP
- LW_GIS_LAYERS
- LW_GIS_SPATIAL_REFERENCE
- LW_GIS_COLUMN_MAPPING 

AutoMapper starts processing the legal descriptions next. 

AutoMapper has a configuraiton where it will attempt to map againts parcel land grid (Land Grid type PAR) when configured for each legal that has parcel number. 
LW_CODE_CONFIG.CONFIG_VALUE WHERE CONFIG_TYPE = 'AutoMapperParcelFirst'
N = Will attempt to map parcel if not found then map legal for it's map type.
Y = Will attempt to map parcel first if not found fail the legal. 

### Township and Range
1. Get all the land grids configured for TR. 
  Loop through each one until legal is found. 
  - Build a search query to get the polygon from Township and section land grid:
    - Try to get Township polygon (WHERE clause generated from legal description: TWP='72' AND TDIR='N' AND RNG='130' AND RDIR='E' AND STATE='WY' AND COUNTY_CODE='001')
    - Try to get Section polygon using (WHERE clause generated from legal description: SEC=2 AND TWP='72' AND TDIR='N' AND RNG='130' AND RDIR='E' AND STATE='WY' AND COUNTY_CODE='001') 
    (Note Township polygon is used as spatial filter to narrow down search is enabled)
    (Note County layer, which is optional setup up, is used as spatial filter to narrow down search for township and sections)
2. Once found, check the quarter call in LW_LEGAL_DESCRIPTION.QUARTER_SECTION
  - Quarter futher
  - Quarter call string has `AND` then quarter each string seperatly and then Union the result. 
  - If the quarter call is NULL, empty string, LEGAL then full section is mapped as is. 
    
### Survey Abstract
1. Get all the land grids configured for SA.
- Land gird layer type codes supported for Abstracts: 
  TXABS (Primary)
  JRABS (Secondary)
- Land gird layer type codes supported for Sections:  
  TXSEC (Primary)
  JRSEC (Secondary)
- Land gird layer type code supported for Blocks:  
  TXBLK (Primary)
2. Before starting to map, test the LW_LEGAL_DESCRIPTON.TX_QUARTER_APPLIES value: 
  - TX Abstract (Map only against texas abstract layer and must have LW_LGEAL_DESCRIPTION.ABSTRACT_NUMBER not null or empty)
  - TX Section (Map only against texas section layer and must have LW_LGEAL_DESCRIPTION.TX_SECTION_NUMBER not null or empty)
  Note: If abstract number, section number is null and tx_block number is NOT null for the legal, then map against texas block layer.
3. Legal is attempted to be mapped with primary land gird first. If legal is not found then retry with secondary land grid. 
4. Texas land gird polygon can have quarter call for west texas with angle tolerance. 

### Area Block (AB)
### BLM Geographic Coordinate Data Base (GCDB)
### Dominion Land Survey (DGS)
### Lot Tract (LT)
### League and Labour (LL)

