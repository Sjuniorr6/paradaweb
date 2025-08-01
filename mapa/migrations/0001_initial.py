# Generated by Django 5.1.6 on 2025-03-06 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(blank=True, max_length=50, null=True, verbose_name='Identificador do Equipamento')),
                ('CCID', models.CharField(blank=True, max_length=50, null=True, verbose_name='CCID')),
                ('data_entrega', models.DateField(blank=True, null=True, verbose_name='Data de Entrega')),
                ('requisicao', models.CharField(max_length=100, verbose_name='Requisição')),
                ('cliente', models.CharField(max_length=150, verbose_name='Cliente')),
                ('local_entrega', models.CharField(max_length=200, verbose_name='Local de Entrega')),
                ('modelo', models.CharField(max_length=100, verbose_name='Modelo')),
                ('sla_insercao', models.IntegerField(blank=True, null=True, verbose_name='SLA de Inserção')),
                ('sla_viagem', models.IntegerField(blank=True, null=True, verbose_name='SLA de Viagem')),
                ('sla_retirada', models.IntegerField(blank=True, null=True, verbose_name='SLA de Retirada')),
                ('sla_envio_brasil', models.IntegerField(blank=True, null=True, verbose_name='SLA de Envio ao Brasil')),
                ('sla_operacao', models.IntegerField(blank=True, null=True, verbose_name='SLA da Operação')),
                ('data_insercao', models.DateTimeField(blank=True, null=True, verbose_name='Data de Inserção')),
                ('data_chegada_destino', models.DateField(blank=True, null=True, verbose_name='Data de Chegada no Destino')),
                ('data_retirada', models.DateField(blank=True, null=True, verbose_name='Data de Retirada')),
                ('data_envio_brasil', models.DateField(blank=True, null=True, verbose_name='Data de Envio ao Brasil')),
                ('data_brasil', models.DateField(blank=True, null=True, verbose_name='Data no Brasil')),
                ('BL', models.CharField(blank=True, max_length=100, null=True, verbose_name='BL')),
                ('container', models.CharField(blank=True, max_length=100, null=True, verbose_name='Container')),
                ('status_operacao', models.CharField(choices=[('em_viagem', 'Em Viagem'), ('no_destino', 'No Destino'), ('desacoplado', 'Desacoplado'), ('em_estoque', 'Em Estoque'), ('na_fazenda', 'Na Fazenda')], default='em_viagem', max_length=20, verbose_name='Status da Operação')),
                ('reposicao', models.CharField(blank=True, max_length=100, null=True, verbose_name='Reposição')),
                ('observacao', models.TextField(blank=True, null=True, verbose_name='Observação')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Latitude')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Longitude')),
                ('destino', models.CharField(blank=True, max_length=50, null=True, verbose_name='Destino')),
                ('data_embarque_maritimo', models.CharField(blank=True, db_column='Data_Embarque_Maritimo', max_length=50, null=True, verbose_name='Data de Embarque Marítimo')),
                ('data_desembarque_maritimo', models.DateField(blank=True, db_column='Data_Desembarque_Maritimo', null=True, verbose_name='Data de Desembarque Marítimo')),
                ('sla_terrestre', models.IntegerField(blank=True, db_column='SLA_Terrestre', null=True, verbose_name='SLA Terrestre')),
                ('sla_maritimo', models.IntegerField(blank=True, db_column='SLA_Maritimo', null=True, verbose_name='SLA Marítimo')),
                ('local_atual', models.CharField(blank=True, db_column='Local', max_length=100, null=True, verbose_name='Local')),
                ('status_do_container', models.CharField(blank=True, db_column='Status_do_Container', max_length=100, null=True, verbose_name='Status do Container')),
                ('data_do_desembarque', models.DateField(blank=True, db_column='Data_do_Desembarque', null=True, verbose_name='Data do Desembarque')),
            ],
        ),
    ]
