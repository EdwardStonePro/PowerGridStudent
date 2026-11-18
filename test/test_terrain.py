
import unittest
import xmlrunner

from pathlib import Path

from Terrain import Terrain, Case

class TestTerrain(unittest.TestCase):

    def test_chargement(self):
        # TODO
        self.fail()

    def test_get_entree(self):
        t = Terrain()
        chemin_terrain = Path(__file__).parent / "terrains" / "t3.txt"
        
        t.charger(str(chemin_terrain))
        entree = t.get_entree()
        self.assertIsNotNone(entree)
        self.assertEqual(entree[1], 0)
        self.assertEqual(entree[0], 2)

    def test_accesseur(self):
        t = Terrain()
        t.cases = [
                [Case.ENTREE, Case.VIDE, Case.VIDE],
                [Case.CLIENT, Case.CLIENT, Case.CLIENT],
        ]
        self.assertEqual(t[0][0], Case.ENTREE)
        self.assertEqual(t[0][1], Case.VIDE)
        self.assertEqual(t[1][2], Case.CLIENT)

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))

