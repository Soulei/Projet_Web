# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texte', models.TextField()),
                ('date_creation', models.DateTimeField(default=django.utils.timezone.now)),
                ('approuve', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Portraits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='pasDimageDispo.png', upload_to='images/')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('date_naissance', models.DateField()),
                ('date_mort', models.DateField(null=True)),
                ('description', models.TextField()),
                ('faits', models.TextField()),
                ('fonctions', models.TextField()),
                ('oeuvres', models.TextField()),
                ('citations', models.TextField()),
                ('date_publication', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('avatar', models.ImageField(default='pasDimageDispo.png', upload_to='images/')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='portraits',
            name='ajouteePar',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commentaire',
            name='auteur',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commentaire',
            name='portraits',
            field=models.ForeignKey(related_name='commentaires', to='roots.Portraits'),
        ),
    ]
