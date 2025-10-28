# test_usdcpayment.py
"""
Tests for USDCPayment module.
"""

import unittest
from usdcpayment import USDCPayment

class TestUSDCPayment(unittest.TestCase):
    """Test cases for USDCPayment class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = USDCPayment()
        self.assertIsInstance(instance, USDCPayment)
        
    def test_run_method(self):
        """Test the run method."""
        instance = USDCPayment()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
