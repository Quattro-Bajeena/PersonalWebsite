from app import db
from app.models import Art
import os
from os import path

from pathlib import Path

from PIL import Image

art_folder = Path("app/static/Images/Art/")
drawings_folder = art_folder.joinpath('Drawings')
stickers_folder = art_folder.joinpath('Stickers')

folders = [
    {'category' : 'drawing', 'folder_path' : drawings_folder},
    {'category' : 'sticker', 'folder_path' : stickers_folder}
    ]


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
            print(f"Name: {name}, aspect ratio: {size}")
            new_art_piece = Art(name=name, src=full_name, category=folder['category'], size=size)
            db.session.add(new_art_piece)
            db.session.commit()
            
            
            print(f"{folder['category']} Added")

        else:
            print(f"{name} - This {folder['category']} is in the database already")


