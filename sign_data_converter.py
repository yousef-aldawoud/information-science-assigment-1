import sys
import xlsxwriter
import os

class Converter:
    def __init__(self, data_file, attributes, result_file, label,
                 line_splitter = "\n", attributes_splitter = ","):
        self.label = label
        self.attributes = attributes
        self.line_splitter = line_splitter
        self.attributes_splitter = attributes_splitter
        self.data_file = open(data_file, "r")
        self.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
        self.result_file = result_file
        sss = open(result_file, "w")
        sss.close()

    def convert(self):
        workbook = xlsxwriter.Workbook(self.result_file)
        worksheet = workbook.add_worksheet()
        for count in range(len(self.attributes)):
            worksheet.write(self.columns[count] + '1', self.attributes[count])
        lines = self.get_file_rows(self.data_file, self.line_splitter)
        print(len(lines))
        for i in range(len(lines)):
            attrs = self.get_row_attributes(lines[i], self.attributes_splitter)
            for n in range(len(attrs)):
                worksheet.write(self.columns[n] + str(i + 2), attrs[n])
            worksheet.write(self.columns[len(attr)-1] + str(i + 2), self.label)
        workbook.close()

    @staticmethod
    def get_row_attributes(row, splitter):
        return row.split(splitter)

    @staticmethod
    def get_file_rows(data_file, splitter="\n"):
        return data_file.read().split(splitter)

    def __str__(self):
        return self.data_file


attr = ['x', 'y', 'z', 'roll', 'pitch', 'yaw', 'thumb', 'fore', 'index', 'ring', 'little',
        'keycode', 'gs1', 'gs2', 'receiver values', 'label']

try:
    label = os.path.basename(sys.argv[1])
    if len(sys.argv)<3:
        result_file = sys.argv[1]+".xlsx"
    else:
        result_file = sys.argv[2]
    c = Converter(sys.argv[1], attr, result_file,label)
    c.convert()
except IndexError:

    try:
        data_file = input("What's the data file directory ?")
        result_file = input("What's the result file directory ?")
        label = input("what is the label ?")
        c = Converter(data_file, attr, result_file,label)
        c.convert()
    except FileNotFoundError:
        print('file not found')
