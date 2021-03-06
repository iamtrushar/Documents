# AutoMapper Business Logic.

Gets all the legal descriptions records (LW_LEGAL_DESCRIPTION) for the job record (LW_JOB_SCHEDULE) in question. 

- Different type of jobs can be set up for each land grid. AutoMapper can map against the following:
  - Township and range (TR)
    - BLM Geographic Coordinate Data Base (GCDB)
    - Lot Tract (LT)
  - Survey Abstract (SA)
  - Area Block (AB)
  - Dominion Land Survey (DGS)
  - League and Labour (LL)

AutoMapper gets all the layer information about the land grids connection, name, column mapping and spatial reference etc from Lpm db. 
See tables below:
- LW_GIS_CONNECTION
- LW_GIS_GROUP
- LW_GIS_LAYERS
- LW_GIS_SPATIAL_REFERENCE
- LW_GIS_COLUMN_MAPPING 

AutoMapper starts processing the legal descriptions next. 

AutoMapper is configured to map each legal againts parcel land grid (Land Grid type PAR) first. Legal must have parcel number to qualify. 
NOTE: the following configuration for parcel mapping: 
- LW_CODE_CONFIG.CONFIG_VALUE WHERE CONFIG_TYPE = 'AutoMapperParcelFirst'
  N = Will attempt to map parcel if not found then map legal for it's map type.
  Y = Will attempt to map parcel first if not found fail the legal. 

### Township and Range
1. Get all the land grids configured for TR. 
  Loop through each one until legal is found. 
  - Build a search query to get the polygon from Township and section land grid:
    - Try to get Township polygon (WHERE clause generated from legal description: TWP='72' AND TDIR='N' AND RNG='130' AND RDIR='E' AND STATE='WY' AND COUNTY_CODE='001' AND MER=12)
    - Try to get Section polygon using (WHERE clause generated from legal description: SEC=2 AND TWP='72' AND TDIR='N' AND RNG='130' AND RDIR='E' AND STATE='WY' AND COUNTY_CODE='001' AND MER=12) 
    (Note Township polygon is used as spatial filter to narrow down search is enabled)
    (Note County layer, which is optional setup up, is used as spatial filter to narrow down search for township and sections)
2. Once found, check the quarter call in LW_LEGAL_DESCRIPTION.QUARTER_SECTION
  - Quarter futher
  - Quarter call string has `AND` then quarter each string seperatly and then Union the result. 
  - If the quarter call is NULL, empty string, ALL, LEGAL then full section is mapped as is. 

If Meridian `MER` is not set, AutoMapper will find it using State and County values. Vendor is generally used as USGS.

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

(TrusharM will need to review BLM and LT logic)
#### BLM Geographic Coordinate Data Base (GCDB) & Lot Tract (LT)
  - To process GCDB polygon or LT legals, see below for special consideration for generating search query where clause. Where clause will be build in two parts: Land key and lot.
  - For Land Key: Get a formatted Township/range information as land key if land grid does not have Land_Key column. Formatted land key must be: `StateCode + MeridianCode + T + TownhshipNumber + TownshipDirection + RangeNumber + RangeDirection`.
  - For Lot: 
    - If Lot Number is not null or empty, then get Survey Type (T or L). 
      - Survey Type is T if the Lot Number starts with value T else it's L.
      - Survey Type == T
        Check if layerType is GCDB then partial where clause is LOT_NUMBER IN (_lot number values_) AND SURVEY_TYPE = 'T'
        Check if layerType is LT then partial where clause is TRACT_NUMBER IN (_lot number values_) AND SURVEY_TYPE = 'T'
        NOTE: _lot number values_ Padd 0 for lot numbers between 0 and 9. Example WHERE = ... IN ('01', '001', '1'). Pad 00 for lot numbers between 10-99. No padding for lot numbers above 99.
      - Survey Type == L
        Check if layerType is GCDB then partial where clause is LOT_NUMBER IN (_lot number values_) AND SURVEY_TYPE = 'L'
    - Else if Lot number is null     
        Use Quater Section String values.
        - Check if layerType is GCDB 
          - Check the length of the quater section string.
            - If length is > 4 (Trim last 4 quarter calls) and use the remainder of the quarter section to get `nominal location` (see below - TrusharM NOTE add a link instead of code) => _nominallocaiton_
        - Generate the lot where clause: NOMINAL_LOCATION in ( _nominallocaiton_ )  (Step incomplete)
        - Check if layerType is LT 
          - Check the length of the quater section string.
            - If length is > 4 (Trim last 4 quarter calls) and use the remainder of the quarter section to get quarter class list (see below - TrusharM NOTE add a link instea of code). Loop on each quarter call and build a comma sepearted `expanded quarter call list` as: `LandKey+ SectionNumber + expandedQuarterCall)` => _qq_
            - Generate the quartersection where clause: LAND_KEY_QQ in ( _qq_ )    
         - Generate the lot where clause: LAND_KEY_QQ in ( _qq_ ) (Step missing)
            
