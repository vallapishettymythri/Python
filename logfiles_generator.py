#log files- csv file
#1.read one by one files
#create 10 files- file handling concepts
#1.eid
#2.ename
#3.activity- 1.work data base
        #2. check the validation
        #3. test model
        #4. taken the gate way connection
#one by one iterate the file and print all the activities of that files.


import csv
files = [
    r"C:\Users\HP\OneDrive\Desktop\Practice\logfiles\file1.csv",
    r"C:\Users\HP\OneDrive\Desktop\Practice\logfiles\file2.csv"
]
def read_logs(files):
    for filename in files:
        file = open(filename, "r")
        reader = csv.reader(file)

        for row in reader:
            yield row[2]

        file.close()
call=read_logs(files)
next(call)