from flask_wtf import FlaskForm
from wtforms import DateField, SubmitField, FloatField
from wtforms.validators import DataRequired, InputRequired


class SelectDateForm(FlaskForm):
    select_date = DateField('Выбор даты',
                            validators=[DataRequired()], format='%Y-%m-%d',
                            render_kw={"class": "datepicker"})
    update = SubmitField('Обновить', render_kw={"class": "btn btn-primary"})


class KoeficientsForm(FlaskForm):
    koef = FloatField('a', validators=[InputRequired()],
                        render_kw={"class": "form-control"})
    submit = SubmitField('Обновить',
                         render_kw={"class": "btn btn-primary"})
