#       ▄▀█ █▀▄▀█ █▀█ █▀█ █▀▀
#      	█▀█ █░▀░█ █▄█ █▀▄ ██▄

#         © Copyright 2022

#       https://t.me/amorescam

#     🔒 Licensed under the GNU GPLv3
#     🧟‍♂️ Not for open source

from io import StringIO
from six import BytesIO as StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


def convert_pdf_to_txt(path, output_path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    with open(output_path, 'wb') as output_f:
        output_f.write(text)
        output_f.close()

    return text


if __name__ == "__main__":
    data_path = 'parse/resumes/'
    input_path = data_path + 'fResume.pdf'
    output_path = 'parse/outputtext.txt'
    convert_pdf_to_txt(input_path, output_path)
