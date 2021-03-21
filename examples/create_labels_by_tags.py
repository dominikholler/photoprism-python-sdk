#!/usr/bin/env python3
import photoprism

# api = photoprism.Client()
api = photoprism.Client(
    domain='http://phototest:2342',
    username='admin',
    password='123456',
    debug=False
)


for photo in api.get_photos():
    info = api.get_photo(photo['UID'])
    subject = info['Details']['Subject']
    if len(subject):
        for tag in subject.split(', '):
            api.add_label_to_photo(
                photo_uid=photo['UID'],
                label_name=tag
            )
