from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    cpu = StringField('CPU', validators=[DataRequired()])
    memoria = StringField('Memoria', validators=[DataRequired()])
    ip = StringField('Ip', validators=[DataRequired()])
    so = RadioField('Sistema Operacional',choices=[('0','Windowns 7 Starter'),('1','Ubuntu')])
    
    submit = SubmitField('Criar')