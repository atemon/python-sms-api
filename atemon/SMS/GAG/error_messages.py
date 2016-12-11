"""
Error codes for GAG Gateway.

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

messages = {
    "000": "DELIVRD Delivered to SIM.",
    "001": "UNDELIV Unidentified subscriber.",
    "003": "Memory Capacity Exceeded",
    "004": "Mobile Equipment Error",
    "005": "EXPIRED Unidentified subscriber/Network Error",
    "006": "Barring",
    "007": "Invalid Sender ID",
    "008": "Dropped",
    "009": "NDNC Failed",
    "010": "UNDELIV Illegal subscriber",
    "011": "UNDELIV Tele service not provisioned",
    "012": "UNDELIV Illegal Equipment",
    "013": "UNDELIV Call Barred",
    "021": "UNDELIV Facility not supported",
    "027": "EXPIRED Absent subscriber",
    "031": "EXPIRED Subscriber busy for MT_SMS",
    "032": "EXPIRED SM-Delivery Failure",
    "034": "EXPIRED System failure",
    "035": "UNDELIV Data missing",
    "036": "UNDELIV Unexpected Data value",
    "100": "Misc. Error",
    "144": "UNDELIV Unrecognized component",
    "145": "UNDELIV Mistyped Component",
    "146": "UNDELIV Body structured component",
    "160": "EXPIRED Duplicate invoke ID",
    "161": "UNDELIV Unrecognized Operation",
    "162": "UNDELIV Mistyped Parameter",
    "163": "EXPIRED Resource Limitation",
    "164": "EXPIRED Initiating release",
    "165": "EXPIRED Unrecognized linked ID",
    "166": "EXPIRED Linked Response expected",
    "167": "EXPIRED Unexpected linked operation",
    "176": "UNDELIV Unrecognized invoke ID",
    "177": "EXPIRED Return result expected",
    "178": "UNDELIV Mistyped Parameter",
    "192": "EXPIRED Unrecognized invoke ID",
    "193": "EXPIRED Return Error unexpected",
    "194": "UNDELIV Unrecognized error",
    "195": "UNDELIV Unexpected Error",
    "196": "UNDELIV Mistyped parameter",
    "200": "UNDELIV Unable to decode respons",
    "201": "EXPIRED Provider Abort",
    "202": "UNDELIV User Abort",
    "203": "EXPIRED Timeout",
    "204": "UNDELIV API error",
    "205": "UNDELIV Unknown Error",
    "408": "REJECTED DND error code",
    "409": "REJECTED Source/template error code",
    "410": "REJECTED Source/Template long message error code",
    "411": "REJECTED Duplicate Submission",
    "1032": "DND Do not disturb",
    "1078": "DND Do not disturb",
}
