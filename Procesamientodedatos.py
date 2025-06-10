class AgenteReactivo: 
    def __init__(self):
        pass
    def percepcion (self, text):
        return [ord (char) for char in text]
    
agente = AgenteReactivo()
percivir = input (" ")
valoresdeASCII = agente.percepcion(percivir)
CadenaASCII = " ".join(map(str, valoresdeASCII))
print ( CadenaASCII)

