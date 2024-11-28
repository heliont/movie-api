from django.core.management.base import BaseCommand
from django.conf import settings
from datetime import datetime
import csv
import os
from actors.models import Actor


class Command(BaseCommand):
    help = 'Comando para importar lista de atores.'

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo CSV com atores'
        )

    def handle(self, *args, **options):
        file_name = options['file_name']

        # Caminho completo do arquivo dentro de _import
        file_path = os.path.join(settings.BASE_DIR, '_import', file_name)

        print(file_path)

        try:
            # Leitura do arquivo CSV e inserindo no banco de dados
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row['name']
                    birthday = datetime.strptime(row['birthday'], '%Y-%m-%d').date()
                    nationality = row['nationality']

                    # Exibir o registro que esta sendo executado
                    self.stdout.write(self.style.NOTICE(f'Processando: {name}'))

                    Actor.objects.create(
                        name=name,
                        birthday=birthday,
                        nationality=nationality
                    )
                # Print do resultado
                self.stdout.write(self.style.SUCCESS(f'Arquivo {file_name} processado com sucesso.'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'O arquivo {file_name} não foi encontrado em _import.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ocorreu um erro: {str(e)}'))
