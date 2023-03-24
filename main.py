from textblob import TextBlob
from dataclasses import dataclass


@dataclass
class Mood:
    emoji: str
    sentiment: float


def get_mood(input_text: str, *, threshold: float) -> Mood:
    """
    Analyze the mood of a given text and return a Mood object containing the emoji and sentiment polarity.

    :param input_text: The input text to be analyzed
    :param threshold: The sentiment threshold used for determining the friendly and hostile moods
    :return: A Mood object containing the emoji representing the mood and the sentiment polarity value
    """

    sentiment: float = TextBlob(input_text).sentiment.polarity

    # Define mood thresholds
    friendly_threshold: float = threshold
    hostile_threshold: float = -threshold

    # Determine the mood and return the corresponding emoji
    if sentiment >= friendly_threshold:
        return Mood('😊', sentiment)
    elif sentiment <= hostile_threshold:
        return Mood('😠', sentiment)
    else:
        return Mood('😐', sentiment)


if __name__ == '__main__':
    text: str = input('Text: ')
    mood: Mood = get_mood(text, threshold=0.3)

    print(f'{mood.emoji} ({mood.sentiment})')
