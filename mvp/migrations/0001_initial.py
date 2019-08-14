# Generated by Django 2.2 on 2019-05-13 17:13

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DireccionEnvio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(help_text='Incluya dirección completa', max_length=150, verbose_name='Dirección')),
                ('localidad', models.CharField(max_length=50, verbose_name='Localidad')),
                ('provincia', models.CharField(max_length=25, verbose_name='Provincia')),
                ('codPostal', models.CharField(max_length=5, verbose_name='Código postal')),
            ],
        ),
        migrations.CreateModel(
            name='FormaCobro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoCobro', models.CharField(choices=[('TARJETA', 'Tarjeta de crédito'), ('CONTRA-REEMBOLSO', 'Contra-reembolso'), ('EFECTIVO', 'Efectivo')], max_length=20, verbose_name='Tipo de cobro')),
            ],
        ),
        migrations.CreateModel(
            name='LineaEnvio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estadoEnvio', models.CharField(blank=True, choices=[('Enviado', 'Enviado'), ('EnProceso', 'En proceso'), ('Cancelado', 'Cancelado')], max_length=10, null=True, verbose_name='Estado de envío')),
                ('direccionEnvio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineaEnvio', to='mvp.DireccionEnvio')),
                ('formaCobro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineaEnvio', to='mvp.FormaCobro')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('foto', models.FileField(blank=True, null=True, upload_to='productos/fotos/', verbose_name='Foto')),
                ('tipo', models.CharField(choices=[('VERDURAS', 'Verduras'), ('FRUTAS', 'Frutas'), ('PANADERIA/BOLLERIA', 'Panadería y bollería'), ('LEGUMBRES', 'Legumbres'), ('PASTAS/ARROCES', 'Pastas y arroces'), ('HARINAS/CEREALES/SEMILLAS', 'Harinas, cereales y semillas'), ('FRUTOSSECOS/DESHIDRATADOS', 'Frutos secos y deshidratados'), ('LACTEOS/YOGURES/HUEVOS', 'Lácteos, yogures y huevos'), ('ACEITES/CONDIMENTOS/SAL', 'Aceites, condimentos y sal'), ('AZUCAR/MIEL', 'Azúcar y miel'), ('CONSERVAS/MERMELADAS', 'Conservas y mermeladas'), ('ZUMOS/CAFES/BEBIDAS', 'Zumos, cafés y bebidas'), ('INFUSIONES/TES/AROMATICAS', 'Infusiones, tés y aromáticas'), ('VINOS/CERVEZAS/LICORES', 'Vinos, cervezas y licores'), ('CHOCO/APERITIVOS/DULCES', 'Chocolate, aperitivos y dulces'), ('HIGIENE', 'Higiene personal'), ('LIMPIEZA', 'Productos de limpieza'), ('INFANTIL', 'Alimentación infantil'), ('ROPA/TEXTIL', 'Ropa y textil')], max_length=30, verbose_name='Tipo de producto')),
                ('certificacion', models.CharField(choices=[('Eco', 'Ecológico'), ('Km.0', 'Kilómetro cero')], max_length=5, verbose_name='Certificación')),
                ('precioUnidad', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Precio')),
                ('unidadMedida', models.CharField(choices=[('€/Kg.', '€/Kg.'), ('€/250gr.', '€/250gr.'), ('€/500gr.', '€/500gr.'), ('€/Ud.', '€/Ud.'), ('€/Manojo', '€/Manojo'), ('€/l.', '€/l.'), ('€/250ml.', '€/250ml.'), ('€/500ml.', '€/500ml.')], max_length=10, verbose_name='Unidad de medida')),
                ('stock', models.BooleanField(verbose_name='Stock')),
                ('infoAdicional', models.TextField(blank=True, help_text='Describe el producto', max_length=500, null=True, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='TipoRecogida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.TextField(max_length=100, verbose_name='Dirección')),
                ('diasYHoras', models.TextField(help_text='Escriba los días y horas de recogida. Por ejemplo: L --> 10:30 a 14:30, M --> 9:00 a 17:30', max_length=500, verbose_name='Días y horas de recogida')),
            ],
        ),
        migrations.CreateModel(
            name='TipoReparto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diasYHoras', models.TextField(help_text='Escriba los días y horas de reparto. Por ejemplo: L --> 10:30 a 14:30, M --> 9:00 a 17:30', max_length=500, verbose_name='Días y horas de reparto')),
            ],
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('mvp.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Consumidor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('mvp.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Productor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('descripcion', models.TextField(help_text='Describe tu empresa', max_length=500, verbose_name='Descripción')),
                ('telefono', models.CharField(max_length=9, verbose_name='Teléfono')),
                ('fotoLogo', models.FileField(blank=True, null=True, upload_to='productores/logos/', verbose_name='Logo')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('mvp.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=9, verbose_name='Teléfono')),
                ('fechaHora', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y hora')),
                ('detallesPedido', models.TextField(help_text='Escriba cualquier aclaración si lo desea', max_length=500, null=True, verbose_name='Detalles del pedido')),
                ('lineaEnvio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mvp.LineaEnvio')),
            ],
        ),
        migrations.CreateModel(
            name='Mensajeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Título')),
                ('fechaHora', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('comentario', models.TextField(max_length=500, verbose_name='Comentario')),
                ('emisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajesEnviados', to=settings.AUTH_USER_MODEL)),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajesRecibidos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LineaProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precioUnidadActual', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Precio actual')),
                ('cantidad', models.IntegerField(default=1, verbose_name='Cantidad')),
                ('producto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mvp.Producto')),
            ],
        ),
        migrations.AddField(
            model_name='lineaenvio',
            name='lineaProducto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mvp.LineaProducto'),
        ),
        migrations.AddField(
            model_name='lineaenvio',
            name='tipoRecogida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineaEnvio', to='mvp.TipoRecogida'),
        ),
        migrations.AddField(
            model_name='lineaenvio',
            name='tipoReparto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineaEnvio', to='mvp.TipoReparto'),
        ),
        migrations.AddField(
            model_name='tiporeparto',
            name='productor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipoReparto', to='mvp.Productor'),
        ),
        migrations.AddField(
            model_name='tiporecogida',
            name='productor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipoRecogida', to='mvp.Productor'),
        ),
        migrations.CreateModel(
            name='ReseñaProductor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaHora', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y hora')),
                ('calificacion', models.IntegerField(default=0, verbose_name='Calificación')),
                ('comentario', models.TextField(help_text='Escriba su comentario', max_length=200, verbose_name='Comentario')),
                ('consumidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reseñasProductor', to='mvp.Consumidor')),
                ('productor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mvp.Productor')),
            ],
        ),
        migrations.CreateModel(
            name='ReseñaProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaHora', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y hora')),
                ('calificacion', models.IntegerField(default=0, verbose_name='Calificación')),
                ('comentario', models.TextField(help_text='Escriba su comentario', max_length=200, verbose_name='Comentario')),
                ('producto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mvp.Producto')),
                ('consumidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reseñasProducto', to='mvp.Consumidor')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='productor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='mvp.Productor'),
        ),
        migrations.AddField(
            model_name='formacobro',
            name='productor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formaCobro', to='mvp.Productor'),
        ),
        migrations.AddField(
            model_name='direccionenvio',
            name='consumidor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='direccionEnvio', to='mvp.Consumidor'),
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Título')),
                ('fechaHora', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y hora')),
                ('articulo', models.TextField(help_text='Escriba el artículo', max_length=1000, verbose_name='Artículo')),
                ('foto', models.FileField(blank=True, null=True, upload_to='blog/fotos/', verbose_name='Foto')),
                ('administrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='mvp.Administrador')),
            ],
        ),
    ]