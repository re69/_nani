import unittest

from cage_types import CageType
from map_provider import MapProvider
from tests import fixtures


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

    def test_generate_map_by_str(self):
        stringed_map = fixtures.simple_map
        provider = MapProvider.generate_by(stringed_map)

        self.assertEqual(provider.width, 7)
        self.assertEqual(provider.height, 5)

        self.assertTrue(CageType.Empty not in provider.cages[0])

        self.assertEqual(provider.cages[1][0], CageType.Empty)
        self.assertEqual(provider.cages[4][5], CageType.Empty)

        self.assertEqual(provider.cages[0][0], CageType.Wall)
        self.assertEqual(provider.cages[0][6], CageType.Wall)
        self.assertEqual(provider.cages[4][6], CageType.Wall)
        self.assertEqual(provider.cages[4][0], CageType.Wall)

        stringed_map = fixtures.snake_path
        provider = MapProvider.generate_by(stringed_map)
        self.assertEqual(provider.width, 7)
        self.assertEqual(provider.height, 9)

        self.assertEqual(provider.cages[0][1], CageType.Empty)
        self.assertEqual(provider.cages[8][2], CageType.Empty)

        self.assertEqual(provider.cages[0][0], CageType.Wall)
        self.assertEqual(provider.cages[0][6], CageType.Wall)
        self.assertEqual(provider.cages[8][6], CageType.Wall)
        self.assertEqual(provider.cages[8][0], CageType.Wall)
