from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notes', '0002_note_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='access',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]