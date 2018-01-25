import sys
import importlib
importlib.reload(sys)

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

def seal_pdf(file_path):
    fp = open(file_path, "rb")
    paser = PDFParser(fp)
    doc = PDFDocument()
    paser.set_document(doc)
    doc.set_parser(paser)
    doc.initialize()

    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        prm = PDFResourceManager()
        lap = LAParams()
        dev = PDFPageAggregator(prm, lap)
        inter = PDFPageInterpreter(prm, dev)
        for page in doc.get_pages():
            # print(page.pageid)
            inter.process_page(page)
            layout = dev.get_result()
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open(r'/home/faith/FaithMove/Python_base/python/1.txt', 'a') as f:
                        results = x.get_text()
                        print(results)
                        f.write(results + '\n')

if __name__ == "__main__":
    file_path = "/home/faith/FaithMove/Python_base/python/test_pdf/hh.pdf"
    seal_pdf(file_path=file_path)
