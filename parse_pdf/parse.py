#       ▄▀█ █▀▄▀█ █▀█ █▀█ █▀▀
#      	█▀█ █░▀░█ █▄█ █▀▄ ██▄

#         © Copyright 2022

#       https://t.me/amorescam

#     🔒 Licensed under the GNU GPLv3
#     🧟‍♂️ Not for open source

from parse_pdf.pdftxt import convert_pdf_to_txt
from parse_pdf.indexer import return_index


def parse_resume(resume_path):
    input_path = resume_path
    output_path = 'parse_pdf/outputtext.txt'
    convert_pdf_to_txt(input_path, output_path)
    indexed = return_index(output_path)
    print(indexed)
    return indexed


if __name__ == "__main__":
    parse_resume('resume/fResume.pdf')
