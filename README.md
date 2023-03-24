# Mood Analysis

This Python script analyzes the mood of a given text and returns a `Mood` object containing an emoji representing the mood (friendly, hostile, or neutral) and the sentiment polarity value. The script uses the TextBlob library for sentiment analysis.

## Dependencies

- Python 3.8 or later
- TextBlob

To install TextBlob, use the following command:

```python
pip install textblob
```

## Usage

Import the `get_mood` function and the `Mood` class from the module:

```python
from your_module import get_mood, Mood

input_text = 'I love this place! The staff is so friendly and helpful.'
threshold = 0.3
mood = get_mood(input_text, threshold=threshold)

```

The `get_mood` function returns a Mood object with two attributes:

- `emoji`: A string containing the emoji representing the mood ('😊' for friendly, '😠' for hostile, '😐' for neutral)
- `sentiment`: A float value representing the sentiment polarity (-1 to 1) of the input text

## Testing
To run the test cases, execute the test script with the unittest module:

```python
python -m unittest test_your_module.py
```

Replace test_your_module.py with the name of the test script containing the TestMoodAnalysis class and the test cases.

## License
This project is licensed under the MIT License.
