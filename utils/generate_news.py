import random
from data.categories import data

def generate_news(category):
    subject = random.choice(data[category]["subjects"])
    action = random.choice(data[category]["actions"])
    place = random.choice(data[category]["places"])

    headline = f"BREAKING: {subject} {action} in {place}!"
    paragraph = (
        f"In an unexpected turn of events, {subject} {action} earlier today in {place}. "
        "Sources close to the event report that the situation has left fans and citizens both surprised and intrigued. "
        "More details are awaited as the story develops."
    )

    return headline, paragraph
