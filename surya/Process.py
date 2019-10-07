import pandas as pd
import torchtext
from torchtext import data
from Tokenize import tokenize 
from Batch import MyIterator, batch_size_fn
import os
import dill as pickle #TODO: What is dill

def read_data(opt):

	englist_data = open('data/english.txt').read()
	french_data = open('data/french.txt').read()

	#get spacy tokenizers
	en_tokenizer = tokenize('en')
	fr_tokenizer = tokenize('fr')

	SRC = data.Field(lower=True, tokenize=en_tokenizer.tokenizer)
	TRG = data.Field(lower=True, tokenize=fr_tokenizer.tokenizer, init_token='<sos>', eos_token='<eos>')

	return SRC, TRG



