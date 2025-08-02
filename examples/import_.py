#!/usr/bin/env python3
import photoprism

api = photoprism.Client(
    domain='https://xxx.datadrop.org',
    username='admin',
    password='xxx',
)

api.import_()
