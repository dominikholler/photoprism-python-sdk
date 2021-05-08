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


offset = 0
count = 0
empty = False

while not empty:
    photos = api.get_photos(offset=offset)
    count = len(photos)
    empty = count == 0
    print(f'offset: {offset}, count:{count}, empty:{empty}')
    offset = offset + count

    for photo in photos:
        info = api.get_photo(photo['UID'])
        print(info['Path'] + '/' + info['Name'])
        subject = info['Details']['Subject']
        if len(subject):
            for tag in subject.split(', '):
                if tag not in albums.keys():
                    albums[tag] = api.create_album(tag)
                api.add_photo_to_album(
                    album_uid=albums[tag]['UID'],
                    photo_uid=photo['UID']
                )

