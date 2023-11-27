# Generated by Django 4.2.7 on 2023-11-27 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=50, unique=True)),
                ('contraseña', models.CharField(max_length=50)),
                ('apellido', models.CharField(blank=True, max_length=50, null=True)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('fnac', models.DateField()),
                ('mail', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Ingrese un Título para producto ', max_length=50)),
                ('descripcion', models.CharField(help_text='Ingrese una descripcion del producto', max_length=100)),
                ('foto1', models.ImageField(upload_to='valioso_Mapp')),
                ('foto2', models.ImageField(upload_to='valioso_Mapp')),
                ('foto3', models.ImageField(upload_to='valioso_Mapp')),
                ('create', models.DateTimeField(auto_now=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('usuario_prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
            },
        ),
    ]