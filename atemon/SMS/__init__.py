"""
Package to send SMS using different providers.

Website: http://www.atemon.com
Git Hub: https://github.com/atemon
Twitter: https://twitter.com/atemonastery

Author: Varghese Chacko varghese@atemon.com

Copyright 2016 Atemon Technology Consultants LLP

This file is part of SMS library and distributed under the MIT license (MIT).

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be included in all copies
or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE X CONSORTIUM BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Except as contained in this notice, the name of the Atemon Technology Consultants LLP shall
not be used in advertising or otherwise to promote the sale, use or other dealings in this
Software without prior written authorization from the Atemon Technology Consultants LLP.
"""
# -*- coding: utf-8 -*-

import importlib


class API(object):
    """SMS API for various providers."""

    provider_code = "GAG"

    def __init__(self, username, password, sender_name, provider=None, number=None, message_type=0):
        """Initialize SMS module for given providers."""
        if provider:
            self.provider_code = provider

        self.username = username
        self.password = password
        self.number = number
        self.message_type = message_type
        self.sender_name = sender_name

        sms_module = importlib.import_module("atemon.SMS." + self.provider_code)
        self.provider = sms_module.API(
            username=username,
            password=password,
            number=number,
            sender_name=sender_name,
        )

    def send(self, message, number=None, message_type=0):
        """Send SMS."""
        return self.provider.send(
            message=message,
            number=number,
            message_type=message_type
        )

    def set_api(self, http_api=None, send_script=None, schedule_script=None, balanceinfo_script=None, getreports_script=None):
        """Set API URL and script."""
        return self.set_api(http_api=None, send_script=None, schedule_script=None, balanceinfo_script=None, getreports_script=None)

    def set_number(self, number):
        """Set number."""
        return self.provider.set_number(number=number)

    def change_provider(self, provider):
        """Change service provider."""
        try:
            sms_module = importlib.import_module("SMS." + provider)
            self.provider = sms_module.API(
                username=self.username,
                password=self.password,
                number=self.number,
                message_type=self.message_type,
                sender_name=self.sender_name,
            )
        except:
            raise

    def schedule_sms(self, message, number=None, scheduled_time=None, message_type=0):
        """Schedule an SMS."""
        return self.provider.schedule_sms(
            message=message,
            number=number,
            scheduled_time=scheduled_time,
            message_type=message_type
        )

    def get_balance_info(self):
        """Get balance info."""
        return self.provider.get_balance_info()

    def get_delivery_report(self, from_date=None, to_date=None, number=None):
        """Get delivery reports."""
        return self.provider.get_delivery_report(
            from_date=from_date,
            to_date=to_date,
            number=number,
        )
