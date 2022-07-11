# ApiChuchNorris

PASSO 1 Docker Build: 
Executar o comando para buildar a imagem 

docker image build -t api_chuck:latest .

PASSO 2 Executar o comando para iniciar a imagem no container:

docker container run -it -v ${pwd}:/usr/src/app --env-file .env -p 81:80 --name api_chuck api_chuck:latest