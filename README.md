## Questions and Answers

## Iniciar con Docker
Clonar el proyecto

```
git clone https://github.com/luisca1985/questions_and_answers.git
```

Ingresar a la carpeta del proyecto

```
cd questions_and_answers
```

## Crear el proyecto con Docker y Docker Compose
Crear el proyecto

```
docker-compose up --build -d
```
## Testing
Para correr los test utilizar:
```
docker-compose run --rm server pytest
```