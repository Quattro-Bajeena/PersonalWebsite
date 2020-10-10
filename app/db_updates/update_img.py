from pathlib import Path
from PIL import Image

#how to import app??

from app import app, db
from app.models import Art
from config import basedir

from flask_sqlalchemy import SQLAlchemy


art_folder =Path('app/static') / app.config['ART_FOLDER']

art_folder_rel = app.config['ART_FOLDER']

drawings_search_path = art_folder / 'Drawings'
stickers_search_path = art_folder / 'Stickers'
three_dee_search_path = art_folder / '3D'
animation_search_path = art_folder / 'Animation'

drawings_folder = art_folder_rel / 'Drawings'
stickers_folder = art_folder_rel / 'Stickers'
three_dee_folder = art_folder_rel / '3D'
animation_folder = art_folder_rel / 'Animation'



categories = [
    {'page': 'drawings', 'category' : 'drawing', 'folder_path' : drawings_folder, 'search_path' : drawings_search_path},
    {'page': 'stickers','category' : 'sticker', 'folder_path' : stickers_folder, 'search_path' : stickers_search_path},
    {'page': '3D','category' : '3D', 'folder_path' : three_dee_folder, 'search_path' : three_dee_search_path},
    {'page': 'animation','category' : 'animation', 'folder_path' : animation_folder, 'search_path' : animation_search_path}
    ]
    

def add_files(art_folder : Path, categories : list, Art, db : SQLAlchemy):
    any_added = False
    
    
    for category in categories:
        art_pieces = category['search_path'].glob('*')
        
        for art_piece in art_pieces:
            name = art_piece.stem
            
            if not Art.query.get(name):
                full_name = art_piece.name
                
                image = Image.open(art_piece)
                width, height = image.size
                aspect_ratio = round(width / height, 1)
                
                
                if aspect_ratio >= 1.4:
                    size = 'wide'
                elif aspect_ratio <= 0.7:
                    size = 'tall'
                else:
                    size = 'square'
                new_art_piece = Art(name=name, src=full_name, category=category['category'], size=size)
                db.session.add(new_art_piece)
                
                
                
                print(f"{name} - {category['category']} -- ADDED")

            else:
                pass
                #print(f"{name} - {folder['category']} - exist")
    if not any_added:
        print("no files added")

    db.session.commit()
    
def remove_files(art_folder : Path, Art, db : SQLAlchemy):
    
    art_works = [art_work.name for art_work in art_folder.rglob('*') if not art_work.is_dir()]
    
    art_works_db = Art.query.all()
    any_deleted = False
    deleted_files = []

    for art_work_db in art_works_db:
        
        if art_work_db.src not in art_works:
            deleted_files.append(art_work_db.src)
            db.session.delete(art_work_db)
            any_deleted = True
            print(f"deleted {art_work_db}")

    

    if not any_deleted:
        print("no files deleted")
        
    db.session.commit()

if __name__ == '__main__':
    add_files(art_folder, categories)
    remove_files(art_folder)



