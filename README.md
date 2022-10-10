# bottlepy-nignx-docker-compose
A simple template for docker-compose, bottlepy, and nginx as reverse proxy

## Getting Started

1. Edit `init-letsencrypt.sh` file with your domain and email address
2. Run `sudo ./init-letsencrypt.sh` to create a dummy cert then create the real one
> Note: `init-letsencrypt.sh` will also rename `nginx/conf/example.conf` to `YOUR_DOMAIN.conf`


### Folder structure

| Folder    | Description            |
| --------- | ---------------------- |
| WWW       | For any static content |
| server    | Bottlepy application   |
| \  routes | server routes          |
| nginx     | nginx configs          |
| certbot   | Letsencrypt SSL files  |