### Dominion Land Survey (DGS)
1. Get all the land grids configured for LSD (Legal subdivions).
2. Sepcial consideration for formatting the where clause for the search query:
  - On LW_LEGAL_DESCRIPTION or table, look for value in the column LW_LEGAL_DESCRIPTION.BLOCK or LW_LEGAL_DESCRIPTION.LOT_NUMBER:
    If BLOCK is provided, then ignore meridian, township, range, section number (Example: On the LSD_mineral layer, the MER, TWP, RGE, SEC values are null when BLOCK & LOT are provided).
    - If BLOCK is not null and LOT_NUMBER is null, then only need to query on BLOCK, get all the polygons for that block and dissolve (i.e. union them)
    - If BLOCK is not null and LOT_NUMBER is not null, then query on BLOCK & LOT_NUMBER, get polygon for lot
  - Check the value in LW_LEGAL_DESCRIPTION.QUATER_SECTION_STRING *ending* in:
    - Drop if `"NW" || "NE" || "SW" || "SE"`     
    - Replace if N2 as IN ('NW', 'NE')
    Replace if S2 as IN ('SW', 'SE')
    and so on for `"E2" || "W2"`. 

### Area Block (AB)
1. Get all the land grids configured for OFFB (offshore block).
2. Generally mapped as is. No quartering.

### League and Labour (LL)
1. Get all the land grids configured for TXSRV (Texas Survey), TXSRO (Texas Survey Overlap). Currently I do not see any special logic for processing League/Labour.  
NOTE: Something about this algo looks amiss - AM is actually calling Area Block which does not make sense. Need further investigation.

### Tables:
`LW_JOB_SCHEDULE`

JOB_ID | JOB_AUTOMAP_ID | JOB_STATUS | SUBMIT_DATE | START_DATE | START_TIME | END_DATE | RUN_FREQ | RUN_DAY | LAST_RAN_DATE | LAST_UPDATE_DATE | LAST_UPDATE_BY
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---

`LW_LEGAL_DESCRIPTION`:

