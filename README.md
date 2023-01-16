## beer-recognition-api API

API for serving models developed for Beer Recognition API.


## Install requirements

```bash
sudo apt update
sudo apt install python3 python3-pip nodejs -y
sudo npm install -g pm2
```

## Deploy application

Application can be launched with the launch script:

```bash
sudo bash launch.sh
```

Or using PM2:
```bash
sudo pm2 start pm2.json
```

Note: if the script `launch.sh` doesn't works, you can use `launch2.sh` instead.

### Docker deployment

Application can be also deployed with docker. For that purpose, first build and push the application:

```bash
docker build . -t iSkYrIsE/beer-recognition-api
docker push iSkYrIsE/beer-recognition-api
```

Then in the enviroment where application must be deplolyed, pull changes and deploy:

```bash
docker pull iSkYrIsE/beer-recognition-api
docker run iSkYrIsE/beer-recognition-api
```

## Run application

For running directly the application in a "raw" way:
```bash
sudo python3 -m pip install pip --upgrade
sudo python3 -m pip install . --upgrade
sudo beer_recognition_models_api
```

### Integration

For make easier the integration, the API deploys a swagger interface. Also in the repository there is a postman collection in `integration/beer-recognition-api.postman_collection.json`, which you can generate the request with for any language included in the postman client.

## Disclaimer

Component developed by Marcos Gómez de Quero Santos (@iSkYrIsE on GitHub) on 2022. For manteinance and bug reports please contact the developer at marcgomezdequero99@gmail.com.
Copyright Marcos Gómez de Quero Santos 2022. All rights reserved. See license for details.
