import csv
from datetime import datetime, timedelta
import os
import time as _time
from webapp import create_app
from wear_lines import read_data_in_base

app = create_app()


def append_in_csv(lines, write_header=True):     
    shift_hours = 8   
    file_name = create_dir(shift_hours=8)
    with open(file_name, mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ";", lineterminator=";\r")
        st_time = str((datetime.now() - timedelta(hours=shift_hours)).hour) + ':' + str(datetime.now().minute) + ':' + str(datetime.now().second)
        if write_header:
            file_writer.writerow(['time'] + [line['name'] for line in lines])
        file_writer.writerow([st_time] + [str(int(line['length'] * 1000)) for line in lines])


def create_dir(shift_hours=0):
    dt = datetime.now() - timedelta(hours=shift_hours)
    year = str(dt.year)
    month = str(dt.month)
    day = str(dt.day)
    file_name = 'Lines_data_' + year + '_' + month + '_' + day + '.csv'
    basedir = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(basedir, 'Data', year, month)
    file_name = os.path.join(path, file_name)
    if not os.path.isdir(path):
        os.makedirs(path)   
    return file_name



if __name__ == '__main__':
    with app.app_context():
        write_header = True
        header_writed_hour = None
        while True:
            if header_writed_hour != datetime.now().hour:
                header_writed_hour = datetime.now().hour 
                write_header = True
            lines = read_data_in_base()
            append_in_csv(lines, write_header)
            write_header = False
            # break
            _time.sleep(60)
