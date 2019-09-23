# -*- coding: utf-8 -*-

class TestConvert:
    """test currency conversion"""

    def convert(self, client, base_currency,
                target_currency, base_amount):
        return client.post('/convert', data=dict(
            base_amount=base_amount,
            base_currency=base_currency,
            target_currency=target_currency,
            csrf_token='',
        ), follow_redirects=True)

    def test_check_csrf(self, client):
        """test that csrf fails"""
        rv = self.convert(client, 'EUR', 'USD', '1.0')

        # todo: better way to check if csrf failed
        assert b'Converted Currency' not in rv.data

    def test_convert_eur_usd(self, client_csrf_disabled):
        """test for successful conversion"""
        rv = self.convert(client_csrf_disabled, 'EUR', 'USD', '1.0')

        # todo: mock api to completely test if result rendered
        assert b'1.0 EUR = ' in rv.data
