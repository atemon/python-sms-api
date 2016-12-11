"""

SMS API GAG.

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
import requests
from datetime import datetime


class API(object):
    """SMS API for GAG."""

    http_api = "http://sapteleservices.com/SMS_API/"
    send_script = 'sendsms.php'
    schedule_script = 'schedule.php'
    balanceinfo_script = 'balanceinfo.php'
    getreports_script = 'getreports.php'

    def __init__(self, username, password, sender_name, number=None, message_type=0, http_api=None):
        """Initialize SMS module for GreenAds Global API."""
        self.username = username
        self.password = password
        self.number = number
        self.sender_name = sender_name
        self.mobile_number = self.__convert_number(number)
        self.message_type = message_type
        if http_api:
            self.http_api = http_api

        self.__set_api()

    def set_api(self, http_api=None, send_script=None, schedule_script=None, balanceinfo_script=None, getreports_script=None):
        """Set API in case you use different one than latest."""
        if http_api:
            self.http_api = http_api

        if send_script:
            self.send_script = send_script

        if schedule_script:
            self.schedule_script = schedule_script

        if balanceinfo_script:
            self.balanceinfo_script = balanceinfo_script

        if getreports_script:
            self.getreports_script = getreports_script

        self.__set_api()

    def __set_api(self):
        """Configure API scripts."""
        self.send_api = "%s%s" % (self.http_api, self.send_script,)
        self.schedule_api = "%s%s" % (self.http_api, self.schedule_script)
        self.balanceinfo_api = "%s%s" % (self.http_api, self.balanceinfo_script)
        self.getreports_api = "%s%s" % (self.http_api, self.getreports_script)

    def __convert_number(self, number=None):
        """Convert number/array of numbers to."""
        if type(number) is list:
            return ",".join([str(n).replace(' ', '') for n in number])
        elif number is None:
            return self.number
        else:
            return str(number).replace(' ', '')

    def __query_api(self, api, payload={}):

        if payload is not None:
            payload.update({
                'username': self.username,
                'password': self.password,
            })
        if api == self.send_api or api == self.schedule_api:
            payload.update({
                'sendername': self.sender_name,
            })
        r = requests.get(api, params=payload)
        # assert False, "%s%s" % (r.status_code, r.content)

        if r.status_code == 200:
            return r.content
        else:
            r.raise_for_status()

    def send(self, message=None, number=None, message_type=None):
        """Send SMS."""
        assert message is not None, "Provide a valid message"

        mobile_number = self.__convert_number(number)
        assert mobile_number is not None, "Provide a valid number"

        message_type = message_type if message_type is not None else self.message_type

        payload = {
            'mobile': mobile_number,
            'message': message,
            'routetype': message_type,
        }
        return self.__query_api(self.send_api, payload)

    def set_number(self, number):
        """Set number."""
        self.number = number
        self.mobile_number = self.__convert_number(number)

    def schedule_sms(self, message, number=None, scheduled_time=None, message_type=2):
        """Schedule an SMS."""
        assert message is not None, "Provide a valid message"
        assert type(scheduled_time) is datetime, "Provide valid date time"
        mobile_number = self.__convert_number(number)
        assert mobile_number is not None, "Provide a valid number"

        message_type = message_type if message_type is not None else self.message_type

        payload = {
            'mobile': mobile_number,
            'message': message,
            'routetype': message_type,
            'datetime': str(scheduled_time),
        }
        return self.__query_api(self.schedule_api, payload)

    def get_balance_info(self):
        """Get balance info."""
        return self.__query_api(self.balanceinfo_api)

    def get_delivery_report(self, from_date=None, to_date=None, number=None):
        """Get delivery reports."""
        assert type(from_date) is datetime, "Provide valid date time"
        assert type(to_date) is datetime, "Provide valid date time"

        payload = {
            'fromDate': str(from_date),
            'toDate': str(to_date),
        }

        if number is None:
            return self.__query_api(self.getreports_api, payload)
        else:
            url = "http://sapteleservices.in/getdelivery/%s/%s/%s" % (self.username, self.password, number)
            return self.__query_api(url, None)
