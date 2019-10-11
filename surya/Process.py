import pandas as pd
import torchtext
from torchtext import data
from Tokenize import tokenize 
from Batch import MyIterator, batch_size_fn
import os
import dill as pickle #TODO: What is dill

class Process:

	def __init__(self):
		max_length = 40
		batch_size = 1500
		
		pass

	def read_data(self):

		self.english_data = open('data/english.txt').read()
		self.french_data = open('data/french.txt').read()

		# Create the objects of tokenize
		en_tokenizer = tokenize('en')
		fr_tokenizer = tokenize('fr')

		# Field is used for pre-processing and post-processing
		self.SRC = data.Field(lower=True, tokenize=en_tokenizer.tokenizer)
		self.TRG = data.Field(lower=True, tokenize=fr_tokenizer.tokenizer, init_token='<sos>', eos_token='<eos>')

	def create_dataset(self):

		print('Creating dataset and iterator')

		raw_data = {'src': [line for line in self.english_data], 'trg': [line for line in self.french_data]}
		df = pd.DataFrame(raw_data, columns=['src', 'trg'])

		mask = (df['src'].str.count(' ') < this.max_length) & (df['trg'].str.count(' ') < this.max_length)
		df = df.loc[mask]

		df.to_csv('data/translate_sentences.csv', index=False)

		data_fields = [('src', self.SRC), ('trg', self.TRG)]
		train = data.TabularDataset(path='data/translate_sentences.csv', format='csv', feilds=data_fields)

		train_iter = MyIterator(train, batch_size=)




