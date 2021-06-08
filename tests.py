# ************************* #
#    Generator Labirytów    #
#      Albert Mouhoubi      #
#           Testy           #
# ************************* #

from main import MainApp

# Wygenerowanie labiryntu o wymiarach 10 na 12 pól
# z wejściem i wyjściem na przeciwnych krawędziach.
def test1():
    app = MainApp()
    app.ui.y.set(12)
    app.ui.prepare_btn.invoke()
    app.ui.start_end = ['9,6', '0,8']
    app.ui.generate_btn.invoke()
    app.start()

# Wygenerowanie labiryntu o wymiarach 20 na 10 pól
# z wejściem i wyjściem cztery pola od przeciwnych, krótszych krawędzi.
def test2():
    app = MainApp()
    app.ui.x.set(20)
    app.ui.prepare_btn.invoke()
    app.ui.start_end = ['3,0', '3,9']
    app.ui.generate_btn.invoke()
    app.start()

# Próba wygenerowania labiryntu o wymiarach 10 na 10
# z wejściem i wyjściem w jednym polu - oczekiwana informacja o błędzie.
# WYJĄTEK RZUCANY W KONSOLI
def test3():
    app = MainApp()
    app.ui.start_end = ['0,6', '0,6']
    app.ui.generate_btn.invoke()
    app.start()

# Próba wygenerowania labiryntu o wymiarach 10 na 10
# z wejściem i wyjściem kolo siebie
# oczekiwana informacja o błędzie, ścieżka jest linią prostą.
# U MNIE TAKI PROBLEM NIE WYSTĘPUJE
def test4():
    app = MainApp()
    app.ui.start_end = ['0,6', '0,5']
    app.ui.generate_btn.invoke()
    app.start()

# Próba wygenerowania labiryntu o wymiarach 10 na 10
# z wejściem i wyjściem między którymi jest 1, 2 lub 3 pola odstępu
# oczekiwany labirynt bez ścieżki będącej linią prostą.
def test5():
    app = MainApp()
    app.ui.start_end = ['0,6', '0,2']
    app.ui.generate_btn.invoke()
    app.start()

# Próba wygenerowania labiryntu którego przynajmniej jeden z wymiarów
# wynosi O lub jest liczbą ujemną - oczekiwana informacja o błędzie.
# PROGRAM SAM SIĘ NAPRAWIA I GENERUJE POPRAWNY JEŚLI MOŻE
def test6():
    app = MainApp()
    app.ui.x.set(-1)
    app.ui.start_end = ['0,6', '0,2']
    app.ui.generate_btn.invoke()
    app.start()

# Próba wygenerowania za dużego labiryntu - oczekiwana informacja o błędzie.
# TUTAJ PROGRAM SIE NIE NAPRAWI BO UI DZIAŁA ALE GENERATOR JUŻ TEGO SAM NIE ZMIENI
def test7():
    app = MainApp()
    app.ui.x.set(26)
    app.ui.prepare_btn.invoke()
    app.ui.start_end = ['0,6', '0,2']
    app.ui.generate_btn.invoke()
    app.start()

test7()
