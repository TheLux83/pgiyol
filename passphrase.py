#!/bin/python
import argparse
import random
import os
import gettext
from pathlib import Path

# generate needed variables and functions to translate my app.
localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locales')
translate_de = gettext.translation('passphrase', localedir, fallback=True, languages=['de-DE'])
translate_en = gettext.translation('passphrase', localedir, fallback=True, languages=['en-US'])
translate_en.install()
_ = translate_en.gettext


def passphrase_generator(argv):
    # open the correct language
    data_folder = Path('languages/')
    language_file = data_folder / '{}.txt'.format(argv.language)
    with open(language_file) as passphrases:
        inputs = passphrases.readlines()  # load the language file into a list
        # get random values from that list
        passphrase = random.sample(inputs, argv.count)
        # strip the list from any \n characters
        passphrase = [i.replace('\n', '') for i in passphrase]
        # should the output be capitalized?
        if argv.capitalize:
            passphrase = [word.capitalize() for word in passphrase]
        # if the user wants numbers in his passphrase, we add them here
        if argv.numbers:
            if argv.count <= 3:
                min_count = 1
                max_count = argv.count
            else:
                min_count = 2
                max_count = random.randint(3, argv.count)
            number_items = random.sample(range(0,argv.count), random.randint(min_count,max_count))
            for item in number_items:
                change_word = passphrase[item] + str(random.randrange(9))
                passphrase[item] = change_word
        # convert the list to a string and add a delimiter.
        passphrase = argv.delimiter.join(passphrase)
        print(passphrase)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--delimiter", default=' ',
                        help=_("Define a delimiter for your passphrase (Standard: space)"))
    parser.add_argument("-c", "--count", type=int,
                        default=4, help=_("How many words should your passphrase have (Standard: 4)"))
    parser.add_argument("-ca", "--capitalize", action="store_true",
                        help=_("Activate capitalizing all words"))
    parser.add_argument("-n", "--numbers", action="store_true",
                        help=_("Add numbers to your passphrase"))
    parser.add_argument("-l", "--language", default="en",
                        help=_("Language of your passphrase (Standard: englisch)"))
    args = parser.parse_args()
    passphrase_generator(args)
