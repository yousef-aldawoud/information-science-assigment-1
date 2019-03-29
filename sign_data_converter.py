import sys
import xlsxwriter
import os


class Converter:

    def __init__(self, data_files, attributes, result_file, person,
                 line_splitter="\n", attributes_splitter=","):
        self.line_count = 0
        self.person = person
        self.attributes = attributes
        self.line_splitter = line_splitter
        self.attributes_splitter = attributes_splitter
        self.data_files = data_files
        self.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']
        self.result_file = result_file

    def convert(self):
        workbook = xlsxwriter.Workbook(self.result_file)
        worksheet = workbook.add_worksheet()
        for count in range(len(self.attributes)):
            worksheet.write(self.columns[count] + '1', self.attributes[count])
        file_count = 0
        for file in self.data_files:
            file_count += 1
            lines = self.get_file_rows(file, self.line_splitter)
            label = file.split("/")[-1].split(".")[0][:-1]
            for i in range(len(lines) - 1):
                self.line_count += 1
                attrs = self.get_row_attributes(lines[i], self.attributes_splitter)
                for n in range(len(attrs)):
                    worksheet.write(self.columns[n] + str(self.line_count + 1), attrs[n])

                worksheet.write(self.columns[len(attr) - 2] + str(self.line_count + 1), label)
                worksheet.write(self.columns[len(attr) - 1] + str(self.line_count + 1), self.person)

        workbook.close()
        print("Converted "+str(len(self.data_files))+" files to "+self.result_file)

    @staticmethod
    def get_row_attributes(row, splitter):
        return row.split(splitter)

    @staticmethod
    def get_file_rows(file, splitter="\n"):
        return open(file, "r").read().split(splitter)

    def __str__(self):
        return self.data_file


attr = ['x', 'y', 'z', 'roll', 'pitch', 'yaw', 'thumb', 'fore', 'index', 'ring', 'little',
        'keycode', 'gs1', 'gs2', 'receiver values', 'label', 'test sample name']

holders = [os.path.join(sys.argv[1],f) for f in os.listdir(sys.argv[1]) if not os.path.isfile(os.path.join(sys.argv[1], f))]
for holder in holders:
    try:
        print(holder)
        person = holder
        data_file = [(os.path.join(holder,f))
                     for f in os.listdir(holder) if os.path.isfile(os.path.join(holder,f))]
        result_file = person.split("/")[1] + "s.xlsx"

        if(len(sys.argv)>=3):
            result_file = os.path.join(sys.argv[2],person.split("/")[1])+".xlsx"
        print(result_file)
        c = Converter(data_file, attr, result_file, person=person)
        c.convert()
    except IndexError:
        print('file not found')
