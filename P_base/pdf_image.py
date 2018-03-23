from reportlab.pdfgen import canvas
from reportlab.lib.units import cm, mm
from PyPDF2 import PdfFileWriter, PdfFileReader
import uuid
from PIL import Image
import os


def create_watermark(f_jpg, f_pdf, x, y, w, h):

    w_pdf = 20 * cm
    h_pdf = 20 * cm
    c = canvas.Canvas(f_pdf, pagesize=(w_pdf, h_pdf))
    c.setFillAlpha(0.3)  # 设置透明度
    c.drawImage(f_jpg, x * mm, y * mm, w * mm, h * mm)  # 这里的单位是物理尺寸
    c.save()
    return f_pdf


def add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out):
    pdf_output = PdfFileWriter()
    input_stream = open(pdf_file_in, 'rb')
    pdf_input = PdfFileReader(input_stream)

    # PDF文件被加密了
    if pdf_input.getIsEncrypted():
        print('该PDF文件被加密了.')
        # 尝试用空密码解密
        try:
            pdf_input.decrypt('')
        except Exception as e:
            print('尝试用空密码解密失败.')
            return False
        else:
            print('用空密码解密成功.')
    # 获取PDF文件的页数
    pageNum = pdf_input.getNumPages()
    # 读入水印pdf文件
    pdf_watermark = PdfFileReader(open(pdf_file_mark, 'rb'))
    # 给每一页打水印
    for i in range(pageNum):
        page = pdf_input.getPage(i)
        page.mergePage(pdf_watermark.getPage(0))
        page.compressContentStreams()  # 压缩内容
        pdf_output.addPage(page)
    outputStream = open(pdf_file_out, "wb")
    pdf_output.write(outputStream)
    return pdf_file_out


def seal_pdf(file_in, seal_path):
    # file_in = "D:/1590.pdf"
    # seal_path = "D:/222.jpg"
    file_path = []
    for i, seal in enumerate(seal_path):
        x, y = 150, 35
        y = 200 - y * i
        file_name = 'D:/' + str(uuid.uuid4()) + ".pdf"
        f_pdf = create_watermark(seal, file_name, x, y, 50, 25)
        file_out = 'D:/' + str(uuid.uuid4()) + ".pdf"
        add_watermark(file_in, f_pdf, file_out)
        file_in = file_out
        file_path.append(file_in)
    return file_path[-1]



if __name__ == "__main__":
    file_in = "/home/faith/FaithMove/Python_base/P_base/test_pdf"
    # seal_path = ["D:/222.jpg", "D:/1.jpg"]
    seal_path = ["/home/faith/FaithMove/Python_base/P_base/test_pdf/12.jpg"]
    path = seal_pdf(file_in, seal_path)

