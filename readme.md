# dateCleanse.py

dateCleanse.py takes a variety of date formats and converts them to a single, common format: MM/DD/YYYY. 

This tool is still in alpha. Development pace will coincide with its frequency of use for date cleansing in 
different applications. Written and tested in Python 3.4.3. 

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
- YYYY-M-DD HH:MM:SS
    
Note that two-digit years are assumed to occur post year 2000 and that dates are assumed to occur post 1930 at this time.  

## Date Formats for Future Release

We do not have any other date formats currently planned for future release. If you'd like to see a different date 
format included for future release, please let us know or submit a pull request. 

## How-To

If you are using R, export the column from your data frame or your vector of dates as follows:

```r
write.csv(dates, "name_of_file.csv", row.names=FALSE, quote=FALSE)
```

Ensure that row names and quotes are not included from the R output. Then, simply fire up your favorite Python IDE 
and hit run. Or from the command line, type:

```python
python dateCleanse.py
```

The script will ask for your the path to your file which contains the dates to be reformatted. If you placed 
your *name_of_file.csv* file in the same directory, simply type:

```python
name_of_file.csv
```

If your file is located in another directory, be sure to specify the correct file path. Then hit enter. The script
will begin reformatting the date values and show a progress bar. Once the process complete, cleansed dates are stored in
 a new file called *newDates.csv*, contained in the same directory as *dateCleanse.py*. 

## Dependencies

- datetime
- tqdm

### To-Do
    
- Toggle the post-2000 assumption on or off
- Ensure extra line at the end of new csv file is not printed
- Allow batch processing of more than one input file
- Allow processing of multiple columns of data
