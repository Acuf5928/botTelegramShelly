import unittest

from code_change_shelly_status import createLink
from code_helper import ShellyInfo

# ShellyInfo object
fakeShelly = ShellyInfo(
    name="FakeShellyForTest",
    ip="999.999.999.999",
    relay="0",
    user="TestIsBoring",
    password="TestIsNecessary"
)


class TestChangeShellyStatus(unittest.TestCase):
    def test_create_link_command_on(self):
        # Create object to test
        link = createLink(fakeShelly, "on")

        # Assert
        self.assertEqual(link, "http://TestIsBoring:TestIsNecessary@999.999.999.999/relay/0?turn=on")

    def test_create_link_command_off(self):
        # Create object to test
        link = createLink(fakeShelly, "off")

        # Assert
        self.assertEqual(link, "http://TestIsBoring:TestIsNecessary@999.999.999.999/relay/0?turn=off")

    def test_create_link_command_update(self):
        # Create object to test
        link = createLink(fakeShelly, "update")

        # Assert
        self.assertEqual(link, "http://TestIsBoring:TestIsNecessary@999.999.999.999/relay/0")


