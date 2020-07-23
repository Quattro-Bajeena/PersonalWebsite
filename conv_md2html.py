from pathlib import Path
import subprocess
from app import app

articles_path = Path('app/static') / app.config['ARTICLES_FOLDER']

for article in articles_path.glob('*.md'):
    cmd = f'pandoc {article} -f markdown -t html -o {articles_path / article.stem}.html'
    subprocess.run(cmd, shell=True)
    