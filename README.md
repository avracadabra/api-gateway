# Bulk management API Gateway

The API gateway takes all GraphQL API requests from a client
(frontend: mobile app, browser app..., scripting or any other services),
determines which services are needed (Warehouse Management System (WMS),
Product Information Management (PIM), ...),
and combines them into a synchronous experience for the user.

## Features

This project is based on [ASGI](https://asgi.readthedocs.io) as asynchronous
web server and [tartiflette.](https://tartiflette.io) as GraphQL engine.

## TODO

Support multiple product software provider (PIM software, ERP, OpenData...):

- openfoodfact
- akeneo
- odoo
- treopim
- icecat
