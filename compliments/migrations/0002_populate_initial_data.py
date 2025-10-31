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
    ]
    
    for text in compliments:
        Compliment.objects.create(id=uuid.uuid4(), text=text)

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
