import unittest

from cage_types import CageType
from map_provider import MapProvider


class TestMapGeneration(unittest.TestCase):
    def test_initialization(self):
        provider = MapProvider(width=10, height=12)
        self.assertEqual(provider.width, 10)
        self.assertEqual(provider.height, 12)

    def test_by_default_is_empty(self):
        provider = MapProvider(width=10, height=12)
        for row in provider.cages:
            for cage in row:
                self.assertEqual(cage, CageType.Empty)
