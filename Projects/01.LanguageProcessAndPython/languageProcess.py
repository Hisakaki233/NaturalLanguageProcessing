from nltk.book import *

print(text1.concordance("monstrous"))
print("---------------------")
print(text1.similar("monstrous"))
print("---------------------")
print(text2.common_contexts(["monstrous", "very"]))
print("---------------------")


# Dispersion Plot
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
print("---------------------")


# Total Document Length
def document_tokens(text):
    return len(text)


# Avg. word frequency
def lexical_diversity(text):
    return len(text) / len(set(text))


# Frequency of a specific word
def wordFrequency(text, word):
    return text.count(word)


if __name__ == '__main__':

    # Frequency Distribution
    fdist = FreqDist(text1)

    # Accumulative Percentage Chart
    fdist.plot(50, cumulative=True)

    # Select Long Words
    V = set(text1)
    long_words = [w for w in V if len(w) > 15]
    print(sorted(long_words))

    # Combine Length and Frequency restriction together
    fdist1 = FreqDist(text5)
    meaningfulWords = [w for w in set(text5) if len(w) > 7 and fdist1[w] > 7]
    print(meaningfulWords)

    # Create Bigrams
    print(bigrams(['1', '2', '3', '4']))

    # collocations are just more frequent bigrams
    print(text4.collocations())
