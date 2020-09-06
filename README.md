# CraigMEPTools

This is a set of tools I've been developing to help with some of the more boring parts of my job. It's been a work in progress for many years now, but finally it's all come together. 
See below for an over-view of each function. 
Caution must be taken when working with batches of files as when you press go, this programme will work through them all. Make sure you have backups. 

## Home Screen:
![This is the Home Screen](/Pictures/Home_Page.png?raw=true "Title")

Down the left hand side are links to each of the programmmes. 

## Drawing Renamer:
![This is the Home Screen](/Pictures/Drawing_Renamer.png?raw=true "Title")

This programme helps with the boring task of re-naming files. 
..* Adding text to the start of a file name
..* Adding text to the end of a file name
..* Replacing text within a file name (note - leave the replace text field blank to remove text)
..* Automatically attempting to rename the a file based on a pattern (see description below)
..* Exporting to an Microsoft Excel file so that you can re-name using that programme. You can then import the file names back in to start the rename process. 

Automatically Rename:
This programme assumes all the drawing numbers have the same format (i.e. it won't work on a folder of mis-matched drawings from different people). To do this you type in a sample drawing number from one of the drawings - the programme will then search the text in the drawing for a match, and then suggest it as the new file name. 

## Standards Search:
![This is the Home Screen](/Pictures/Standards_Search.png?raw=true "Title")

This programme extracts text from a PDF, looks for standards, then queries the BSI website for a match. It then returns the top 15 searches along with their name, date and current status. This programme relies on webscraping as no API exists so it is reliant on the BSI website not changing. If it changes this will need to be updated. 
The Standards searched are:
..* BS
..* BS EN
..* EN
..* ISO
..* IEC
..* BSRIABG
..* DW

## Image Tools:
![This is the Home Screen](/Pictures/Image_Tools.png?raw=true "Title")

This programme is for working with images as large batches. It has two main functions:
..* Compressing pictures to different sizes (e.g. for e-mailing)
..* Adding a watermark to the pictures - such as adding a company logo to an image. 
