import docx

'''
    1. dictionary
        - encoding
        - file
    2. replacing
'''

#load dictionary

#load file
input_file = docx.Document('example.docx')
input_dictionary = docx.Document('dictionary.docx')

paragraph_as_list = []
dictionary_as_dict = {}

#get dict from file
for key_value in input_dictionary.paragraphs:    
    key_value.text.replace(' ','')
    key = key_value.text.split(':')[0]
    value = key_value.text.split(':')[1]
    dictionary_as_dict.update({key:value})


#convert paragraph > list of elements
for paragraph in input_file.paragraphs:
    paragraph_as_list.append(paragraph.text.replace('\t',' ').split(' '))     #need to use regex...

#do replace
for each_paragraph in paragraph_as_list:
    for each_element in each_paragraph:
        try:
            if dictionary_as_dict[each_element]:
                each_paragraph[each_paragraph.index(each_element)] = dictionary_as_dict[each_element]
        except KeyError as e:
            pass


#save
replaced_example = docx.Document()

for each_paragraph in paragraph_as_list:
    replaced_example.add_paragraph(' '.join(each_paragraph))
    
replaced_example.save('replaced.docx')