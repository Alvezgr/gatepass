# GatePass API

Esta es una aplicación diseñada para gestionar los distintos vehículos que ingresan o egresan de una urbanización privada. Proporciona una API REST que permite realizar operaciones CRUD (crear, leer, actualizar, eliminar) sobre los vehículos registrados.

## Características

- Registro de diferentes tipos de vehículos, a travez del model `VehicleKind` como autos, motocicletas, bicicletas, camionetas, yates, veleros, etc.
- Los datos requeridos para cada vehículo a travez del model `Vehicle` incluyen tipo, marca, modelo, color, patente, nombre de la aseguradora y fecha de vencimiento de la póliza del seguro.

## Endpoints

**Usuarios**

- **GET /users**: Obtiene la lista de todos los usuarios registrados.

- **GET /users/{id}**: Obtiene los detalles de un usuario específico según su ID.

- **GET /users/verify**: Sirve para verificar un usuario.

- **POST /users/signup**: Registra un nuevo usuario con la información proporcionada en el cuerpo de la solicitud.

- **PUT /users/{id}**: Actualiza la información de un usuario existente identificado por su ID.

- **DELETE /users/{id}**: Elimina un usuario de la base de datos según su ID.

  

**Vehículos**

- **GET /vehicles**: Obtiene la lista de todos los vehículos registrados.
- **GET /vehicles/{id}**: Obtiene los detalles de un vehículo específico según su ID.
- **POST /vehicles**: Crea un nuevo vehículo con la información proporcionada en el cuerpo de la solicitud.
- **PUT /vehicles/{id}**: Actualiza la información de un vehículo existente identificado por su ID.
- **DELETE /vehicles/{id}**: Elimina un vehículo de la base de datos según su ID.

## Formato de Datos

Todos los datos se manejan en formato JSON tanto en las solicitudes como en las respuestas.

### Ejemplo de Datos de Vehículo

```json
{
  "kind": 1,
  "brand": "Toyota",
  "model": "Corolla",
  "color": "Negro",
  "license_plate": "ABC123",
  "insurer": "Seguros XYZ",
  "insurance_expiration": "2024-12-31"
}
```

## Tecnologías Utilizadas

- **Lenguaje de Programación**: Python 3.x
- **Framework**: Django Rest-Framework
- **Base de Datos**: PostgreSQL

## Instalación y Uso

1. Clona este repositorio `git clone https://github.com/Alvezgr/gatepass.git && cd gatepass`   

2. run `pipenv install Pipfile` o `pip install -f requiremets.txt` dependiendo de tus preferencias.

3. Crea una base de datos, por ejemplo, MariaSQL, PostgreSQL, etc...

4. Crea un archivo .env y proporciana datos como el ejemplo

   ```
   DATABASE_URL=psql://alvezgr:testime12@127.0.0.1:5432/gatepass
   SECRET_KEY=django-insecure-k_a(cr5848&ta$e9r&k4nev8xz=76twr=@iraw8(_6kqnsls6k
   DEBUG=True
   ```

   

5. Corre el siguiente comando `./manage.py migrate && ./manage.py runserver`

6. Accede a la documentación de la API en tu path /docs/ e.g: `localhost:8000/docs/`