from flask_wtf import FlaskForm
from wtforms import SelectField, DecimalField, SubmitField

class ConvertForm(FlaskForm):
    """convert from to convert amount from base to taret currency"""

    available_currencies = [('EUR', 'EUR Euro'),
                            ('USD', 'US Dollar'),
                            ('JPY', 'JPY Japanese Yen')]

    base_currency = SelectField('base_currency',
                                choices=available_currencies)
    base_amount = DecimalField('base_amount',
                               places=None)
    target_currency = SelectField('target_currency',
                                  choices=available_currencies)

    submit = SubmitField('Submit')
