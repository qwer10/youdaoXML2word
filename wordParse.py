import xml.sax
import sys
import time
class WordHandler(xml.sax.ContentHandler):
	def __init__(self):
		self.CurrentData = ''
		self.word = 'abc'
		self.phonetic = ''
		self.trans = ''
	
	def startElement(self, tag, attributes):
		self.CurrentData = tag
		
	
	def endElement(self, tag):
		# str = self.word + self.phonetic + self.trans + '\n'
		# f.write(str)
		# print(self.word, self.phonetic, self.trans)
		if self.CurrentData == 'word':
			# print(self.word, end = '')
			pass
		elif self.CurrentData == 'phonetic':
		    # print(self.phonetic, end = '')
		    pass
		elif self.CurrentData == 'trans':
			# print(self.trans)
			pass
		if tag == 'item':
			a = self.word.ljust(20)
			b = self.phonetic.ljust(20)
			c = self.trans.replace('\n', '   ').ljust(60)

			# str = self.word + self.phonetic + self.trans + '\n'
			str = a + b + c + '\n'
			# print(str)
			f.write(str)
			self.phonetic = ''
			self.trans = ''
		self.CurrentData = ""

	
	def characters(self, content):
		# print(content)
		# print(self.CurrentData)
		if self.CurrentData == 'word':
			self.word = content
		elif self.CurrentData == 'phonetic':
		    self.phonetic = self.phonetic + content
		 
		elif self.CurrentData == 'trans':
			self.trans = self.trans + content
			# print(self.trans)

if __name__ == '__main__':
	global f
	f = open("youdao.txt", 'r+', encoding='utf-8')
	parser = xml.sax.make_parser()
	handler = WordHandler()
	# parser.setContentHandler(handler)
	# ret = parser.parse("C:\\Users\\10251\\Documents\\YouDaoDic.xml")
	# parser.parse('C:\\Users\\10251\\Documents\\YouDaoDic.xml', handler)
	xml.sax.parse('C:\\Users\\10251\\Documents\\YouDaoDic.xml', handler)
	# with open("youdao.txt", 'r+') as f:
	# 	f.write("abc")
	f.close()
