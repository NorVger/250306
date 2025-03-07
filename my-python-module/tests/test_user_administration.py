import unittest
from my_module.user_administration import *  # Adjust imports based on actual functions/classes

class TestUserAdministration(unittest.TestCase):

    def test_os_name(self):
        self.assertIn(os.name, ['posix', 'nt'])

    def test_cpu_count(self):
        self.assertGreaterEqual(os.cpu_count(), 1)

    def test_available_ram(self):
        available_ram = psutil.virtual_memory().total / (1024**3)
        self.assertGreater(available_ram, 0)

if __name__ == '__main__':
    unittest.main()