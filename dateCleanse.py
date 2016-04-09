# for number of days since 1900 conversion
import datetime
from tqdm import tqdm
import csv

# ask user to define file path
file_path = input("\nEnter the file path: ")


# function to help check if value is an integer
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


# date cleansing function
def date_cleanse(txt_file):
    try:
        f = open(txt_file, "r") # open the text file
        lines = f.read().split("\n") # define delimiter for each line
        formatted = [] # array to store formatted values
        print('Reformatting date values...')
        for line in tqdm(lines, leave=False):

            if any(character.isalpha() for character in line): # if there are any characters in the line
                formatted.append('NA') # recode to NA

            elif line == '': # if the line is blank
                formatted.append('NA') # recode to NA

            elif len(line) == 19: # if YYYY-MM-DD 00:00:00
                spaceSplit = line.split(' ')
                spaceSplit = spaceSplit[0] # remove 00:00:00
                split = spaceSplit.split('-')
                year = split[0]
                month = split[1]
                day = split[2]
                date = month + "/" + day + "/" + year
                formatted.append(date)

            elif len(line) == 7:
                if '/' in line and ' ' not in line: # if yyyy/mm or mm/yyyy
                    split = line.split('/')
                    if len(split[0]) == 4: # if the year is before /
                        year = split[0]
                        month = split[1]
                        date = str(month) + "/01/" + str(year)
                        formatted.append(date)
                    elif len(split[0]) == 2: # if the month is before /
                        year = split[1]
                        month = split[0]
                        date = str(month) + "/01/" + str(year)
                        formatted.append(date)
                    # @Note: Added to ensure not missing cases
                    else:
                        formatted.append('NA')
                elif '-' in line and ' ' not in line: # if yyyy-mm
                    split = line.split('-')
                    year = split[0]
                    month = split[1]
                    date = str(month) + "/01/" + str(year)
                    formatted.append(date)
                # @Note: Added to ensure not missing cases
                else:
                     formatted.append('NA')

            elif len(line) == 6:
                if line[0] == "*" and '-' in line: # if *yy-mm
                    line = line[1:]  # remove the asterisk *
                    split = line.split('-')
                    month = split[1]
                    year = "20" + split[0] # assume these years are after year 2000
                    date = month+"/01/"+year
                    formatted.append(date)
                # @Note: Added to ensure not missing cases
                else:
                    formatted.append('NA')

            elif len(line) == 5:
                if line[0] == "4" and '/' not in line: # if ddddd (days since 01/01/1900)
                    date = datetime.date(1900, 1, 1) + datetime.timedelta(int(line)) # calculate date
                    date = date.strftime("%d/%m/%Y") # convert to proper format
                    formatted.append(date)
                elif '/' in line: # if yy/mm
                    split = line.split('/')
                    if split[0].isalpha() or split[1].isalpha():
                        formatted.append('NA')
                    elif split[0] == '00' or split[1] == '00' or split[0] == '0' or split[1] == '0':
                        formatted.append('NA')
                    elif split[0] == '??' or split[1] == '??':
                        formatted.append('NA')
                    else:
                        year = "20" + split[0] # assume these years are after year 2000
                        month = split[1]
                        date = str(month) + "/01/" + str(year)
                        formatted.append(date)
                elif '-' in line: # if yy-mm
                    split = line.split('-')
                    if split[0] == "00" and split[1] == "00":
                        formatted.append("NA")
                    else:
                        year = "20" + split[0] # assume these years are after year 2000
                        month = split[1]
                        date = month + "/01/" + year
                        formatted.append(date)
                #@Note: Added to ensure not missing cases
                else:
                    formatted.append('NA')

            elif len(line) == 4:
                if line.isdigit(): # if yymm or yyyy
                    if line[0] + line[1] == "20": # yyyy
                        date = "01/01/" + line # if only year value, assign to first day of year
                        formatted.append(date)
                    elif line[0] + line[1] > "20":
                        formatted.append('NA') # if greater than 20, date value unknown
                    else: # yymm
                        year = "20" + line[:2] # assume these years are after year 2000
                        month = line[2:4]
                        date = month + "/01/" + year
                        formatted.append(date)
                elif '/' in line: # if m/yy
                    split = line.split('/')
                    year = "20" + split[0] # assume these years are after year 2000
                    month = split[1]
                    date = month + "/01/" + year
                    formatted.append(date)
                elif '-' in line and line[1] == '-': # if m-yy
                    split = line.split('-')
                    year = "20" + split[0] # assume these years are after year 2000
                    month = split[1]
                    date = month + "/01/" + year
                    formatted.append(date)
                elif '-' in line and line[2] == '-': # if yy-m
                    split = line.split('-')
                    if split[0] == '00' or split[1] == '00' or split[0] == '0' or split[1] == '0':
                        formatted.append('NA')
                    else:
                        year = "20" + split[0] # assume these years are after year 2000
                        month = split[1]
                        date = month + "/01/" + year
                        formatted.append(date)
                #@Note: Added to ensure not missing cases
                else:
                    formatted.append('NA')

            elif len(line) == 3:
                if '-' not in line: # if myy:
                    if line[1] == '\\':
                        formatted.append('NA')
                    else:
                        month = line[0]
                        year = "20" + str(line[1] + line[2])
                        date = month + "/01/" + year
                        formatted.append(date)
                #@Note: Added to ensure not missing cases
                else:
                    formatted.append('NA')
            else:
                formatted.append('NA') # add NA for remaining cases

        # check for erroneous errors (e.g. month > 12)
        # for now let's do all of this here
        for index, date in enumerate(formatted):
            if '/' in date: # Take dates only and not NAs
                split = date.split('/')
                # Check if month can be converted to int
                month = split[0]
                if is_int(month):
                    month = int(month)
                    if month > 12 or month <= 0: # check if have months not between 1 and 12
                        formatted[index] = 'NA'
                else:
                    formatted[index] = 'NA'

        # write formatted contents to csv
        with open('newDates.csv', 'w') as export:
            writer = csv.writer(export)
            print('Saving the reformatted date values...')
            for i in tqdm(formatted): # for every entry in the formatted array
                row = [i]
                writer.writerow(row) # write the entry to the file

        print('\nConversion complete. Formatted dates stored in "newDates.csv".\n')

    except FileNotFoundError:
        print('\nFile not found. Please check the file path and try again.')
    except NameError:
        print('\nDependencies not met. Please check to ensure the datetime and tqdm modules are installed.')

date_cleanse(file_path)