LEGAL_DESC_ID | AGMT_ID | TRACT_ID | ABSTRACT_NUMBER | ADDRESS | ADDRESS_1 | ADDRESS_2 | ALL_TRACTS | ATTRIBUTE_SOURCE | BLOCK | CITY | COUNTRY_CODE | COUNTY_CODE | DEPOSIT_NUMBER | FED_GROUP_CODE | FORMATTED_LEGAL | LABOR | LAST_REMARK_COUNT | LAST_UPDATE_BY | LAST_UPDATE_DATE | LEAGUE | LEGAL_GROSS_ACRES | LEGAL_REF_ID | LOT_NUMBER | LOT_TYPE_CODE | LSD_NUMBER | MAP_STATUS_CODE | MAP_TYPE | MUNICIPALITY_ID | LEGAL_REF_NAME_ID | OFFSHORE_BLOCK | PARCEL_NUMBER | PARENT_ID | OTHER_LOT_NUMBER | PRIME_MERIDIAN_CODE | PROJECT_ID | QUARTER_SECTION_STRING | RANGE_DIRECTION | RANGE_NUMBER | REF_OFFICE_CODE | ROLL_NUMBER | ROW_WIDTH | ROW_UOM | SECTION_NUMBER | SOURCE_KEY | STATE_CODE | SUBDIV_LOT | SUBDIVISION | SURVEY_NAME | TAX_DISTRICT | TITLE_NUMBER | TOWNSHIP_DIRECTION | TOWNSHIP_NUMBER | TRACT_OWNED | TWP_NAME_ID | TX_BLOCK | TX_LOT_NUMBER | TX_SECTION_NUMBER | UNIT_NUMBER | ZIP_CODE | REQUEST_ID | SURVEY_ID | APPRAISAL_ID | REFERENCE_TYPE | SUBDIV_SECTION | CODE_COUNTY_ID | TX_QUARTER | TX_QUARTER_APPLIES | SPATIAL_ID | UNIT_ID | REGION
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |--- | --- | --- | --- | --- | --- | --- | --- | --- | --- |--- | --- | --- | --- | --- | --- | --- | --- | --- | --- |--- | --- | --- | --- | --- | --- | --- | --- | --- | --- |--- | --- | --- | --- | --- | --- | --- | --- | --- | --- |--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---

`LW_GIS_CONNECTION`

GIS_CONN_ID | CONNECTION_NAME | GDB_SERVER | SDE_SERVICE | GDB_DATABASE | GDB_CONNECTION_TYPE | GDB_USER | GDB_PASSWORD | GDB_PATH | GDB_VERSION | LAST_UPDATE_DATE | LAST_UPDATE_BY
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- 

`LW_GIS_GROUP`

GIS_GROUP_ID | GIS_GROUP_DESC | GIS_CONN_ID | GIS_SPAT_REF_ID | GROUP_USAGE | QUERY_ID | DISABLE_GROUP | GIS_GROUP_TYPE_CODE | VENDOR_CODE | LAST_UPDATE_DATE | LAST_UPDATE_BY | COUNTRY_CODE | GIS_GROUP_QUERY_ID | FEATURE_SERVICE
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- 

`LW_GIS_LAYER`

GIS_LAYER_ID | GIS_GROUP_ID | LAYER_OWNER | LAYER_NAME | SPATIAL_COLUMN | GEOMETRY_TYPE | LAYER_DESC | LAYER_TYPE_CODE | LAYER_CONFIG_CODE | LAST_UPDATE_DATE | LAST_UPDATE_BY | FACILITY_FLAG | SUMMARY_SOURCE_FLAG
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- 

`LW_GIS_COLUMN_MAP`

COLUMN_ID | GIS_LAYER_ID | SEARCH_COLUMN | SOURCE_COLUMN | SOURCE_DATATYPE | LAST_UPDATE_DATE | LAST_UPDATE_BY
--- | --- | --- | --- | --- | --- | --- 

`LW_GIS_SPATIAL_REFERENCE`

GIS_SPAT_REF_ID | GIS_SPAT_REF_DESC | UOM_CODE | ESRI_FACTORY_CODE | LAST_UPDATE_DATE | LAST_UPDATE_BY | DATUM | DATUM_CODE | COORDINATE_SYSTEM | COORD_SYS_CODE
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- 

