#       ▄▀█ █▀▄▀█ █▀█ █▀█ █▀▀
#      	█▀█ █░▀░█ █▄█ █▀▄ ██▄

#         © Copyright 2022

#       https://t.me/amorescam

#     🔒 Licensed under the GNU GPLv3
#     🧟‍♂️ Not for open source

import csv


def csv_to_dictList(file):
    reader = csv.DictReader(open(file, 'r'))
    dictList = [line for line in reader]
    return dictList
