from datetime import datetime, timedelta
from flask import Blueprint, current_app, render_template
from webapp.tunings.forms import SelectDateForm
from webapp.tunings.models import Lines


blueprint = Blueprint('tunings', '__name__')


@blueprint.route('/tuning_lines', methods=['GET', 'POST'])
def tuning_lines():
    form = SelectDateForm()
    if form.select_date.data:
        select_date = form.select_date.data
    else:
        select_date = datetime.today()
        form.select_date.data = select_date
    # if form.validate_on_submit():
    #     s_begin_time = form.select_date.data
    #     return redirect(url_for('trends.monitor'))
    title = "Настройка счетчиков метража"
    return render_template('tunings/index.html',                           
                           page_title=title, form=form,
                           lines= read_data_in_base(),
                           )


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
            'length' : line.length,
            'speed_line' : line.speed_line,
            'description' : line.description,
            'created_dt' : line.created_dt,
            'updated_dt' : line.updated_dt,
        })
    return params
