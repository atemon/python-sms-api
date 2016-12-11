"""Test Suit for SMS API."""
from atemon.SMS import API
from datetime import datetime, timedelta

sms_api = API(
    username='demo',
    password='demmo',
    sender_name='UPDATE',
    number='9999999999'
)

def test_send_sms():
    """Test send."""
    rep = sms_api.send(message="Test One")
    assert 'Remark:Sent Successfully' in rep, "%s" % (rep)

def test_send_multiple_sms():
    """Test send multiple."""
    rep = sms_api.send(message="Test One", number=['9999999999', '1111111111'])
    assert 'Message(s) Sent' in rep, "%s" % (rep)

def test_schedule_sms():
    """Test schedule SMS."""
    rep = sms_api.schedule_sms(message="Test One", scheduled_time=datetime.now() + timedelta(minutes=1))
    assert ' Successfully Scheduled' in rep, "%s" % (rep)

def test_balance_report():
    """Test balance report."""
    rep = sms_api.get_balance_info()
    assert 'T-' in rep and 'P-' in rep, "No balance info available. %s" % (rep)

def test_get_delivery_report():
    """Test delivery report."""
    rep = sms_api.get_delivery_report(datetime.today() - timedelta(days=1), datetime.today() + timedelta(days=1))
    assert rep, "No delivery report available. %s" % (rep)
