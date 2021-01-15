import datetime
import unittest

from code_helper import ShellyInfo

# ShellyInfo object
from code_helper import checkTotp
from code_helper import retrieveDevicesInfo

fakeShelly = ShellyInfo(
    name="FakeShellyForTest",
    ip="999.999.999.999",
    relay="0",
    user="TestIsBoring",
    password="TestIsNecessary"
)


class TestHelper(unittest.TestCase):
    def test_retrieveDevicesInfo_empy_db(self):
        # Create object to test
        listToTest = retrieveDevicesInfo(path=".\\testsDB\\db_1")

        # Assert
        self.assertEqual(listToTest, [])

    def test_retrieveDevicesInfo_db_with_one_entry(self):
        # Create object to test
        listToTest = retrieveDevicesInfo(path=".\\testsDB\\db_2")

        # Assert
        self.assertEqual(listToTest, [fakeShelly])

    def test_retrieveDevicesInfo_db_with_two_entries(self):
        # Create object to test
        listToTest = retrieveDevicesInfo(path=".\\testsDB\\db_3")

        # Assert
        self.assertEqual(listToTest, [fakeShelly, fakeShelly])

    def test_checkTotp_wrong_code(self):
        # Create object to test
        key = "DYOOI6XW2PMNSBCZ"
        value = "00000asfdf"
        timeNow = datetime.datetime.strptime("10 january 2000", "%d %B %Y")

        result = checkTotp(value=value, key=key, timeNow=timeNow)

        # Assert
        self.assertEqual(result, False)

    def test_checkTotp_correct_code_previous_time(self):
        # Create object to test
        key = "DYOOI6XW2PMNSBCZ"
        value = "883026"
        timePrevious = datetime.datetime.utcfromtimestamp(1610708198.601391)
        timeNow = datetime.datetime.utcfromtimestamp(1610738198.601391)

        result = checkTotp(value=value, key=key, timeNow=timeNow, delta=timeNow-timePrevious)

        # Assert
        self.assertEqual(result, True)

    def test_checkTotp_correct_code_current_time(self):
        # Create object to test
        key = "DYOOI6XW2PMNSBCZ"
        value = "660865"
        timeNow = datetime.datetime.utcfromtimestamp(1610738198.601391)

        result = checkTotp(value=value, key=key, timeNow=timeNow, delta=timeNow-timeNow)

        # Assert
        self.assertEqual(result, True)

    def test_checkTotp_correct_code_next_time(self):
        # Create object to test
        key = "DYOOI6XW2PMNSBCZ"
        value = "201501"
        timeNow = datetime.datetime.utcfromtimestamp(1610738198.601391)
        timeNext = datetime.datetime.utcfromtimestamp(1610768198.601391)

        result = checkTotp(value=value, key=key, timeNow=timeNow, delta=timeNext-timeNow)

        # Assert
        self.assertEqual(result, True)
