# GatePass API

Esta es una aplicación diseñada para gestionar vecindarios, puertas de accesos y vehículos que ingresan o egresan de una urbanización privada. 
Proporciona una API REST que permite realizar operaciones CRUD (crear, leer, actualizar, eliminar) sobre los vehículos registrados, vecindarios y puertas de acceso de vecindarios. Permite crear pases y alertas sobre pólizas vencidas o vehículos que ya ingresaron o egresaron intentando repetir la misma acción.

## Características

- Registro de urbanizaciones privadas a través del model `Neighborhood`y puertas de accesos a través del model `Gates`
- Registro de diferentes tipos de vehículos, a través del model `VehicleKind` como autos, motocicletas, bicicletas, camionetas, yates, veleros, etc.
- Los datos requeridos para cada vehículo a través del model `Vehicle` incluyen tipo, marca, modelo, color, patente, nombre de la aseguradora y fecha de vencimiento de la póliza del seguro.
- Permite sumarizar los vehículos por algún atributo como ser: Color, modelo, marca, etc...
- Permite crear pases de vehículos a traves del model `Pass`
- Emite alertas según el tipo de acción o si la póliza del vehículo expiró.

## Endpoints

**Usuarios**

- **GET /users**: Obtiene la lista de todos los usuarios registrados.

- **GET /users/{id}**: Obtiene los detalles de un usuario específico según su ID.

- **GET /users/verify**: Sirve para verificar un usuario.

- **POST /users/signup**: Registra un nuevo usuario con la información proporcionada en el cuerpo de la solicitud.

- **PUT /users/{id}**: Actualiza la información de un usuario existente identificado por su ID.

- **DELETE /users/{id}**: Elimina un usuario de la base de datos según su ID.


**Vecindarios**

- **GET /neighborhoods**: Obtiene la lista de todos los vecindarios registrados.

- **GET /neighborhoods/{id}**: Obtiene los detalles de un vehículo específico según su ID.

- **POST /neighborhoods**: Crea un nuevo vehículo con la información proporcionada en el cuerpo de la solicitud.

- **PUT /neighborhoods/{id}**: Actualiza la información de un vehículo existente identificado por su ID.

- **DELETE /neighborhoods/{id}**: Elimina un vehículo de la base de datos según su ID.

**Puertas de accesos**

- **GET /gates**: Obtiene la lista de todos las puertas de accesos.

- **GET /gates/{id}**: Obtiene los detalles de un puertas de acceso específico según su ID.

- **POST /gates**: Crea un nuevo puertas de acceso con la información proporcionada en el cuerpo de la solicitud.

- **PUT /gates/{id}**: Actualiza la información de un puertas de acceso existente identificado por su ID.

- **DELETE /gates/{id}**: Elimina un puertas de acceso de la base de datos según su ID.

**Vehículos**

- **GET /vehicles**: Obtiene la lista de todos los vehículos registrados.
- **GET /vehicles/{id}**: Obtiene los detalles de un vehículo específico según su ID.

- **GET /vehicles/summarize**: Permite contar vehículos por un determinado atributo.

- **POST /vehicles**: Crea un nuevo vehículo con la información proporcionada en el cuerpo de la solicitud.

- **PUT /vehicles/{id}**: Actualiza la información de un vehículo existente identificado por su ID.

- **DELETE /vehicles/{id}**: Elimina un vehículo de la base de datos según su ID.

**Passes**

- **GET /passes**: Obtiene la lista de todos los pases registrados.
- **GET /passes/{id}**: Obtiene los detalles de un pase específico según su ID.

- **POST /passes**: Crea un nuevo pase con la información proporcionada en el cuerpo de la solicitud.

- **PUT /passes/{id}**: Actualiza la información de un pase existente identificado por su ID.

- **DELETE /passes/{id}**: Elimina un pase de la base de datos según su ID.

**Alertas**

- **GET /alerts**: Obtiene la lista de todos las alertas registradas.
- **GET /alerts/{id}**: Obtiene los detalles de una alerta específica según su ID.


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
   DATABASE_URL=psql://{{user}}:{{db_user}}@127.0.0.1:5432/{{db_name}}
   SECRET_KEY=django-insecure-k_a(cr5848&ta$e9r&k4nev8xz=76twr=@iraw8(_6kqnsls6k
   DEBUG=True
   ```

   

5. Corre el siguiente comando `./manage.py migrate && ./manage.py runserver`

6. Accede a la documentación de la API en tu path /docs/ e.g: `localhost:8000/docs/`
