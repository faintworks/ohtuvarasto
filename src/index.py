from varasto import Varasto

def tulosta_varastot(mehua, olutta):
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

def testaa_olutgetterit(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

def testaa_mehusetterit(mehua):
    print("Mehu setterit:")
    mehua.lisaa_varastoon(50.7)
    tulosta_varastot(mehua, None)
    mehua.ota_varastosta(3.14)
    tulosta_varastot(mehua, None)

def testaa_varasto_negative_capacity():
    print("Varasto(-100.0);")
    try:
        Varasto(-100.0)
    except ValueError as e:
        print(f"Virhe: {e}")

def testaa_varasto_negative_initial_amount():
    print("Varasto(100.0, -50.7)")
    try:
        Varasto(100.0, -50.7)
    except ValueError as e:
        print(f"Virhe: {e}")

def testaa_ota_varastosta(olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

def testaa_lisaa_varastoon(olutta, mehua):
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

def testaa_varastot(mehua, olutta):
    testaa_lisaa_varastoon(olutta, mehua)
    testaa_ota_varastosta(olutta)

    print(f"Mehuvarasto: {mehua}")
    print("mehua.ota_varastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")

def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    tulosta_varastot(mehua, olutta)

    testaa_olutgetterit(olutta)
    testaa_mehusetterit(mehua)
    testaa_varasto_negative_capacity()
    testaa_varasto_negative_initial_amount()
    testaa_varastot(mehua, olutta)

if __name__ == "__main__":
    main()
