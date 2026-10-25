# test_solidityprairie.py
"""
Tests for SolidityPrairie module.
"""

import unittest
from solidityprairie import SolidityPrairie

class TestSolidityPrairie(unittest.TestCase):
    """Test cases for SolidityPrairie class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = SolidityPrairie()
        self.assertIsInstance(instance, SolidityPrairie)

    def test_run_method(self):
        """Test the run method."""
        instance = SolidityPrairie()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
