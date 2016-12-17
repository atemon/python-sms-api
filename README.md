
Python wrapper for SMS APIs
===========================

&copy; 2016 ATEMON Technology Consultants LLP<br>
License: MIT License (modified)<br>
Website: <a href="http://www.atemon.com">http://www.atemon.com</a><br>
Author: Varghese Chacko <varghese@atemon.com>

#### Install

    pip install Atemon-SMSAPI


#### Usage

    from atemon.SMS import API

    sms_api = API(
        username=<Your User Name>,
        password=<Your Password>,
        sender_name=<Your Sender Name>,
    )

    rep = sms_api.send(message=<Message string>, number=<Receiver's mobile number>)

### Send Message

Create an instance of SMS API to send SMS.

    from atemon.SMS import API

    sms_api = API(
        username=<Your User Name>,
        password=<Your Password>,
        sender_name=<Your Sender Name>,
        number=[List of numbers],
        message_type=[message type],
        http_api=[http API URL],
    )

<ul>
    <li>username     - Your username for SMS API</li>
    <li>password     - Your password for SMS API</li>
    <li>sender_name  - Your sender name on SMS API</li>
    <li>number       - If you wish to send message to same mobile number, you may set it here and need not pass mobile number to other funcetion calls. You can set a string as a number or pass a list of strings to send to multiple mobile numbers.</li>
    <li>message_type - The message type identifier by provider(transactional or promotional).
        <ul>For GreenAds Global
            <li>0 - Promotional</li>
            <li>1 - Transactional</li>
            <li>2 - Promotional with sender id.</li>
        </ul>
    </li>
    <li>http_api - URL to HTTP API. Default value is http://sapteleservices.com/SMS_API/.</li>
</ul>

```sh

    rep = sms_api.send(message=<Message string>)
```

<ul>
    <li>message - The message to be sent.</li>
</ul>

#### Example 1- Send to single number

    from atemon.SMS import API

    sms_api = API(
        username='demo',
        password='demo',
        sender_name='UPDATE',
        number='9999999999',
        message_type=0,
    )

    rep = sms_api.send(message="Hello world")

#### Example 2- Send to multiple numbers

    from atemon.SMS import API

    sms_api = API(
        username='demo',
        password='demo',
        sender_name='UPDATE',
        number=['9999999999', '1111111111'],
        message_type=0,
    )

    rep = sms_api.send(message="Hello world")

#### Example 3- Send to single number

    from atemon.SMS import API

    sms_api = API(
        username='demo',
        password='demo',
        sender_name='UPDATE',
        message_type=0,
    )

    rep = sms_api.send(
        message="Hello world",
        number='9999999999',
    )

#### Example 4- Send to multiple numbers

    from atemon.SMS import API

    sms_api = API(
        username='demo',
        password='demo',
        sender_name='UPDATE',
        message_type=0,
    )

    rep = sms_api.send(
        message="Hello world",
        number=['9999999999', '1111111111'],
    )

Note: If mobile number(s) is passed to ```send()```, the message is end ONLY to the number passed. The number(s) set via constructor will be ignored for that call. It will NOT replace the number(s) set via constructor

### Schedule SMS to be send later

    sms_api.schedule_sms(
        message=<Message String>,
        number=[mobile numbers],
        scheduled_time=<Time to send SMS>,
        message_type=[message type]
    )
<ul>
    <li>Message         - Your username for SMS API</li>
    <li>number          - Mobile number to which the message to be delivered.  Single number cpuld be set as a string or pass a list of strings to send to multiple mobile numbers.</li>
    <li>scheduled_time  - Time at which message to be sent - Python's datetime.datetime object.</li>
    <li>message_type - The message type identifier by provider(transactional or promotional).</li>
</ul>

#### Example 1- Schedule to send to single number after 30 minutes

    from datetime import datetime, timedelta
    from atemon.SMS import API

    sms_api = API(
        username='demo',
        password='demo',
        sender_name='UPDATE',
        number='9999999999',
        message_type=0,
    )

    rep = sms_api.schedule_sms(
        message="Hello world",
        scheduled_time=datetime.now() + timedelta(minutes=30)
    )

#### Example 2- Schedule to send to multiple numbers after 30 minutes

    from atemon.SMS import API

    sms_api = API(
        username='demo',
        password='demo',
        sender_name='UPDATE',
        number=['9999999999', '1111111111'],
        message_type=0,
    )

    rep = sms_api.schedule_sms(
        message="Hello world",
        scheduled_time=datetime.now() + timedelta(minutes=30)
    )

#### Example 3- Schedule to send to single number after 30 minutes

    from atemon.SMS import API

    sms_api = API(
        username='demo',
        password='demo',
        sender_name='UPDATE',
        message_type=0,
    )

    rep = sms_api.schedule_sms(
        message="Hello world",
        number='9999999999',
        scheduled_time=datetime.now() + timedelta(minutes=30)
    )

#### Example 4- Schedule to send to multiple numbers after 30 minutes

    from atemon.SMS import API

    sms_api = API(
        username='demo',
        password='demo',
        sender_name='UPDATE',
        message_type=0,
    )

    rep = sms_api.schedule_sms(
        message="Hello world",
        number=['9999999999', '1111111111'],
        scheduled_time=datetime.now() + timedelta(minutes=30)
    )


#### Example 5- Schedule to send to multiple numbers on 1st Jan 2018 (midnight)

    from atemon.SMS import API

    sms_api = API(
        username='demo',
        password='demo',
        sender_name='UPDATE',
        message_type=0,
    )

    rep = sms_api.schedule_sms(
        message="Hello world",
        number=['9999999999', '1111111111'],
        scheduled_time=datetime(2018, 1, 1)
    )

Note: If mobile number(s) is passed to ```send()```, the message is end ONLY to the number passed. The number(s) set via constructor will be ignored for that call. It will NOT replace the number(s) set via constructor
Note: scheduled_time need to be a valid datetime.datetime object. It's the developers freedom, how to set date. For dates in past, or in far future, its the API decides to accept or not or deny.

### Get balance information

    info = sms_api.get_balance_info()

#### Example

    from atemon.SMS import API

    sms_api = API(
        username='demo',
        password='demo'
    )
    info = sms_api.get_balance_info()

Note: Passed only necessary info to API. You may call ```get_balance_info()``` on any sms_api Object.


### Get delivery report between dates

    info = sms_api.get_delivery_report(
        from_date=<Start date>,
        to_date=<End date>,
    )

<ul>
    <li>from_date - Start date - Python's datetime.datetime object.</li>
    <li>to_date   - End date - Python's datetime.datetime object.</li>
</ul>

#### Example

    from atemon.SMS import API

    sms_api = API(
        username='demo',
        password='demo'
    )
    info = sms_api.get_delivery_report(
        from_date=datetime.datetime(2016, 12, 1),
        to_date=datetime.datetime(2016, 12, 31),
    )

Note: Passed only necessary info to API. You may call ```get_delivery_report()``` on any sms_api Object.

### Get delivery report between dates for a given number

    info = sms_api.get_delivery_report(
        from_date=<Start date>,
        to_date=<End date>,
        number=<Mobile number>
    )

<ul>
    <li>from_date - Start date - Python's datetime.datetime object.</li>
    <li>to_date   - End date - Python's datetime.datetime object.</li>
    <li>number    - Number for which the report is taken.</li>
</ul>

#### Example

    from atemon.SMS import API

    sms_api = API(
        username='demo',
        password='demo'
    )
    info = sms_api.get_delivery_report(
        nu
        from_date=datetime.datetime(2016, 12, 1),
        to_date=datetime.datetime(2016, 12, 31),
    )

Note: Passed only necessary info to API. You may call ```get_delivery_report()``` on any sms_api Object.


## Contributors.

You are requested to report bugs and/or contribute to the package. We will try our best to keep track of any pull requests or bug reports. A mail with package name in subject line, sent to ```varghese@atemon.com```, will get quicker attention :)
