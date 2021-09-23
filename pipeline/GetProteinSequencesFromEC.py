'''
Este programa faz o download de sequências de proteínas de um dado EC para a taxonomomia Viridiplantae
Os arquivos são baixados do site Uniprot usando uma URL. Exemplo:
https://www.uniprot.org/uniprot/?query=taxonomy:33090+AND+ec:3.2.1.23&format=fasta

Como usar o programa?
python3 GetProteinSequencesFromEC.py 2.1.1.141

@author: Waldeyr Mendes Cordeiro da Silva Março-2020
'''

import os
import sys
from textwrap import wrap
import urllib.request

def formatSequence(sequence, length):
    formatedSequence = ''
    listTemp = wrap(sequence, length)
    for temp in listTemp:
        formatedSequence = formatedSequence + str(temp) + '\n'
    return formatedSequence.rstrip('\n')

number_of_arguments = len(sys.argv)
if number_of_arguments == 2:
    # Arguments passed
    script_name = str(sys.argv[0])
    ec = str(sys.argv[1])
    print(f"\nRunning {script_name}\n")
    try:
        url = f'https://www.uniprot.org/uniprot/?query=taxonomy:33090+AND+ec:{ec}&format=fasta'
        with urllib.request.urlopen(url) as response, open(f"{ec}.faa", 'wb') as out_file:
            data = response.read()  # a bytes object
            out_file.write(data)
    except OSError:
        print("Could not open/read file:", str(sys.argv[1]))
        sys.exit()
else:
    print("Missing arguments.")
print("Done.")