from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Repository', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questiondb',
            name='notes',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
