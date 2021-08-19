#!/usr/bin/env python3
import photoprism

# api = photoprism.Client()
api = photoprism.Client(
    domain='https://xx.datadrop.org',
    username='admin',
    password='xxx',
    debug=False
)


offset = 0
count = 0
empty = False

while not empty:
    photos = api.get_photos(offset=offset, private=True)
    count = len(photos)
    empty = count == 0
    offset = offset + count

    for photo in photos:
        info = api.get_photo(photo['UID'])
        for file in info['Files']:
            print('echo mv "digicam/{}" "private_Fotos/{}"'.format(
                file['Name'], file['Name']
            ))

