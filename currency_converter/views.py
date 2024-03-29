from flask import Blueprint, render_template, request, flash

from forex_python.converter import CurrencyRates

from .forms import ConvertForm

currency_converter = Blueprint('currency_converter', __name__)

@currency_converter.route('/convert', methods=['GET', 'POST'])
def convert():
    """convert amount from base to target currency"""
    form = ConvertForm(request.form)
    has_result = False
    target_amount = False
    has_csrf_token = hasattr(form, 'csrf_token')
    if request.method == 'POST':
        if form.validate_on_submit():
            has_result = True

            try:
                CR = CurrencyRates()
                target_amount = CR.convert(form.base_currency.data,
                                           form.target_currency.data,
                                           form.base_amount.data)
            except Exception:
                # TODO: test with testing framework
                flash('currency conversion API failed', 'warning')
        else:
            flash('Form could not be validated. See below', 'warning')

    return render_template('convert.html',
                           form=form,
                           has_result=has_result,
                           target_amount=target_amount,
                           has_csrf_token=has_csrf_token)
