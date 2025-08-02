# test_multisigwallet.py
"""
Tests for MultiSigWallet module.
"""

import unittest
from multisigwallet import MultiSigWallet

class TestMultiSigWallet(unittest.TestCase):
    """Test cases for MultiSigWallet class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MultiSigWallet()
        self.assertIsInstance(instance, MultiSigWallet)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MultiSigWallet()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
