import sqlite3
import os
import pandas as pd
import kaggle
kaggle.api.authenticate()
kaggle.api.dataset_download_files("nageshsingh/dna-sequence-dataset", path=".", unzip=True)
dna_kaggle_human = pd.read_table("human.txt")
dna_human = dna_kaggle_human.drop_duplicates().dropna()
dna_human.reset_index(drop=True, inplace=True)
dna_kaggle_dog = pd.read_table("dog.txt")
dna_dog = dna_kaggle_dog.drop_duplicates().dropna()
dna_dog.reset_index(drop=True, inplace=True)
dna_kaggle_monke = pd.read_table("chimpanzee.txt")
dna_monke = dna_kaggle_monke.drop_duplicates().dropna()
dna_monke.reset_index(drop=True, inplace=True)
conect = sqlite3.connect('database.db')
dna_human.to_sql("dna_human", con = conect, if_exists = 'replace')
dna_monke.to_sql("dna_monke", con = conect, if_exists = 'replace')
dna_dog.to_sql("dna_dog", con = conect, if_exists = 'replace')
conect.close()