from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, InputRequired


class SelectLineForm(FlaskForm):
    select_line = SelectField('Выбор линии для настройки', choices=[])


class TuningSelectLineForm(FlaskForm):
    line_number = IntegerField('line_number', validators=[InputRequired()],
                               render_kw={"class": "form-control"})
    name = StringField('name', validators=[DataRequired()],
                           render_kw={"class": "form-control"})
    port = IntegerField('port', validators=[InputRequired()],
                               render_kw={"class": "form-control"})
    adr = IntegerField('adr', validators=[InputRequired()],
                               render_kw={"class": "form-control"})
    k = FloatField('k', validators=[InputRequired()],
                        render_kw={"class": "form-control"})
    description = StringField('description', validators=[DataRequired()],
                           render_kw={"class": "form-control"})
    save = SubmitField('Сохранить',
                         render_kw={"class": "btn btn-primary"})

