#-*- conding:<utf-8> -*-
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from settings import *
import urllib.request
import os


def download():
	url = URL
	os.mkdir('source')
	title = './source/target.pdf'
	urllib.request.urlretrieve(url, title)
	print('Done Download')
	

def write():
	 input_path = './source/target.pdf'
	 output_path = './source/target.txt'
	 rsrcmgr = PDFResourceManager()
	 retstr = StringIO()
	 codec = 'utf-8'
	 laparams = LAParams()
	 device = TextConverter(rsrcmgr, retstr, laparams=laparams)
	 with open(input_path, encoding=codec) as file:
	 	interpreter = PDFPageInterpreter(rsrcmgr, device)
	 	pages = PDFPage.get_pages(file)
	 	for page in pages:
	 		interpreter.process_page(page)
	 		
	 	print(retstr.getvalue())
	 	file.close()
	 	device.close()
	 	retstr.close()
	 	
	 	
if __name__ == "__main__":
	#download()
	write()
