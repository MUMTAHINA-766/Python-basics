#comma separated value
import csv
"""
file = open('D:\Soft\Documents\Django projects\Python basics\example.csv')
file_reader = csv.reader(file)
print(file_reader)


#data = list(file_reader)
#print(data)


for row in file_reader:
    print('Row no= '+str(file_reader.line_num)+ ' ' +str(row))
"""
#create data
"""
output_file = open('D:\Soft\Documents\Django projects\Python basics\out.csv', 'w', newline='')
output_writer = csv.writer(output_file)
output_writer.writerow(['ID','Name','Class','gender'])
output_file.close()
"""
#append data
output_file = open('D:\Soft\Documents\Django projects\Python basics\out.csv', 'a', newline='')
output_writer = csv.writer(output_file)
output_writer.writerow(['3','Suhi','2019','F'])
output_file.close()

