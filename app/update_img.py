from pathlib import Path
from PIL import Image

#how to import app??
from app import db
from app.models import Art
from config import basedir



art_folder = Path("app/static/Images/Art/")

drawings_folder = art_folder.joinpath('drawings')
stickers_folder = art_folder.joinpath('stickers')
three_dee_folder = art_folder.joinpath('3D')
animation_folder = art_folder.joinpath('animation')

categories = [
    {'page': 'drawings', 'category' : 'drawing', 'folder_path' : drawings_folder},
    {'page': 'stickers','category' : 'sticker', 'folder_path' : stickers_folder},
    {'page': '3D','category' : '3D', 'folder_path' : three_dee_folder},
    {'page': 'animation','category' : 'animation', 'folder_path' : animation_folder}
    ]
    

def add_files(art_folder : Path, folders : list):
    any_added = False
    for folder in folders:
        art_pieces = folder['folder_path'].glob('*')
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
                new_art_piece = Art(name=name, src=full_name, category=folder['category'], size=size)
                db.session.add(new_art_piece)
                
                
                
                print(f"{name} - {folder['category']} -- ADDED")

            else:
                pass
                #print(f"{name} - {folder['category']} - exist")
    if not any_added:
        print("no files added")

    db.session.commit()
    
def remove_files(art_folder : Path):
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



