Map {
  buffer-size: 512;
}


#townships { 
  [zoom=6],[zoom=7],[zoom=8],[zoom=9] {
    line-width: 0.5px;
  }
  [zoom=10]{
    [twpzoom10 = 'none'] { text-name: ''; }
    [twpzoom10 = 'vertical'] { text-orientation: 90; }
  }
  [zoom=11]{
    [twpzoom11 = 'none'] { text-name: ''; }
    [twpzoom11 = 'vertical'] { text-orientation: 90; }
  }
  [zoom=12]{
    [twpzoom12 = 'none'] { text-name: ''; }
    [twpzoom12 = 'vertical'] { text-orientation: 90; }
  }
  [zoom=13]{
    [twpzoom13 = 'none'] { text-name: ''; }
    [twpzoom13 = 'vertical'] { text-orientation: 90; }
  }
  [zoom=14]{
    [twpzoom14 = 'none'] { text-name: ''; }
    [twpzoom14 = 'vertical'] { text-orientation: 90; }
  }
  [zoom=15]{
    [twpzoom15 = 'none'] { text-name: ''; }
    [twpzoom15 = 'vertical'] { text-orientation: 90; }
  }
  [zoom=16]{
    [twpzoom16 = 'none'] { text-name: ''; }
    [twpzoom16 = 'vertical'] { text-orientation: 90; }
  }
  [zoom=10] {
    text-face-name: 'Arial Bold';
    text-name: [Township_L];
    text-size: 12;
    line-width: 2px;
    text-halo-fill: fadeout(white, 30%);
    text-halo-radius: 2.5;
    text-allow-overlap: true;
  }
  [zoom=11] {
    line-width: 3px;
    text-face-name: 'Arial Bold';
    text-name: [Township_L];
    text-size: 15;
    text-halo-fill: fadeout(white, 30%);
    text-halo-radius: 2.5;
    text-allow-overlap: true;
  }
  [zoom=12] {
    line-width: 4px;
    text-name: [Township_L];
    text-fill: #404040;
    text-face-name: 'Arial Bold';
    text-size: 24;
    text-opacity: 1;
    text-halo-fill: fadeout(white, 10%);
    text-halo-radius: 2.5;
    text-allow-overlap: true;
  }
  [zoom=13], [zoom=14] {
    line-width: 4px;
    text-name: [Township_L];
    text-fill: #404040;
    text-face-name: 'Arial Bold';
    text-size: 32;
    text-opacity: 1;
    text-halo-fill: fadeout(white, 10%);
    text-halo-radius: 3.5;
    text-allow-overlap: true;
  }
  [zoom=15],[zoom=16] {
    line-width: 4px;
    text-name: [Township_L];
    text-fill: #404040;
    text-face-name: 'Arial Bold';
    text-size: 32;
    text-opacity: 1;
    text-halo-fill: fadeout(white, 10%);
    text-halo-radius: 3.5;
    text-allow-overlap: true;
  }
}


#sections{
  [zoom=11],[zoom=12]{
    [Acres < 160] { text-name: ''; }
    }
  [zoom=13] {
    [seczoom13 = 'none'] { text-name: ''; }
    }
  [zoom=14] {
    [seczoom14 = 'none'] { text-name: ''; }
    }
  [zoom=15] {
    [seczoom15 = 'none'] { text-name: ''; }
    }
  [zoom=16] {
    [seczoom16 = 'none'] { text-name: ''; }
    }
 }
#sections {
  [zoom=10] {
    line-width: 0.5px;
    line-color: #A0A0A0;
  }
  [zoom=11] {
    line-width: 1px;
    line-color: #808080;
    text-fill: #808080;
    text-face-name: 'Arial Bold';
    text-name: [Section];
    text-size: 11;
    text-halo-fill: fadeout(white, 30%);
    text-halo-radius: 1.5;
  }
  [zoom=12] {
    line-width: 1px;
    line-color: #404040;
    text-fill: #808080; 
    text-opacity: 1;
    text-face-name: 'Arial Bold';
    text-name: [Section];
    text-size: 16;
    text-halo-fill: fadeout(white, 30%);
    text-halo-radius: 2;
  }
  [zoom=13] {
    line-width: 2px;
    line-color: #404040;
    text-fill: #606060; 
    text-opacity: 1;
    text-face-name: 'Arial Bold';
    text-name: [Section];
    text-size: 24;
    text-halo-fill: fadeout(white, 30%);
    text-halo-radius: 2.5;
  }
  [zoom=14] {
    line-width: 2px;
    line-color: #404040;
    text-fill: #606060; 
    text-opacity: 1;
    text-face-name: 'Arial Bold';
    text-name: [Section];
    text-size: 28;
    text-halo-fill: fadeout(white, 30%);
    text-halo-radius: 2.5;
  }
  [zoom=15],[zoom=16] {
    line-width: 3px;
    line-color: #404040;
    text-fill: #606060; 
    text-opacity: 1;
    text-face-name: 'Arial Bold';
    text-name: [Section];
    text-size: 28;
    text-halo-fill: fadeout(white, 10%);
    text-halo-radius: 3.5;
    text-allow-overlap: true;
  }
}


