import os
from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Seed database with initial data'

    def handle(self, *args, **kwargs):
        # Directorio donde se encuentran los archivos JSON
        fixtures_dir = os.path.join('web', 'base')

        # Lista de archivos JSON
        files = ['CategoriasProducto.json', 'Flan.json', 'usuarios.json']

        for file in files:
            file_path = os.path.join(fixtures_dir, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    call_command('loaddata', file_path)
                    self.stdout.write(self.style.SUCCESS(f'Successfully loaded {file}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error loading {file}: {e}'))