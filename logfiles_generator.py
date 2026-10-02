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