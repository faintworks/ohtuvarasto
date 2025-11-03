### import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_lisays_yli_tilavuuden(self):
        self.varasto.lisaa_varastoon(15)  # Try to add more than capacity
        self.assertAlmostEqual(self.varasto.saldo, 10)  # Should be full

    def test_lisays_negatiivinen(self):
        self.varasto.lisaa_varastoon(-5)  # Try to add negative
        self.assertAlmostEqual(self.varasto.saldo, 0)  # Should not change saldo

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ottaminen_yli_saldon(self):
        self.varasto.lisaa_varastoon(5)  # Fill the varasto with 5
        saatu_maara = self.varasto.ota_varastosta(10)  # Try to take more than available (10)
        self.assertAlmostEqual(saatu_maara, 5)  # Should return the entire saldo
        self.assertAlmostEqual(self.varasto.saldo, 0)  # Should be empty now

    def test_ottaminen_negatiivinen(self):
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(-3)  # Try to take negative
        self.assertAlmostEqual(saatu_maara, 0)  # Should return 0

    def test_varasto_konstruktori_negatiivinen_tilavuus(self):
        varasto = Varasto(-10)  # Should set tilavuus to 0
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_varasto_konstruktori_negatiivinen_saldo(self):
        varasto = Varasto(10, -5)  # Should set saldo to 0
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_varasto_konstruktori_saldo_yli_tilavuuden(self):
        varasto = Varasto(10, 15)  # Should set saldo to tilavuus (10)
        self.assertAlmostEqual(varasto.saldo, 10)

    def test_ottaminen_kaikki_varastosta(self):
        self.varasto.lisaa_varastoon(5)  # Fill the varasto with 5
        self.varasto.ota_varastosta(5)    # Take all of it
        saatu_maara = self.varasto.ota_varastosta(10)  # Try to take more than available (10)
        self.assertAlmostEqual(saatu_maara, 0)  # Should return 0 since saldo is 0
        self.assertAlmostEqual(self.varasto.saldo, 0)  # Should still be empty

    def test_str_muoto(self):
        self.varasto.lisaa_varastoon(3)
        self.assertEqual(str(self.varasto), "saldo = 3, vielä tilaa 7")

if __name__ == "__main__":
    unittest.main()