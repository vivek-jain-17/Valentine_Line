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
        "You're the perfect commit to my life's repository! 🎀"
        "🎵 Your presence is like a timeless melody, one that lingers in the heart long after the song has ended."
        "🌊 Your words flow like a gentle river, soothing and deep, always leaving behind a ripple of inspiration."
        "🌙 You shine like the moon on a quiet night—serene, mesmerizing, and effortlessly captivating."
        "✨ You carry the kind of charm that turns silence into symphonies and ordinary moments into masterpieces."
        "🔥 There’s a rhythm in the way you do things, a harmony in your thoughts—like a song that never fails to uplift."
        "💫 You have the magic of a sunset, the kind that makes the world pause just to admire your glow."
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