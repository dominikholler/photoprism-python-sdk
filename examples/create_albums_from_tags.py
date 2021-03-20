#!/usr/bin/env python3
import photoprism

# api = photoprism.client.Client()
api = photoprism.Client(
    domain='http://phototest:2342',
    username='admin',
    password='123456',
    debug=False
)


albums = {album['Title']: album for album in api.get_albums(type='album')}

for photo in api.get_photos():
    info = api.get_photo(photo['UID'])
    subject = info['Details']['Subject']
    if len(subject):
        for tag in subject.split(', '):
            if tag not in albums.keys():
                albums[tag] = api.create_album(tag)
            api.add_photo_to_album(
                album_uid=albums[tag]['UID'],
                photo_uid=photo['UID']
            )
