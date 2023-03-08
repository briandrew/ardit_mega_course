
def sentence_maker(phrase):
    #need to deermine if a question is being asked or not
    interrogatives = ('how', 'what', 'when', 'who', 'where', 'why')
    #need to capitalize the input because will be first word in phrase sentence
    capitalized = phrase.capitalize()
    #now determine if a question
    if phrase.startswith(interrogatives):
        return f"{capitalized}"
    else:
        return f"{capitalized}"




results = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(results) #prints the list in []
print(' '.join(results)) #to print a normal sentence
