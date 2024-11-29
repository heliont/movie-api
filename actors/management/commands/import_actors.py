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
            # Leitura do arquivo CSV e inserindo ou atualizando no banco de dados
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row['name']
                    birthday = datetime.strptime(row['birthday'], '%Y-%m-%d').date()
                    nationality = row['nationality']
                    actor_id = row['id']  # Supondo que o CSV tenha um campo 'id'

                    # Exibir o registro que está sendo processado
                    self.stdout.write(self.style.NOTICE(f'Processando: {actor_id} - {name}'))

                    # Verificar se o ator com o ID já existe
                    actor = Actor.objects.filter(id=actor_id).first()

                    if actor:
                        # Se o ator já existe, atualize
                        actor.name = name
                        actor.birthday = birthday
                        actor.nationality = nationality
                        actor.save()
                        self.stdout.write(self.style.SUCCESS(f'Ator {actor_id} - {name} atualizado com sucesso.'))
                    else:
                        # Caso contrário, crie um novo ator
                        Actor.objects.create(
                            # Certifique-se de que o id é único
                            id=actor_id,
                            name=name,
                            birthday=birthday,
                            nationality=nationality
                        )
                        self.stdout.write(self.style.SUCCESS(f'Ator {actor_id} - {name} criado com sucesso.'))

                # Print do resultado
                self.stdout.write(self.style.SUCCESS(f'Arquivo {file_name} processado com sucesso.'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'O arquivo {file_name} não foi encontrado em _import.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ocorreu um erro: {str(e)}'))
