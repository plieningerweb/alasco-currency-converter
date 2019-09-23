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
    if request.method == 'POST':
        if form.validate_on_submit():
            has_result = True
            
            try:
                CR = CurrencyRates()
                target_amount = CR.convert(form.base_currency.data,
                                           form.target_currency.data,
                                           form.base_amount.data)
                #raise Exception('test')
            
            except Exception as e:
                # TODO: test with testing framework
                #print('error')
                flash('currency conversion API failed', 'warning')    
        else:
            flash('form is not valid', 'warning')
                
            
    return render_template('convert.html', 
                           form=form,
                           has_result=has_result,
                           target_amount=target_amount)