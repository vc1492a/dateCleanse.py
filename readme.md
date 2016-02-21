# dateCleanse.py

dateCleanse.py takes a variety of date formats and converts them to a common format: MM/DD/YYYY. This tool is 
still in alpha. Development pace will coincide with its frequency of use for date cleansing in different applications.

## Currently Supported Date Formats

- MM/YYYY
- YYYY/MM
- YYYY-MM
- *YY-MM
- DDDDD (days since 01/01/1900)
- YY/MM
- YY-MM
- YYMM
- YYYY
- M-YY
- M/YY
- YY-M
- MYY
    
Note that two-digit years are assumed to occur post year 2000 and that dates are assumed to occur post 1930 at this time.  

## Date Formats for Future Release

- YYYY-M-DD HH:MM:SS

## How-To

If you are using R, export the column from your data frame or your vector of dates as follows:

```r
write.csv(dates, "dates.csv", row.names=FALSE, quote=FALSE)
```

Ensure that row names and quotes are not included from the R output. 

Then place your your *dates.csv* file is in the same directory as *dateCleanse.py*. Then simply fire up your favorite
Python IDE and hit run. Or from the command line, type:

```python
python dateCleanse.py
```
Cleansed dates will be in a new file called *newDates.csv* contained in the same directory. 

### To-Do
    
- Ensure sure format assumptions are correct for type: 2016-9-01 00:00:00
- Allow user input of source file name
- Ensure robust behavior in different use cases
- Toggle the post-2000 assumption on or off
- Ensure extra line at the end of new csv file is not printed
- Allow batch processing of more than one input file
- Allow processing of multiple columns of data
