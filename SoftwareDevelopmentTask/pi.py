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

### Time complexity: at the beginning, given that the number of logs is n, ordering them in a list, is O(n).  
### The loop runs on all of the size 2 subsets of the list of logs, which means: O(n^2) iterations,
### given that the number of logs is n. Given that the longest log length is m,
### the time complexity for each iteration is O(m) for the replace procedure, O(m) for split and O(m) for the set procedure.
### Given that t is the number of words in a log sentence, the set-minus operation takes O(t). Pop procedure is O(1).
### To conclude: the runtime of this code is: O((n^2) * (m + t))

### If I had two weeks for this assignment, I would choose to train a TF-IDF algorithm with data I already grouped, and help it recognize
### the structures appearing in this kind of logs. The TF-IDF grades strings according to a given scale, using cosine functions,
### and then finds the closest match to the given string. I Believe it would improve the time complexity inside each iteration.
