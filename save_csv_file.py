import csv
from datetime import datetime, timedelta
import os


def append_in_csv(lines):        
    file_name = create_dir()
    with open(file_name, mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ";", lineterminator=";\r")
        st_time = str(datetime.now().hour) + ':' + str(datetime.now().minute) + ':' + str(datetime.now().second)
        file_writer.writerow(['time'] + [line['name'] for line in lines])
        file_writer.writerow([st_time] + [line['length'] for line in lines])

def create_dir():
    dt = datetime.now() - timedelta(hours=8)
    year = str(dt.year)
    month = str(dt.month)
    day = str(dt.day)
    file_name = 'Line_data_' + year + '_' + month + '_' + day + '.csv'
    basedir = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(basedir, 'Data', year, month, day)
    file_name = os.path.join(path, file_name)
    if not os.path.isdir(path):
        os.makedirs(path)   
    return file_name