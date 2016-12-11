
Python wrapper for SMS APIs
===========================

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

### Documentation

Create an instance of SMS API to send SMS.

    from atemon.SMS import API

    sms_api = API(
        username=<Your User Name>,
        password=<Your Password>,
        sender_name=<Your Sender Name>,
        number=[List of numbers],
        message_type=[message type]
    )

    rep = sms_api.send(message=<Message string>)

* username     - Your username for SMS API
* password     - Your password for SMS API
* sender_name  - Your sender name on SMS API
* number       - If you wish to send message to same mobile number, you may set it here and need not pass mobile number to other funcetion calls. You can set a string as a number or pass a list of strings to send to multiple mobile numbers.
* message_type - The message type identifier by provider(transactional or promotional).

#### Example - Single number

    from atemon.SMS import API

    sms_api = API(
        username='demo',
        password='demo',
        sender_name='UPDATE',
        number='9999999999',
        message_type=0,
    )

    rep = sms_api.send(message="Hello world")

#### Example - Multiple number

    from atemon.SMS import API

    sms_api = API(
        username='demo',
        password='demo',
        sender_name='UPDATE',
        number=['9999999999', '1111111111'],
        message_type=0,
    )

    rep = sms_api.send(message="Hello world")
