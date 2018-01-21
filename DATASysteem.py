import xlrd

#ask username and date from DATASysteem
username = input("Enter username from DATASysteem: ")
print("Recieved username: "+username)
print('\n')

dateDATASysteem = input("Enter date and end with '#' : ")
print("Recieved date "+dateDATASysteem)
print('\n')

#open workbook and sheet
workbook = xlrd.open_workbook("/Users/LorenzoRozenblad/Desktop/Marchano/file.xlsx")
worksheet = workbook.sheet_by_name("DATASysteem")
count = 0

#if username is equal to collum data print row
print("%-10s %-10s %-10s" %('Minuten:','ordernr:', 'Datum DataSysteem:'))
for row_num in range(worksheet.nrows):
    row_value = worksheet.row_values(row_num)
    if (row_value[20] == username) and (row_value[6] == dateDATASysteem):
        count += row_value[4]
        print("%-10s %-10s %-10s " % (row_value[4], row_value[0], row_value[6]))

#Print Total hours
print('\n')
print('Total minutes', count)
print('Total hours', (count // 60))

