from django.db import migrations

def create_initial_votes(apps, schema_editor):
    Vote = apps.get_model('polls', 'Vote')
    days = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    for day in days:
        Vote.objects.create(day=day)

class Migration(migrations.Migration):
    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_votes),
    ]