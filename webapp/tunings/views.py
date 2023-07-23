from datetime import datetime, timedelta
from flask import Blueprint, current_app, redirect, render_template, url_for
from webapp.db import db
from webapp.tunings.forms import SelectLineForm, TuningSelectLineForm
from webapp.tunings.models import Lines


blueprint = Blueprint('tunings', '__name__')


@blueprint.route('/tuning_lines', methods=['GET', 'POST'])
def tuning_lines():    
    lines= read_data_in_base()

    form_select = SelectLineForm()
    form_tuning = TuningSelectLineForm()
    form_select.select_line.choices.append((-1, 'Добавить новую линию'))
    for index, line in enumerate(lines):
        form_select.select_line.choices.append(
            (index,
             line['name'])
        )
    if form_select.validate_on_submit():
        # print(form_select.select_line.choices)
        # print(form_select.select_line.data)
        sel_line_index = int(form_select.select_line.data)
        if sel_line_index >= 0 and sel_line_index < len(lines):
            init_form_tuning(lines[sel_line_index], form_tuning)

    if form_tuning.validate_on_submit():
        update_line_in_base(form_tuning)
        return redirect(url_for('tunings.tuning_lines'))
        

    form_select.select_line.data = -1    
    title = "Настройка счетчиков метража"
    
    return render_template('tunings/index.html',                           
                           page_title=title, 
                           form_select=form_select,
                           form_tuning=form_tuning,
                           lines=lines,
                           line=line
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


def init_form_tuning(line, form:TuningSelectLineForm):
    form.line_number.data = line['line_number']
    form.name.data = line['name']
    form.port.data = line['port']
    form.adr.data = line['adr']
    form.k.data = line['k']
    form.description.data = line['description']


def update_line_in_base(form:TuningSelectLineForm):
    line_number = form.line_number.data
    line = Lines.query.filter(Lines.line_number==line_number).first()
    if line:
        line.line_number = form.line_number.data 
        line.name = form.name.data 
        line.port = form.port.data 
        line.adr = form.adr.data
        line.k = form.k.data
        line.description = form.description.data
    else:
        line = Lines(name=form.name.data,
                  line_number = form.line_number.data,
                  port=form.port.data,
                  adr=form.adr.data,
                  k=form.k.data,
                  no_connection_counter=False,
                  indikator_value=0,
                  length=0.0,
                  speed_line=0.0,
                  description=form.description.data,
                  created_dt=datetime.now(),
                  updated_dt=datetime.now()
                  )        

    db.session.add(line)
    db.session.commit()
    