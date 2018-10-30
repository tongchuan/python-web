
from flask import render_template
from controller.base import BaseClass

class IndexClass(BaseClass):
	"""docstring for IndexClass"""
	def __init__(self):
		super(BaseClass,self).__init__()
		# super(self).__init__()

	def index_function(self):
		return render_template('index.html', name='dddd')
		return '33333'
	
	def test_function(self):
		return self.getDateTime() +'==='+ self.getDateTime2()