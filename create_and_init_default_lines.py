from datetime import datetime
from webapp import create_app
from webapp.db import db
from webapp.tunings.models import Lines
from cfg import LINES_PARAMS

app = create_app()


def add_reccord_in_base(line_params):
    lines = Lines(name=line_params['name'],
                  line_number = line_params['line_number'],
                  port=line_params['port'],
                  adr=line_params['adr'],
                  k=1.0,
                  no_connection_counter=False,
                  indikator_value=0,
                  length=0.0,
                  speed_line=0.0,
                  description=line_params['description'],
                  created_dt=datetime.now(),
                  updated_dt=datetime.now()
                  )
    db.session.add(lines)
    print('Added {}'.format(lines))


def clear_base():
    row_count = Lines.query.count()
    for _ in range(row_count):
        first_record = Lines.query.order_by(Lines.id.asc()).first()
        db.session.delete(first_record)
        print('deleted {}'.format(first_record))


if __name__ == '__main__':
    with app.app_context():
        # clear_base()
        for line_params in LINES_PARAMS:
            add_reccord_in_base(line_params)        
        db.session.commit()
