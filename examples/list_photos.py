#!/usr/bin/env python3
import photoprism
import timeit

# api = photoprism.Client()
api = photoprism.Client(
    domain='https://xxx.datadrop.org',
    username='admin',
    password='xxx',
    debug=False
)

iterations = 10


def list_photos():
    offset = 0
    count = 60
    empty = False

    for i in range(iterations):
        photos = api.get_photos(
            count=count,
            offset=offset,
            merged='true',
            camera=0,
            lens=0,
            year=0,
            month=0,
            order='added',  # 0.5738903962999757
            # order='newest',  # 2.7784242087996973
            public='true',
            quality=3
        )
        count = len(photos)
        empty = count == 0
        offset = offset + count


time = timeit.timeit(stmt=list_photos, number=1)
print(time/iterations)