# Gis Functional Domain Model

## Requirements

Retrive geometry (polygon) from database for a given legal description string.  
The legal description can be of type Township/Range, (Survey/Abstract and Geographic Coordinate System to be desinged in later phase). 

- Legal description for Township/Range must have State, County, Township number, Township direction, Range number, Range direction. 
  - Meridian value is optional for input
    - Meridian value must be determined by State and County.
  - Quarter call value is optional
    - The polygon retrived may need to be quartered if the legal description contains quarter call.

(Following TBD later)
- Legal description for Abstract must have State (default value Texas), County and Abstract number (if Abstract polygon needs to be retived)
- Legal description for Sections must have State (default value Texas), County and Section number (if Survey polygon needs to be retived)
- Legal description for Block must have State (default value Texas), County and Block number (if Block polygon needs to be retived)


```

type Option<`T> =
    | Some of `T
    | None


type LegalDescription = LegalDescription of string
let createLegalDescription (l:string) =
    if l.length <= 100
    then Some (LegalDescription l)
    else None
createLegalDescription:
    string -> LegalDescription option

type ValidatedTownshipDirection = ValidatedTownshipDirection of string
type createValidatedTownshipDirection = 
    (LegalDescripotion * ParsingTownshipDirectionLogic) -> ValidatedTownshipDirection option

type ValidatedTownship = ValidatedTownship of string
type createValidatedTownship = 
    (LegalDescripotion * ParsingTownshipLogic) -> ValidatedTownship option

type ValidatedRange = ValidatedRange of string
type createValidatedRange = 
    (LegalDescripotion * ParsingRangeLogic) -> ValidatedRange option

type ValidatedRangeDirection = ValidatedRangeDirection of string
type createValidatedRangeDirection = 
    (LegalDescripotion * ParsingRangeDirectionLogic) -> ValidatedRangeDirection option

type ValidatedCounty = ValidatedCounty of string
type createValidatedRange = 
    (LegalDescripotion * ParsingCountyLogic) -> ValidatedCounty option

type ValidatedState = ValidatedState of string
type createValidatedState = 
    (LegalDescripotion * ParsingStateLogic) -> ValidatedState option

type ValidatedMeridian = ValidatedMeridian of string
type createValidatedMeridian = 
    (LegalDescripotion * ParsingMeridianLogic) -> ValidatedMeridian option

type ValidatedSection = ValidatedSection of string
type createValidatedSection = 
    (LegalDescripotion * ParsingSectionLogic) -> ValidatedSection option

type ValidatedQuarterCall = ValidatedQuarterCall of string
type createValidatedQuarterCall = 
    (LegalDescripotion * ParsingQuarterCallLogic) -> ValidatedQuarterCall option


type Township = {
    TownshipNumber: ValidatedTownship
    TownshipDirection: ValidatedTownshipDirection
    RangeNumber: ValidatedRange
    RangeDirection: ValidatedRangeDirection    
    Meridina: ValidatedMeridian
}
type Section = {
    TownshipNumber: ValidatedTownship
    TownshipDirection: ValidatedTownshipDirection
    RangeNumber: ValidatedRange
    RangeDirection: ValidatedRangeDirection    
    Meridina: ValidatedMeridian
    Section: ValidatedSection
    QuarterCall = ValidatedQuarterCall
}
type TownshipSectionInfo =
    | Township
    | Section
    | TownshipAndSection of (Township * Section)
type TownshipSection = {
    State: Abbrivation
    County: PaddedString
    TownshipSectionInfo: TownshipSectionInfo
}


type Polygon = Geometry
type TownshipTable = Polygon list
type SectionTable = Polygon list
type GetTownshipPolygon = (TownshipSection * TownshipTable) -> Polygon
type GetSectionPolygon = (TownshipSection * SectionTable) -> Polygon
type Quartering = (GetTownshipPolygon * GetSectionPolygon) -> Polygon option


```
