import numpy
import sounddevice as sd
import time


class CharlieWhisky:

    def __init__(self, volume=0.5, samplerate=22050, dit_duration_ms=180, frequency=1660.0, debug=False):
        self.volume = volume
        self.samplerate = samplerate
        self.frequency = frequency
        self.dit_duration = dit_duration_ms / 1000
        self.words_per_minute = 1200 / dit_duration_ms
        self.debug = debug

        self.letter_dictionary = {"A": "01", "B": "1000", "C": "1010",
                                  "D": "100", "E": "0", "F": "0010",
                                  "G": "110", "H": "0000", "I": "00",
                                  "J": "0111", "K": "101", "L": "0100",
                                  "M": "11", "N": "10", "O": "111",
                                  "P": "0110", "Q": "1101", "R": "010",
                                  "S": "000", "T": "1", "U": "001",
                                  "V": "0001", "W": "011", "X": "1001",
                                  "Z": "1100", ".": "010101", ",": "110011",
                                  "?": "001100", "/": "10010", "@": "011010",
                                  "1": "01111", "2": "00111",
                                  "3": "00011", "4": "00001",
                                  "5": "00000", "6": "10000",
                                  "7": "11000", "8": "11100",
                                  "9": "11110", "0": "11111"
                                  }


    def dit(self):
        duration = numpy.arange(int(numpy.ceil(self.dit_duration * self.samplerate))) / self.samplerate
        dit = self.volume * numpy.sin(numpy.pi*self.frequency*duration)
        sd.play(dit, self.samplerate, blocking=True)

    def dah(self):
        duration = numpy.arange(int(numpy.ceil(self.dit_duration * 3 * self.samplerate))) / self.samplerate
        #dah = self.volume * numpy.sin(numpy.pi*(self.frequency-10)*duration)
        dah = self.volume * numpy.sin(numpy.pi*(self.frequency)*duration)
        sd.play(dah, self.samplerate, blocking=True)

    def space_letter(self):
        duration = numpy.arange(int(numpy.ceil(self.dit_duration * 3 * self.samplerate))) / self.samplerate
        space = self.volume * numpy.sin(numpy.pi*1*duration)
        sd.play(space, self.samplerate, blocking=True)

    def space_word(self):
        duration = numpy.arange(int(numpy.ceil(self.dit_duration * 7 * self.samplerate))) / self.samplerate
        space = self.volume * numpy.sin(numpy.pi*0*duration)
        sd.play(space, self.samplerate, blocking=True)

    def space_units(self):
        time.sleep(self.dit_duration)

    def play_letter(self, letter):
        morse = self.letter_dictionary[letter.upper()]
        if self.debug:
            print(letter.upper(), end=" ", flush=True)
        for bit in morse:
            if bit == "0":
                if self.debug:
                    print(".", end="", flush=True)
                self.dit()
            elif bit == "1":
                if self.debug:
                    print("-", end="", flush=True)
                self.dah()
        if self.debug:
            print(" ")
        self.space_letter()

    def play_word(self, word, repeat=1):
        for letter in word:
            if letter.upper() in self.letter_dictionary.keys():
                self.play_letter(letter)
            elif letter == " ":
                if self.debug:
                    print(" ")
                self.space_word()
