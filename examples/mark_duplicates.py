#!/usr/bin/env python3
import photoprism

# api = photoprism.client.Client()

api = photoprism.Client(
    domain='http://phototest:2342',    
    username='admin',
    password='123456',
    debug=False
)

offset = 0
count = 0
empty = False


by_hash = {}

# works for my scenario, might not work for other people
def hash(photo):
    return photo['Name'] + photo['TakenAt'] + str(photo['Iso']) + str(photo['FNumber']) + photo['Exposure'] + photo['CameraModel']

def Timestamp():
    return '2021-05-07 00:00:00'

# https://github.com/photoprism/photoprism/blob/ab40583c9a692730c57d4e9f5f1cd581daeed4c1/internal/entity/photo_merge.go#L92
def print_sql(original_id, original_photo_uid, merge_id, merge_photo_uid):
    print("UPDATE `files` SET photo_id = {}, photo_uid = '{}', file_primary = 0 WHERE photo_id = {} ;".format(original_id, original_photo_uid, merge_id))
    print("UPDATE `photos` SET photo_quality = -1, deleted_at = '{}' WHERE id = {} ;".format(Timestamp(), merge_id))
    print("UPDATE IGNORE `photos_keywords` SET `photo_id` = {} WHERE photo_id = {} ;".format(original_id, merge_id))
    print("UPDATE IGNORE `photos_labels` SET `photo_id` = {} WHERE photo_id = {} ;".format(original_id, merge_id))
    print("UPDATE IGNORE `photos_albums` SET `photo_uid` = '{}' WHERE photo_uid = '{}' ;".format(original_photo_uid, merge_photo_uid))


while not empty:
    photos = api.get_photos(offset=offset)
    count = len(photos)
    empty = count == 0
    offset = offset + count

    for photo in photos:
        if photo['FileRoot'] == 'sidecar':
            continue

        h = hash(photo)
        other = by_hash.get(h)
        if other:
            photo = api.get_photo(photo['UID'])
            other = api.get_photo(other['UID'])
            #for a in photo.keys():
            #    if photo.get(a) != other.get(a):
                    # print('{}: {} - {}'.format(a, photo.get(a), other.get(a)))
            print('-- {}'.format(other))
            print('-- {}'.format(photo))
            print_sql(other['ID'], other['UID'], photo['ID'], photo['UID']) 
            print('')
        else:
            by_hash[h] = photo


