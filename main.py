from collections import Counter
import matplotlib.pyplot as plt


# Parse text into words and remove whitespace and punctuation, except apostrophes
def parse_words(text: str) -> list[str]:
    punctuation = r"""!"#$%&()*+,-./:;<=>?@[\]^_`{|}~"""
    text = text.casefold().replace('\n', ' ')
    translator = str.maketrans(punctuation, ' ' * len(punctuation))
    text = text.translate(translator)
    return text.split()


# Parse text into letters and remove whitespace and punctuation
def parse_letters(text: str) -> list[str]:
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    text = text.casefold().replace('\n', '')
    translator = str.maketrans(punctuation, ' ' * len(punctuation))
    text = text.translate(translator)
    text = text.replace(' ', '')
    return list(text)


def main():
    # Read the contents of the input file into a variable
    with open('input.txt', 'r') as file:
        text = file.read()
    # Parse the text
    parsed = parse_letters(text)
    # Count the frequency of unique items in the text
    count = Counter(parsed)
    # Sort the dictionary from greatest to least
    count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
    # Create x and y axes for a graph
    x = [i for i in count.keys()]
    y = [i for i in count.values()]
    # Create a graph with matplotlib
    plt.bar(x, y)
    # Show the graph
    plt.show()


if __name__ == '__main__':
    main()
