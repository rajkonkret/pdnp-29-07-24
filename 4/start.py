# import fun10
import pakiet
from pakiet import fun  # importujemy konkretny plik z pakietu
import pakiet.fun as pk  # importuje plik jako alias

# pakiet.powitanie()  # AttributeError: module 'pakiet' has no attribute 'powitanie'
fun.powitanie()  # Cześć
pk.powitanie()  # Cześć
# po dodaniu w __init__ impportu tej metody jest ona widoczna z pakietu
pakiet.powitanie()

# nie ma metody info() w pakiet
# pakiet.info()
pk.info()
fun.info()
