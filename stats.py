#get string.puntuation
import string

""" #get book and return contents as string
def get_num_words(text_string):
    for char in string.punctuation:
        text_string = text_string.replace(char, " ")
    text_string = ' '.join(text_string.split())
    word_list = text_string.split()
    #filter word list
    filtered_word_list = [word for word in word_list if word.isalpha()]
    #return word_list
    word_count = len(filtered_word_list)
    #print(f'{word_count} words found in the document')
    return word_count """

def get_num_words(text_string):
    # This simple logic now gives the target word count (75,767)
    words = text_string.split()
    word_count = len(words)
    return word_count

#counts characters
def counting_characters(file_contents):
    dictionary = {}
    for character in file_contents:
        lowercase_char = character.lower()
        if lowercase_char.isalpha():
           dictionary[lowercase_char] = dictionary.get(lowercase_char, 0) + 1
    return dictionary

#function that sorts characters. Each character is in its own dictionary
def character_dict(dictionary):
    character_list = dictionary.items()
    sorted_chars = sorted(character_list, key = lambda item: item[1], reverse=True)
    return sorted_chars

#create list of dictionaries
def dict_grouping(sorted_chars):
    dict_of_dict = []
    for char, count in sorted_chars:
        char_dict = {'char': char, 'count': count}
        dict_of_dict.append(char_dict)
    return dict_of_dict


#runs when program is executed directly
#if __name__ == "__main__":
    #get_num_words()
   