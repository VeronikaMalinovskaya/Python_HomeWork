from os.path import exists
from Creating import creating
from Writing import writing_csv
from Writing import writing_txt

path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_csv()
writing_txt()