# CSV stands for comma seperated values
# allow us to put data into a text file which has a delimiter which is usually a comma, to seperate the different fields
import csv

csv_file = open('sample_data.csv', 'r') # open the file first in the read format to get it started
# csv_reader = csv.reader(csv_file) # put file in a custom reader that reads csv files
# # next(csv_reader) # skip over the first iteration

new_file = open('new_names.csv', 'w') # create a new file to write to
# csv_writer = csv.writer(new_file, delimiter='\t') # create a customer writer to write to csv files, can specify delimeter

# for index,line in enumerate(csv_reader): # need to iterate through csv_rader, gives us lists of each comma seperated value
#    csv_writer.writerow(line)



# new_file.close()
# print(csv_reader)

# can also use a DictReader
csv_reader = csv.DictReader(csv_file) # puts all table and rows into a dictionary, easier to pull and see information
field_names = ['ID','Name','Email']
csv_writer = csv.DictWriter(new_file, fieldnames=field_names, delimiter='\t')
csv_writer.writeheader()
for line in csv_reader:
    del line['Phone Number'] # get rid of the keys that are not there or create a new obj and pass it through
    # del line['Date of Birth']
    # del line['Address']
    # del line['Salary']
    csv_writer.writerow(line)



csv_file.close()

