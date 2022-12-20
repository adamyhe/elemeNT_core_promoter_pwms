# ElemeNT position weight matrices

ElemeNT ([Sloutskin et al., 2015](http://dx.doi.org/10.1080/21541264.2015.1067286)) was a web app for visualizing core promoter elements. However, the [web API](http://lifefaculty.biu.ac.il/gershon-tamar/index.php/resources) appears to be down, and I couldn't find the resource elsewhere. I scraped the core promoter element PWMs published in the supplemental materials of the original paper and converted them into `.csv` files.

## Files

```
ktrn-06-03-1067286-s001.zip -     Zip archive of raw supplemental files.
*.csv                       -     Core promoter element PWMs in csv format.
conversion_script.py        -     Converts csv files to txt files like from CisBP.
core_promoter_pwms.zip      -     Zip archive of conversion_script.py output.
```