`Nominal Locations`:
```
                case "S2":
                    nomLocs = "('P','O','L','K','J','I','N','M')";
                    break;
                case "N2":
                    nomLocs = "('D','C','H','G','F','E','B','A')";
                    break;
                case "W2":
                    nomLocs = "('L','K','I','J','H','G','E','F')";
                    break;
                case "E2":
                    nomLocs = "('P','O','M','N','D','C','A','B')";
                    break;
                case "N2S2":
                    nomLocs = "('J','I','N','M')";
                    break;
                case "S2S2":
                    nomLocs = "('K','L','O','P')";
                    break;
                case "E2S2":
                    nomLocs = "('P','O','N','M')";
                    break;
                case "W2S2":
                    nomLocs = "('L','K','J','I')";
                    break;
                case "S2N2":
                    nomLocs = "('D','C','H','G')";
                    break;
                case "N2N2":
                    nomLocs = "('F','E','B','A')";
                    break;
                case "E2N2":
                    nomLocs = "('D','C''B','A')";
                    break;
                case "W2N2":
                    nomLocs = "('H','G','F','E')";
                    break;
                case "S2W2":
                    nomLocs = "('L','K','I','J')";
                    break;
                case "N2W2":
                    nomLocs = "('H','G','E','F')";
                    break;
                case "E2W2":
                    nomLocs = "('I','H','E','L')";
                    break;
                case "W2W2":
                    nomLocs = "('J','K','G','F')";
                    break;
                case "S2E2":
                    nomLocs = "('P','O','M','N')";
                    break;
                case "N2E2":
                    nomLocs = "('D','C','A','B')";
                    break;
                case "E2E2":
                    nomLocs = "('P','M','D','A')";
                    break;
                case "W2E2":
                    nomLocs = "('O','N','C','B')";
                    break;
                case "E2SW":
                    nomLocs = "('I','L')";
                    break;
                case "SE":
                    nomLocs = "('M','N','O','P')";
                    break;
                case "SW":
                    nomLocs = "('I','J','K','L')";
                    break;
                case "NW":
                    nomLocs = "('E','F','G','H')";
                    break;
                case "NE":
                    nomLocs = "('A','B','C','D')";
                    break;
                case "N2NE":
                    nomLocs = "('A','B')";
                    break;
                case "S2NE":
                    nomLocs = "('C','D')";
                    break;
                case "N2NW":
                    nomLocs = "('E','F')";
                    break;
                case "S2NW":
                    nomLocs = "('G','H')";
                    break;
                case "N2SW":
                    nomLocs = "('I','J')";
                    break;
                case "S2SW":
                    nomLocs = "('K','L')";
                    break;
                case "N2SE":
                    nomLocs = "('M','N')";
                    break;
                case "S2SE":
                    nomLocs = "('O','P')";
                    break;
                case "NENE":
                    nomLocs = "('A')";
                    break;
                case "NWNE":
                    nomLocs = "('B')";
                    break;
                case "SWNE":
                    nomLocs = "('C')";
                    break;
                case "SENE":
                    nomLocs = "('D')";
                    break;
                case "NENW":
                    nomLocs = "('E')";
                    break;
                case "NWNW":
                    nomLocs = "('F')";
                    break;
                case "SWNW":
                    nomLocs = "('G')";
                    break;
                case "SENW":
                    nomLocs = "('H')";
                    break;
                case "NESW":
                    nomLocs = "('I')";
                    break;
                case "NWSW":
                    nomLocs = "('J')";
                    break;
                case "SWSW":
                    nomLocs = "('K')";
                    break;
                case "SESW":
                    nomLocs = "('L')";
                    break;
                case "NESE":
                    nomLocs = "('M')";
                    break;
                case "NWSE":
                    nomLocs = "('M')";
                    break;
                case "SWSE":
                    nomLocs = "('O')";
                    break;
                case "SESE":
                    nomLocs = "('P')";
                    break;
                case "W2NE":
                    nomLocs = "('B','C')";
                    break;
                case "W2NW":
                    nomLocs = "('F','G')";
                    break;
                case "W2SE":
                    nomLocs = "('N','O')";
                    break;
                case "W2SW":
                    nomLocs = "('J','K')";
                    break;
                case "E2NE":
                    nomLocs = "('A','D')";
                    break;
                case "E2NW":
                    nomLocs = "('E','H')";
                    break;
                case "E2SE":
                    nomLocs = "('M','P')";
                    break;
```

