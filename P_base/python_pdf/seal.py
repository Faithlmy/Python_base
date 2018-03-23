# from pdfminer.pdfinterp import PDFResourceManager, process_pdf
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from io import StringIO
# from io import open
#
#
# def readPDF(pdfFile):
#     rsrcmgr = PDFResourceManager()
#     retstr = StringIO()
#     laparams = LAParams()
#     device = TextConverter(rsrcmgr, retstr, laparams=laparams)
#
#     process_pdf(rsrcmgr, device, pdfFile)
#     device.close()
#
#     content = retstr.getvalue()
#     retstr.close()
#     return content
#
#
# def saveTxt(txt):
#     with open("istxt.txt", "w") as f:
#         f.write(txt)
#
# if __name__ == "__main__":
#     txt = readPDF(open('/root/pdf/meng.pdf', 'rb'))
#     saveTxt(txt)



from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content

pdfFile = open('/root/pdf/meng.pdf', 'rb')
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()
