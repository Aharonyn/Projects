logs = list(open("input.log", "r"))
num_of_logs = len(logs)
output = open("output.txt", "w")
output.write("=============================\n")

for i in range(num_of_logs): # iterating over all of the sentences
    sentence = logs[i].replace("\n", "") # removing whitespaces
    senset1 = set(sentence.split(" ")[2:]) # extracting the words out of the sentence, in a form of a set (without date and hour)
    for j in range(i+1, num_of_logs): # iterating over the rest of sentences
        sentence2 = logs[j].replace("\n", "")
        senset2 = set(sentence2.split(" ")[2:])
        minus = senset1 - senset2 # applying set-minus operation on both sets
        if len(minus) == 1: # indicates that only one word is different
            output.write(sentence + "\n")
            output.write(sentence2 + "\n")
            output.write("The changing word was: {i}, {j}\n\n".format(i = (senset1 - senset2).pop(), j = (senset2 - senset1).pop()))

output.write("=============================")
output.close()