from rtmsio.auth import sign


def test_sign():
    payload = {'yxz': 'foo', 'abc': 'baz', 'feg': 'bar'}
    secret = 'BANANAS'

    assert '82044aae4dd676094f23f1ec152159ba' == sign(payload, secret)
