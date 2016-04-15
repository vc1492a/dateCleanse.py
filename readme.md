# dateCleanse.py

dateCleanse.py converts a variety of date formats and to a single, common format: MM/DD/YYYY.

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

Export a single column from your data frame or your vector of dates into the directory *input_data*. If you 
are using R, you can export the files to that directory individually as follows:

```r
# include the dates you wish to reformat in the directory titled input_data
setwd("C:/user/folder/input_data")
# repeat the following write command for all the files you want to reformat
write.csv(dates, "name_of_file.csv", row.names=FALSE, quote=FALSE)
```

Your working directory will be different depending on your system configuration. Ensure that row names and quotes are 
not included from the R output. Then, simply fire up your favorite Python IDE and hit run. 
Or from the command line, type:

```python
python dateCleanse.py
```

The script will ask for the path to the directory which contains the dates to be reformatted. If you placed 
your *name_of_file.csv* file in the same directory, simply type:

```python
input_data
```
and hit enter (this step may seem trivial but allows for flexibility if your files are in a different directory).

The script will begin reformatting the date values and show several progress bars. Once the process complete, 
cleansed dates are stored in a new file called *newDates.csv*, contained in a new directory titled *output_data*. 

## Non-native Dependencies

- tqdm

### To-Do
    
- Toggle the post-2000 assumption on or off
- Allow processing of multiple columns of data
- Multiprocessing for increased performance
