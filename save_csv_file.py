import csv
from datetime import datetime


def append_in_csv(lines):        
    file_name = 'Line_data_' + str(datetime.now().year) + '_' + str(datetime.now().month) + '_' + str(datetime.now().day) + '.csv'
    with open(file_name, mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ";", lineterminator=";\r")
        file_writer.writerow([line['name'] for line in lines])
        file_writer.writerow([line['length'] for line in lines])