#quarters {
  [zoom=12]{
    [Acres < 100] { text-name: ''; }
    }
  [zoom=13]{
    [qrtzoom13 = 'none'] { text-name: ''; }
    }
  [zoom=14] {
    [qrtzoom14 = 'none'] { text-name: ''; }
    }
  [zoom=15], [zoom=16] {
    // same size for zoom 15, 16
    [qrtzoom15 = 'none'] { text-name: ''; }
    }
 }
#quarters {  
  [zoom=12] {
    line-width: 0.5px;
    line-color: #606060;
    text-fill: #000000;
    text-face-name: 'Arial Bold';
    text-size: 10;
    text-opacity: 0.35;
    text-name: [Quarter];
    text-halo-fill: fadeout(white, 30%);
    text-halo-radius: 2.5;
  }
  [zoom=13] {
    line-width: 1px;
    line-color: #606060;
    text-fill: #707070;
    text-face-name: 'Arial Bold';
    text-size: 16;
    text-opacity: 1;
    text-name: [Quarter];
    text-halo-fill: fadeout(white, 30%);
    text-halo-radius: 1.5;
  }
  [zoom=14] {
    line-width: 1px;
    line-color: #606060;
    text-fill: #606060;
    text-face-name: 'Arial Bold';
    text-name: [Quarter];
    text-size: 20;
    text-halo-fill: fadeout(white, 30%);
    text-halo-radius: 2.5;
    text-opacity: 1;
  }
  [zoom=15] {
    line-width: 1px;
    line-color: #606060;
    text-fill: #606060;
    text-face-name: 'Arial Bold';
    text-name: [Quarter];
    text-size: 20;
    text-halo-fill: fadeout(white, 30%);
    text-halo-radius: 2.5;
    text-opacity: 1;
  }
  [zoom=16] {
    line-width: 1px;
    line-color: #606060;
    text-fill: #606060;
    text-face-name: 'Arial Bold';
    text-name: [Quarter];
    text-size: 20;
    text-halo-fill: fadeout(white, 30%);
    text-halo-radius: 2.5;
    text-opacity: 1;
  }
}


#qtrqtr{
  [zoom=14] {
    [Acres < 16] { text-name: ''; }
    }
  [zoom=15] {
    [Acres < 8] { text-name: ''; }
    }
  [zoom=16] {
    [Acres < 2] { text-name: ''; }
    }
 }
#qtrqtr {
  [zoom=14] {
    line-width: 0.5px;
    line-color: #A0A0A0;
    text-face-name: 'Arial Bold';
    text-name: [QtrQtr];
    text-size: 11;
    text-fill: #606060;
    text-halo-fill: fadeout(white, 30%);
    text-halo-radius: 1.5;
    }
  
  [zoom=15] {
    line-width: 0.5px;
    line-color: #A0A0A0;
    text-face-name: 'Arial Bold';
    text-name: [QtrQtr];
    text-size: 16;
    text-fill: #606060;
    text-halo-fill: fadeout(white, 30%);
    text-halo-radius: 1.5;
    }
  
   [zoom=16] {
    line-width: 0.5px;
    line-color: #A0A0A0;
    text-face-name: 'Arial Bold';
    text-name: [QtrQtr];
    text-size: 16;
    text-fill: #606060;
    text-halo-fill: fadeout(white, 30%);
    text-halo-radius: 1.5;
    }
  }


#lots{
  [zoom=15] {
    [Acres < 8] { text-name: ''; }
    }
  [zoom=16] {
    [Acres < 2] { text-name: ''; }
    }
 }
#lots {
  [zoom=15],[zoom=16] {
    line-width: 0.5px;
    line-color: #A0A0A0;
    text-face-name: 'Arial Bold';
    text-name: [Lot];
    text-size: 11;
    text-fill: #606060;
    text-halo-fill: fadeout(white, 30%);
    text-halo-radius: 1.5;
    }
  }
