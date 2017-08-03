from wtforms import Form, FloatField, validators
from math import pi

class InputForm(Form):
	A = FloatField(
		label='shotnum', default=1.0,
		validators=[validators.InputRequired()])
	B = FloatField(
		label='node name', default=0,
		validators=[validators.InputRequired()])
	C = FloatField(
		label='frequency (1/s)', default=2*pi,
		validators=[validators.InputRequired()])
	D = FloatField(
		label='time interval (s)', default=18,
		validators=[validators.InputRequired()])
	