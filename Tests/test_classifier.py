from Python_project import Classify_mood_state

def test_positive_mood():
    assert Classify_mood_state("I'm happy today") == 'positive'
    
def test_negative_mood():
    assert Classify_mood_state("I'm sad today") == 'negative'

def test_neutral_mood():
    assert Classify_mood_state("I'am sleepy today") == "neutral"
    
def test_invalid_format():
    assert "Could not detect" in Classify_mood_state("I'm feeling lonely today") 