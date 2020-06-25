class RPSError(Exception):
    def __init__(self, code = 000):
        self.errorMessage = "~" * 50 + "\n"

        self.errorDict = {
            000 : "Error 000 : Nespecificirana greška",
            101 : "Error 101 : Greška prilikom pogrešnog unosa"
        }

        try:
            self.errorMessage += self.errorDict[code]
        except KeyError:
            self.errorMessage += self.errorDict[000]