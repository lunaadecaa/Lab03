from dataclasses import dataclass
from operator import attrgetter

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti=[]

        return None
    def __str__(self):
        testo=f"{self.nome} - {self.responsabile}"
        for strumento in self.strumenti:
            testo+=f"\n {strumento}"
        return testo


    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        try:
            with open(file_path, "r",newline="",encoding="utf-8") as f:
                f.readline()
                for line in f:
                    parte=line.strip().split(",")
                    codice = parte[0]
                    strument = parte[1]
                    marca = parte[2]
                    anno_acquisto = int(parte[3])
                    valore = float(parte[4])

                    strumento = Strumento(codice, strument, marca, anno_acquisto, valore)
                    self.strumenti.append(strumento)

        except FileNotFoundError:
            print("file non trovato")

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        if self.strumenti == []:
            codice="S1"
        else:
            ultimo = self.strumenti[-1]
            i = int(ultimo[0][1:])
            codice = "S" + str(i + 1)
        self.strumenti.append([codice, tipo, marca, anno_acquisto, valore])
        strumento = [codice, tipo, marca, anno_acquisto, valore]

        return strumento

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        return sorted(self.strumenti, key=attrgetter('marca'))

    def nuovo_prestito(self, data, id_strumento, cognome_allievo,):
        """Crea un nuovo prestito"""
        # TODO
        trovato = False
        for s in self.strumenti:
            if s.codice == id_strumento:
                trovato = True
                break
        if not trovato:
            raise Exception("Strumento non presente nel deposito!")
        for p in self.prestiti:
            if p[2] == id_strumento:
                raise Exception("Strumento già in prestito!")
        codice = f"P{len(self.prestiti) + 1}"
        prestito = [codice, data, id_strumento, cognome_allievo]
        self.prestiti.append(prestito)

        return prestito

def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
        prestito_trovato = None
        for p in self.prestiti:
            if p[0] == id_prestito:
                prestito_trovato = p
                break
        if not prestito_trovato:
            raise Exception(f"Prestito '{id_prestito}' non trovato nel sistema!")
        self.prestiti.remove(prestito_trovato)


class Strumento:
    def __init__(self, codice, nome, marca, anno_acquisto, valore):
        self.codice = codice
        self.nome = nome
        self.marca = marca  # <-- Questo attributo rende possibile usare attrgetter("marca")
        self.anno_acquisto = anno_acquisto
        self.valore = valore

    def __str__(self):
        return f"[{self.codice}] {self.nome} - {self.marca} ({self.anno_acquisto}) - {self.valore}€"