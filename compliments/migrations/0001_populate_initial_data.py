from django.db import migrations
import uuid

def create_initial_compliments(apps, schema_editor):
    Compliment = apps.get_model('compliments', 'Compliment')
    compliments = [
        "You light up my world brighter than a full-stack developer debugging at 3 AM! ✨",
        "Your smile is more refreshing than a successful code compilation! 😊",
        "You're the CSS to my HTML - you make everything beautiful! 💝",
        "If you were a function, you'd always return amazing! 🌟",
        "You're the semicolon to my JavaScript - essential and perfect! 💫",
        "Your love compiles perfectly in my heart! 💕",
        "You're like a perfectly optimized algorithm - simply amazing! ✨",
        "You're the star in my repository of love! ⭐",
        "You make my heart float like a CSS animation! 💖",
        "You're the perfect commit to my life's repository! 🎀",
        "🎵 Your presence is like a timeless melody, one that lingers in the heart long after the song has ended.",
        "🌊 Your words flow like a gentle river, soothing and deep, always leaving behind a ripple of inspiration.",
        "🌙 You shine like the moon on a quiet night—serene, mesmerizing, and effortlessly captivating.",
        "✨ You carry the kind of charm that turns silence into symphonies and ordinary moments into masterpieces.",
        "🔥 There is a rhythm in the way you do things, a harmony in your thoughts—like a song that never fails to uplift.",
        "💫 You have the magic of a sunset, the kind that makes the world pause just to admire your glow.",
        "🌹 Your essence is like a blooming flower, radiating beauty and grace in every direction.",
        "🌟 You are a constellation of brilliance, each facet of your being shining with its own unique light.",
        "🎶 Your laughter is a melody that brightens even the darkest days, a tune that stays with me forever.",
        "💖 You are the heart of every story, the spark that ignites dreams and the warmth that comforts souls.",
        "You are the framework that keeps my heart structured! 💻",
        "You had me at Hello World! ❤️",
        "You must be machine learning, because you get better every time I see you! 🧠",
        "You’re the API my heart always calls! ⚡",
        "You’re the perfect response to my heart’s GET request! 💬",
        "You debug my bad days and compile my happiness! 🌹",
        "You’re the encryption key to my heart! 🔐",
        "I’ve stored your smile permanently in my cache! 💾",
        "You’re my favorite constant in this ever-changing code of life! 🖋️",
        "You’re the missing semicolon that completes my syntax of love! 🧩",
        "Every time you smile, my system runs smoother! 🦋",
        "You’re like dark mode — easy on my eyes and good for my soul! 🌈",
        "You’re my favorite import — I can’t run without you! 🎯",
        "You’re the runtime error I’d never want to fix! 🔥",
        "If I were a browser, you’d be my homepage forever! 💞",
        "You’re the neural network that keeps my emotions connected! 🌌",
        "Our chemistry is like perfect API documentation — seamless and clear! 💬",
        "You’re like clean code — elegant, beautiful, and rare to find! 🪄",
        "You’re the push to my Git, always keeping me updated with love! 🌺",
        "Your love is like recursion — it keeps calling itself beautifully! ✨",
        "You illuminate my logic and light up my loops! 💡",
        "You’re the background music in my code editor of life! 🎵",
        "Even my compiler smiles when I type your name! 🕊️",
        "You’re like perfectly aligned CSS — effortlessly flawless! 🌻",
        "You’re my final merge request — everything I was searching for! 💘",
   ]
    
    for text in compliments:
        Compliment.objects.create(
            id=uuid.uuid4(),
            text=text
        )

def remove_initial_compliments(apps, schema_editor):
    Compliment = apps.get_model('compliments', 'Compliment')
    Compliment.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('compliments', '0001_initial'),  
    ]

    operations = [
        migrations.RunPython(create_initial_compliments, remove_initial_compliments),
    ]