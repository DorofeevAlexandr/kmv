from datetime import datetime
from cfg import LINES_PARAMS
from read_counter import read_input_registers_modbus_device, get_conection, get_indikator_value
import time as _time

from webapp import create_app
from webapp.db import db
from webapp.tunings.models import Lines



COUNTER_SIMULATION = False


app = create_app()


def read_all_lines(lines):
    for line in lines:
        if line['port'] == 0:
            port = '/dev/ttyS0'
        elif line['port'] == 1:
            port = '/dev/ttyS1'
        else:
            port = None

        registers = read_input_registers_modbus_device(port=port,
                                                    slave_adr=line['adr'])
        
        if COUNTER_SIMULATION:
            ind_value = datetime.now().second
            conected = False
        else:
            ind_value = get_indikator_value(registers)
            conected = get_conection(registers)

        length = ind_value * line['k'] / 1000.0
        update_line_in_base(line, 
                            ind_value=ind_value,
                            conected=conected,
                            length=length)
        line['length'] = length
        # print(length)
        

def read_data_in_base():
    params = []
    lines = Lines.query.filter().all()
    for line in lines:
        params.append({
            'id' : line.id,
            'line_number' : line.line_number,
            'name' : line.name,
            'port' : line.port,
            'adr' : line.adr,
            'k' : line.k,
            'no_connection_counter' : line.no_connection_counter,
            'indikator_value' : line.indikator_value, 
            'length' : line.length,
            'speed_line' : line.speed_line,
            'description' : line.description,
            'created_dt' : line.created_dt,
            'updated_dt' : line.updated_dt,
        })
    return params



def update_line_in_base(line_params, ind_value=0, conected=False, length=0):
    line_number = line_params['line_number']
    line = Lines.query.filter(Lines.line_number==line_number).first()
    if line:
        line.indikator_value = ind_value
        line.no_connection_counter = not conected
        line.length = length
        line.speed_line = 0.0
        line.updated_dt=datetime.now()
        db.session.add(line)
        db.session.commit()       


def read_and_save_in_base():
    lines = read_data_in_base()
    read_all_lines(lines)


if __name__ == '__main__':
    with app.app_context():
        while True:
            lines = read_data_in_base()
            read_all_lines(lines)
            # break
            _time.sleep(15)
