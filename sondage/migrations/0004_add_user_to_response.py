from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sondage', '0003_remove_option_likert_value_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='user',
            field=models.ForeignKey(
                to='auth.user',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='responses',
                null=True
            ),
        ),
    ] 