#tool for random redditor

user_input = input('Please enter the name of the input file containing the phrases to modify: ')
all_output_phrases = []
with open(user_input,'r') as phrases_file:
    for phrase in phrases_file:
        capitalised_list = []
        new_phrase = phrase.replace('b','bb')
        new_phrase = new_phrase.replace('e','3')
        phrase_list = new_phrase.split(' ')
        for word in phrase_list:
            capitalised_last = word[-1:]
            capitalised_last = capitalised_last.upper()
            word = word[:-1] + capitalised_last
            capitalised_list.append(word)
        all_rules_applied = ' '.join(capitalised_list)
        all_output_phrases.append(all_rules_applied)
with open('output.txt', 'w') as output:
    for line in all_output_phrases:
        output.write(line)

print('\nAll done, converted phrases written to output.txt')