`Expanded Quarter Call List`:
```
                case "S2":
                    strQQ = "NWSE,NESE,SWSE,SESE,NWSW,NESW,SWSW,SESW";
                    break;
                case "N2":
                    strQQ = "NWNW,NENW,SWNW,SENW,NWNE,NENE,SWNE,SENE";
                    break;
                case "W2":
                    strQQ = "NWNW,NENW,SWNW,SENW,NWSW,NESW,SWSW,SESW";
                    break;
                case "E2":
                    strQQ = "NWNE,NENE,SWNE,SENE,NWSE,NESE,SWSE,SESE";
                    break;
                case "N2S2":
                    strQQ = "NWSW,NESW,NWSE,NESE";
                    break;
                case "S2S2":
                    strQQ = "SWSW,SESW,SWSE,SESE";
                    break;
                case "E2S2":
                    strQQ = "NWSE,NESE,SWSE,SESE";
                    break;
                case "W2S2":
                    strQQ = "NWSW,NESW,SWSW,SESW";
                    break;
                case "S2N2":
                    strQQ = "SWNW,SENW,SWNE,SENE";
                    break;
                case "N2N2":
                    strQQ = "NWNW,NENW,NWNE,NENE";
                    break;
                case "E2N2":
                    strQQ = "NWNE,NENE,SWNE,SENE";
                    break;
                case "W2N2":
                    strQQ = "NWNW,NENW,SWNW,SENW";
                    break;
                case "S2W2":
                    strQQ = "NWSW,NESW,SWSW,SESW";
                    break;
                case "N2W2":
                    strQQ = "NWNW,NENW,SWNW,SENW";
                    break;
                case "E2W2":
                    strQQ = "NENW,SENW,NESW,SESW";
                    break;
                case "W2W2":
                    strQQ = "NWNW,SWNW,NWSW,SWSW";
                    break;
                case "S2E2":
                    strQQ = "NWSE,NESE,SWSE,SESE";
                    break;
                case "N2E2":
                    strQQ = "NWNE,NENE,SWNE,SENE";
                    break;
                case "E2E2":
                    strQQ = "NENE,SENE,NESE,SESE";
                    break;
                case "W2E2":
                    strQQ = "NWNE,SWNE,NWSE,SWSE";
                    break;
                case "SE":
                    strQQ = "NWSE,NESE,SWSE,SESE";
                    break;
                case "SW":
                    strQQ = "NWSW,NESW,SWSW,SESW";
                    break;
                case "NW":
                    strQQ = "NWNW,NENW,SWNW,SENW";
                    break;
                case "NE":
                    strQQ = "NWNE,NENE,SWNE,SENE";
                    break;
                case "N2NE":
                    strQQ = "NWNE,NENE";
                    break;
                case "S2NE":
                    strQQ = "SWNE,SENE";
                    break;
                case "N2NW":
                    strQQ = "NWNW,NENW";
                    break;
                case "S2NW":
                    strQQ = "SWNW,SENW";
                    break;
                case "N2SW":
                    strQQ = "NWSW,NESW";
                    break;
                case "S2SW":
                    strQQ = "SWSW,SESW";
                    break;
                case "N2SE":
                    strQQ = "NWSE,NESE";
                    break;
                case "S2SE":
                    strQQ = "SWSE,SESE";
                    break;
                case "W2NE":
                    strQQ = "NWNE,SWNE";
                    break;
                case "W2NW":
                    strQQ = "NWNW,SWNW";
                    break;
                case "W2SE":
                    strQQ = "NWSE,SWSE";
                    break;
                case "W2SW":
                    strQQ = "NWSW,SWSW";
                    break;
                case "E2NE":
                    strQQ = "NENE,SENE";
                    break;
                case "E2NW":
                    strQQ = "NENW,SENW";
                    break;
                case "E2SE":
                    strQQ = "NESE,SESE";
                    break;
                case "E2SW":
                    strQQ = "NESW,SESW";
                    break;                 
```                    
