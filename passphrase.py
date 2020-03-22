#!/bin/python
import argparse
import random


def passphrase_generator(argv):
    # open the correct language
    language_file = 'languages/{}.txt'.format(argv.language)
    with open(language_file) as passphrases:
        inputs = passphrases.readlines()  # load the language file into a list
        # get random values from that list
        passphrase = random.sample(inputs, argv.count)
        # strip the list from any \n characters
        passphrase = [i.replace('\n', '') for i in passphrase]
        # should the output be case sensitive or insensitive?
        if argv.case_sensitive:
            passphrase = [word.capitalize() for word in passphrase]
        elif argv.case_insensitive:
            passphrase = [word.lower() for word in passphrase]
        # convert the list to a string and add a delimiter.
        passphrase = argv.delimiter.join(passphrase)
        print(passphrase)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--delimiter", default=' ',
                        help="Definiere das Trennzeichen (Standard: Leertaste)")
    parser.add_argument("-c", "--count", type=int,
                        default=4, help="Anzahl der Wörter")
    case_group = parser.add_mutually_exclusive_group()
    case_group.add_argument("-cs", "--case_sensitive", action="store_true",
                            help="Großschreibung aller Wörter aktivieren")
    case_group.add_argument("-ci", "--case_insensitive", action="store_true",
                            help="Kleinschreibung aller Wörter aktivieren")
    parser.add_argument("-n", "--numbers", action="store_true",
                        help="Füge Nummern im Passphrase hinzu")
    parser.add_argument("-l", "--language", action="store_true", default="de",
                        help="Sprache des Passphrases (Standard: Deutsch)")
    args = parser.parse_args()
    passphrase_generator(args)
