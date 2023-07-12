from datetime import datetime
from webapp import create_app
from webapp.db import db
from webapp.trends.models import Lines

app = create_app()


def add_reccord_in_base(name='Line_name', port=0, adr=16):
    lines = Lines(name=name,
                  port=port,
                  adr=adr,
                  k=1.0,
                  no_connection_counter=False,
                  indikator_value=0,
                  length=0.0,
                  speed_line=0.0,
                  description='',
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
        add_reccord_in_base('Line_1', port=0, adr=101)
        add_reccord_in_base('Line_2', port=0, adr=102)
        add_reccord_in_base('Line_3', port=0, adr=103)
        add_reccord_in_base('Line_4', port=0, adr=104)
        add_reccord_in_base('Line_5', port=0, adr=105)
        add_reccord_in_base('Line_6', port=0, adr=106)
        add_reccord_in_base('Line_7', port=1, adr=107)
        add_reccord_in_base('Line_8', port=1, adr=108)
        db.session.commit()
