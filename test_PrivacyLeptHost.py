from unittest import TestCase
from PrivacyLeptHost import PrivacyLeptHost


class TestPrivacyLeptHost(TestCase):
    def test_notify(self):
        PrivacyLeptHost.notify()
