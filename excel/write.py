import json
import xlwt

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('Sheet1')
with open('student.txt') as fp:
    info = json.load(fp)

    for i, key in enumerate(info):
        worksheet.write(i, 0, key)
        for j in range(len(info[key])):
            worksheet.write(i, j + 1, info[key][j])

workbook.save('student.xls')