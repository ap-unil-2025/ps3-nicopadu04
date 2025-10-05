"""
Problem 4: File Word Counter
Process text files and perform various analyses.
"""

def create_sample_file(filename="sample.txt"):
    """Create a sample text file for testing."""
    content = """Python is a powerful programming language.
It is widely used in web development, data science, and automation.
Python's simple syntax makes it great for beginners.
Many companies use Python for their projects."""

    with open(filename, 'w') as f:
        f.write(content)
    print(f"Created {filename}")


def count_words(filename):
    """Count total words in the file."""
    with open(filename, 'r') as f:
        content = f.read()
        words = content.split()
        return len(words)


def count_lines(filename):
    """Count total lines in the file."""
    with open(filename, 'r') as f:
        lines = f.readlines()
        return len(lines)


def count_characters(filename, include_spaces=True):
    """Count characters in the file."""
    with open(filename, 'r') as f:
        content = f.read()
        if include_spaces:
            return len(content)
        else:
            return len(content.replace(' ', '').replace('\n', ''))


def find_longest_word(filename):
    """Find and return the longest word in the file."""
    import string
    
    with open(filename, 'r') as f:
        content = f.read()
        words = content.split()
        
        longest = ""
        for word in words:
            clean_word = word.strip(string.punctuation)
            if len(clean_word) > len(longest):
                longest = clean_word
        
        return longest


def word_frequency(filename):
    """Return a dictionary of word frequencies."""
    import string

    frequency = {}

    with open(filename, 'r') as f:
        content = f.read()
        words = content.split()
        
        for word in words:
            clean_word = word.lower().strip(string.punctuation)
            
            if clean_word:
                if clean_word in frequency:
                    frequency[clean_word] += 1
                else:
                    frequency[clean_word] = 1

    return frequency


def analyze_file(filename):
    """Perform complete analysis of the file."""
    print(f"\nAnalyzing: {filename}")
    print("-" * 40)

    try:
        print(f"Lines: {count_lines(filename)}")
        print(f"Words: {count_words(filename)}")
        print(f"Characters (with spaces): {count_characters(filename, True)}")
        print(f"Characters (without spaces): {count_characters(filename, False)}")
        print(f"Longest word: {find_longest_word(filename)}")

        print("\nTop 5 most common words:")
        freq = word_frequency(filename)

        top_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
        for word, count in top_words:
            print(f"  '{word}': {count} times")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Main function to run the file analyzer."""
    create_sample_file()
    analyze_file("sample.txt")

    print("\n" + "=" * 40)
    user_file = input("Enter a filename to analyze (or press Enter to skip): ").strip()
    if user_file:
        analyze_file(user_file)


if __name__ == "__main__":
    main()