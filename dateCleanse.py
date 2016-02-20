import tqdm # for timing
import re # for string matching
import csv


def dateCleanse(txt_file):
    f = open(txt_file, "r") # open the text file
    lines = f.read().split("\n") # define delimiter for each line
    formatted = []
    for line in lines:

        if line.isalpha(): # if anything is entirely string
            formatted.append('NA') # recode to NA

        elif line.strip() == '': # if the line is blank
            formatted.append('NA') # recode to NA

        elif len(line) == 7 and '/' in line and ' ' not in line: # if yyyy/mm or mm/yyyy
            split = line.split('/')
            year = 0
            month = 0
            if len(split[0]) == 4 or len(split[1]) == 4:
                year = split[0]
                if len(year) == 2:
                    year = "20" + year
            elif len(split[0]) == 2 or len(split[1]) == 2:
                month = split[0]
            date = str(month) + "/01/" + str(year)
            formatted.append(date)

        elif len(line) == 5 and '/' in line: # if yy/mm
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


        elif len(line) == 5 and '-' in line: # if yy-mm
            split = line.split('-')
            if split[0] == "00" and split[1] == "00":
                formatted.append("NA")
            else:
                year = "20" + split[0] # assume these years are after year 2000
                month = split[1]
                date = month + "/01/" + year
                formatted.append(date)


##### THIS SHOULD BE len(line) == 4
# When changed, get error below ..

        elif len(line) == 3 and '/' in line: # if m/yy
            print(line)
            if split[0].isalpha() or split[1].isalpha():
                formatted.append('NA')
            elif split[0] or split[1] == 'A':
                formatted.append('NA')
            else:
                split = line.split('/')
                year = "20" + split[1] # assume these years are after year 2000
                month = split[0]
                date = month + "/01/" + year
                print(date)
                formatted.append(date)

        elif len(line) == 3 and '-' in line: # if yy-m
            if split[0].isalpha() or split[1].isalpha():
                formatted.append('NA')
            elif split[0] or split[1] == '20N':
                formatted.append('NA')
            else:
                split = line.split('-')
                propformat = 0
                year = "20" + split[0] # assume these years are after year 2000
                propformat += ((float(year) - 1900) * 365)
                month = split[1]
                propformat += float(month) * 30
                propformat = str(round(propformat)).rstrip('.')
                formatted.append(propformat)

        elif len(line) == 7 and '-' in line: # if yyyy-mm
            split = line.split('-')
            propformat = 0
            year = split[0]
            propformat += ((float(year) - 1900) * 365)
            month = split[1]
            propformat += float(month) * 30
            propformat = str(round(propformat)).rstrip('.')
            formatted.append(propformat)

        elif len(line) == 3 and '-' not in line: # if myy:
            if line[0] == 'N':
                formatted.append('NA')
            elif line[1] == '\\':
                formatted.append('NA')
            else:
                month = line[0]
                propformat = 0
                propformat += float(month) * 30
                year = str(line[1] + line[2])
                if int(year) < 20:
                    year = "20" + year # assume these years are after year 2000
                    propformat = 0
                    propformat += ((float(year) - 1900) * 365)
                    propformat = str(round(propformat)).rstrip('.')
                    formatted.append(propformat)
                else:
                    formatted.append('NA')

        elif len(line) == 6 and line[0] == "*" and '-' in line: # if *yy-mm
            #remove the *
            line = line[1:]
            split = line.split('-')
            propformat = 0
            month = split[1]
            year = "20" + split[0]
            date = month+"/01/"+year

        elif len(line) == 4 and line.isdigit(): #yymm or yyyy
            # Check if yymm or yyyy
            if line[0] + line[1] == "20": #yyyy
                date = "01/01/"+line
            elif line[0] + line[1] > "20":
                date = 'NA'
            else: # yymm
                year = "20" + line[:2]
                month = line[2:4]
                date = month + "/01/" + year

        ## remaining use cases
        # 0-0
        # 2016-9-01 00:00:00

        else:
            formatted.append(line) # include the original value if it does not meet these use cases

    #for i in formatted:
     #   print(i)

    return formatted

words = dateCleanse('dates.csv')

#print(words)