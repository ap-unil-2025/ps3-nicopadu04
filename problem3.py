"""
Problem 3: Number Analysis
Analyze a list of numbers entered by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.
    """
    numbers = []
    
    while True:
        user_input = input("Enter a number: ")
        
        if user_input.lower() == 'done':
            break
        
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input! Please enter a number or 'done'.")
    
    return numbers


def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers
    """
    if not numbers:
        return None
    
    analysis = {}
    
    analysis['count'] = len(numbers)
    analysis['sum'] = sum(numbers)
    analysis['average'] = analysis['sum'] / analysis['count']
    analysis['minimum'] = min(numbers)
    analysis['maximum'] = max(numbers)
    
    even_count = 0
    odd_count = 0
    
    for num in numbers:
        if int(num) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    analysis['even_count'] = even_count
    analysis['odd_count'] = odd_count
    
    return analysis


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.
    """
    if analysis is None:
        print("No analysis to display!")
        return
    
    print("\nAnalysis Results:")
    print("-----------------")
    print(f"Count: {analysis['count']}")
    print(f"Sum: {analysis['sum']:.0f}")
    print(f"Average: {analysis['average']:.2f}")
    print(f"Minimum: {analysis['minimum']:.0f}")
    print(f"Maximum: {analysis['maximum']:.0f}")
    print(f"Even numbers: {analysis['even_count']}")
    print(f"Odd numbers: {analysis['odd_count']}")


def main():
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    
    numbers = get_numbers_from_user()
    
    if not numbers:
        print("No numbers entered!")
        return
    
    analysis = analyze_numbers(numbers)
    display_analysis(analysis)


if __name__ == "__main__":
    main()