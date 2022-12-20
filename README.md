# ElemeNT position weight matrices

ElemeNT was a web app for visualizing core promoter elements (`http://dx.doi.org/10.1080/21541264.2015.1067286`). However, the web API at `http://lifefaculty.biu.ac.il/gershon-tamar/index.php/resources` appears to be down, and I couldn't find the resource elsewhere. I scraped the core promoter element PWMs published in the supplemental materials of the original paper and converted them into `.csv` files.

## Files

```
ktrn-06-03-1067286-s001.zip -     Zip archive of raw supplemental files.
*.csv                       -     Core promoter element PWMs in csv format. Converted from xlsx sheet.
conversion_script.py        -     Converts csv files to txt files like those downloaded from CisBP.
core_promoter_pwms.zip      -     Zip archive of conversion_script.py output.
```