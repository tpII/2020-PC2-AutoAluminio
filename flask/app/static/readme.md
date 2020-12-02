## Integrantes

Nehuen Pereyra - 878/6

Estrada Elmer - 1259/8

Quispe Matias - 1346/5

---

## Defición de API

### Status del vehiculo

**Ruta:** `/api/vehicle/status`

**Metodo:** `GET`

**Argumentos:**

- N/A

**Ejemplo exitoso:**

```json
{
  "data": {
    "bumper_status": false,
    "datetime": "02/12/2020-18:25:38",
    "position_x": 10,
    "position_y": 10,
    "speed": 0,
    "speed_motor_1": 0,
    "speed_motor_2": 0
  }
}
```

### Historial de hasta los ultimos 15 valores

_Aclaraciones:
Muestra hasta los ultimos 15 valores guardados en la base de datos._

**Ruta:** `/api/vehicle/historical`

**Metodo:** `GET`

**Argumentos:**

- N/A

**Ejemplo exitoso:**

```json
{
  "data": [
    {
      "bumper_status": false,
      "created_at": "02/12/2020-18:29:36",
      "motor_1": 0,
      "motor_2": 0,
      "speed": 0,
      "version": 49
    },
    {
      "bumper_status": false,
      "created_at": "02/12/2020-18:29:35",
      "motor_1": 0,
      "motor_2": 0,
      "speed": 0,
      "version": 49
    },
    {
      "bumper_status": false,
      "created_at": "02/12/2020-18:29:34",
      "motor_1": 0,
      "motor_2": 0,
      "speed": 0,
      "version": 49
    }
  ]
}
```

### Historial completo

**Ruta:** `/api/vehicle/export`

**Metodo:** `GET`

**Argumentos:**

- N/A

**Ejemplo exitoso:**

```json
{
  "data": [
    {
      "bumper_status": false,
      "created_at": "02/12/2020-18:29:36",
      "motor_1": 0,
      "motor_2": 0,
      "speed": 0,
      "version": 49
    },
    {
      "bumper_status": false,
      "created_at": "02/12/2020-18:29:35",
      "motor_1": 0,
      "motor_2": 0,
      "speed": 0,
      "version": 49
    },
    {
      "bumper_status": false,
      "created_at": "02/12/2020-18:29:34",
      "motor_1": 0,
      "motor_2": 0,
      "speed": 0,
      "version": 49
    }
  ]
}
```

### Control del vehiculo

**Ruta:** `/api/vehicle/control/<int:code>`

**Metodo:** `POST`

**Argumentos:**

- `codigo*`

_Aclaraciones: El codigo representa la acción a realizar sobre el vehiculo, a continuación se ve el listado:_

- 0 es STOP.
- 1 es ARRIBA.
- 2 es ABAJO.
- 3 es DERECHA.
- 4 es IZQUIERDA.

**Codigos de error:**

- 400 Bad Request

**Ejemplo exitoso:**

Cuerpo de la respuesta

```json
{ "data": "success stop" }
```
