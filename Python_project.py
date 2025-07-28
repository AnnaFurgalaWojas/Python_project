# New project as Mood classifier base on general statement.

positive_words = {"happy",
    "joyful",
    "cheerful",
    "excited",
    "grateful",
    "thankful",
    "hopeful",
    "content",
    "optimistic",
    "loved",
    "peaceful",
    "satisfied",
    "enthusiastic",
    "delighted",
    "amused",
    "inspired",
    "blessed",
    "relaxed",
    "amazing",
    "awesome",
    "fantastic",
    "great",
    "wonderful",
    "pleasant",
    "lovely",
    "sweet",
    "encouraged",
    "confident",
    "motivated",
    "proud"}


negative_words = {"sad",
    "angry",
    "upset",
    "depressed",
    "frustrated",
    "anxious",
    "worried",
    "afraid",
    "lonely",
    "unhappy",
    "miserable",
    "terrible",
    "horrible",
    "hate",
    "annoyed",
    "disappointed",
    "guilty",
    "jealous",
    "bored",
    "tired",
    "stressed",
    "nervous",
    "resentful",
    "hurt",
    "ashamed",
    "fearful",
    "hopeless",
    "worthless",
    "discouraged",
    "embarrassed"}

def Classify_mood_state(response: str) ->str:
    response = response.strip().lower()
    words = response.split()
    mood_word= None
    
    if "I'm" in words and "today" in words:
        try:
            i = words.index("I'm")
            j = words.index("today")
            if j - i == 2:
                mood_word = words[i + 1]
        except ValueError:
            pass  # Unexpected format
        
            if not mood_word:
        return "Could not detect mood word. Use format: 'I'm <feeling> today'."

    if mood_word in positive_words:
        return "positive"
    elif mood_word in negative_words:
        return "negative"
    else:
        return "neutral"
    
    
    
    
print("How do you feel today?")
response = input("Enter your answer (e.g. I'm happy today): ")
mood = Classify_mood_state(response)
print(f"Detected mood: {mood}")