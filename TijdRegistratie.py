import xlrd

#ask username and date from DATASysteem
lastnameTR = input("Enter last name from timeregistration: ")
print("Recieved last name: "+ lastnameTR)
print('\n')

dateTR = input("Enter date and end with '#' : ")
print("Recieved date from TR: "+dateTR)
print('\n')

#open workbook and sheet
workbook = xlrd.open_workbook("<filename>")
worksheet = workbook.sheet_by_name("TR")
count = 0

#if username is equal to collum data print row
print("%-5s %-10s %-25s,%-20s,%-10s" %('Uren:','Ordernr:','Order Activ.:','Datum TR:','Data Activ.:'))
for row_num in range(worksheet.nrows):
    row_value = worksheet.row_values(row_num)
    if (row_value[4] == lastnameTR) and (row_value[0] == dateTR):
        count += row_value[1]
        print("%-5s %-10s %-25s,%-20s,%-10s " % (row_value[1], row_value[5], row_value[7], row_value[0],row_value[8]))

#Print Total hours
print('\n')
print('Total minutes', count)
print('Total hours', (count // 60))
