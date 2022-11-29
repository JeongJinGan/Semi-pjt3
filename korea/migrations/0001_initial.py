from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=7)),
                ('english_name', models.CharField(max_length=20)),
                ('back_number', models.IntegerField()),
                ('birthdate', models.DateField()),
                ('team', models.CharField(max_length=20)),
                ('player_image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='')),
                ('position', models.CharField(max_length=10)),
                ('height', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('like_users', models.ManyToManyField(related_name='like_comments', to=settings.AUTH_USER_MODEL)),
                ('players', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='korea.players')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
