# NSW Water Dashboard — API Reference

Base URL: `http://localhost:5001/api`
Production base URL will vary — check your environment config.

All endpoints are **GET only**. POST, PUT, DELETE return `405 Method Not Allowed`.
Swagger docs are available at `{base_url}/api/docs`.

---

## Error Responses

**404 Not Found**
```json
{
    "message": "...",
    "status": 404
}
```

**400 Bad Request** — returned when a date path parameter is not valid `YYYY-MM-DD`.

---

## Endpoints

### `GET /api/`
Welcome message. No parameters.

**Response**
```json
{
    "message": "Welcome to the Dam Management API!"
}
```

---

### `GET /api/dams`
List all dams.

**Response** — array of dam objects:
```json
[
    {
        "dam_id": "203042",
        "dam_name": "Toonumbar Dam",
        "full_volume": 10814,
        "latitude": -28.602383,
        "longitude": 152.763769
    }
]
```

| Field | Type | Notes |
|---|---|---|
| `dam_id` | string | Primary key, 6-digit code |
| `dam_name` | string | Human-readable name |
| `full_volume` | integer | Full capacity in megalitres |
| `latitude` | float | Nullable |
| `longitude` | float | Nullable |

---

### `GET /api/dams/<dam_id>`
Get a single dam by ID. Returns 404 if not found.

**Response** — single dam object (same shape as above).

---

### `GET /api/latest_data`
Most recent storage snapshot for every dam.

**Response** — array:
```json
[
    {
        "dam_id": "203042",
        "dam_name": "Toonumbar Dam",
        "date": "2026-02-01",
        "storage_volume": 10979.0,
        "percentage_full": 101.53,
        "storage_inflow": 92.0,
        "storage_release": 66.0
    }
]
```

| Field | Type | Notes |
|---|---|---|
| `dam_id` | string | FK to dams |
| `dam_name` | string | |
| `date` | string | ISO date `YYYY-MM-DD` |
| `storage_volume` | float | Megalitres, nullable |
| `percentage_full` | float | Can exceed 100 when dam is over capacity, nullable |
| `storage_inflow` | float | Megalitres, nullable. Can be negative in source data |
| `storage_release` | float | Megalitres, nullable |

---

### `GET /api/latest_data/<dam_id>`
Latest data for a single dam. Returns 404 if not found.

**Response** — single object (same shape as above).

---

### `GET /api/dam_resources`
Full historical time-series data across all dams.

**Response** — array:
```json
[
    {
        "resource_id": 1,
        "dam_id": "203042",
        "date": "2026-02-01",
        "storage_volume": 10979.0,
        "percentage_full": 101.53,
        "storage_inflow": 92.0,
        "storage_release": 66.0
    }
]
```

| Field | Type | Notes |
|---|---|---|
| `resource_id` | integer | Auto-increment PK |
| `dam_id` | string | FK to dams |
| `date` | string | ISO date `YYYY-MM-DD` |
| `storage_volume` | float | Nullable |
| `percentage_full` | float | Nullable |
| `storage_inflow` | float | Nullable |
| `storage_release` | float | Nullable |

---

### `GET /api/dam_resources/<resource_id>`
Single historical record by its auto-increment ID. Returns 404 if not found.

**Response** — single object (same shape as above).

---

### `GET /api/specific_dam_analysis`
Per-dam rolling averages (12-month, 5-year, 10-year) for storage, inflow, and release.

**Response** — array:
```json
[
    {
        "dam_id": "203042",
        "analysis_date": "2026-01-31",
        "avg_storage_volume_12_months": 10961.077,
        "avg_storage_volume_5_years": 10823.117,
        "avg_storage_volume_10_years": 9934.992,
        "avg_percentage_full_12_months": 101.36,
        "avg_percentage_full_5_years": 100.08,
        "avg_percentage_full_10_years": 91.87,
        "avg_storage_inflow_12_months": 6772.385,
        "avg_storage_inflow_5_years": 5514.451,
        "avg_storage_inflow_10_years": 3668.905,
        "avg_storage_release_12_months": 6778.985,
        "avg_storage_release_5_years": 5555.156,
        "avg_storage_release_10_years": 3549.407
    }
]
```

| Field | Type | Notes |
|---|---|---|
| `dam_id` | string | Part of composite PK |
| `analysis_date` | string | Part of composite PK, ISO date |
| `avg_storage_volume_12_months` | float | Nullable |
| `avg_storage_volume_5_years` | float | Nullable |
| `avg_storage_volume_10_years` | float | Nullable |
| `avg_percentage_full_12_months` | float | Nullable |
| `avg_percentage_full_5_years` | float | Nullable |
| `avg_percentage_full_10_years` | float | Nullable |
| `avg_storage_inflow_12_months` | float | Nullable |
| `avg_storage_inflow_5_years` | float | Nullable |
| `avg_storage_inflow_10_years` | float | Nullable |
| `avg_storage_release_12_months` | float | Nullable |
| `avg_storage_release_5_years` | float | Nullable |
| `avg_storage_release_10_years` | float | Nullable |

---

### `GET /api/specific_dam_analysis/<dam_id>`
All analysis records for a single dam. Returns 404 if no records exist for that dam.

**Response** — array of analysis objects (same shape as above).

---

### `GET /api/specific_dam_analysis/<dam_id>/<analysis_date>`
Single analysis record by composite key. `analysis_date` must be `YYYY-MM-DD` (returns 400 if malformed, 404 if not found).

**Response** — single analysis object (same shape as above).

---

### `GET /api/overall_dam_analysis`
System-wide rolling averages aggregated across all dams.

**Response** — array:
```json
[
    {
        "analysis_date": "2026-01-31",
        "avg_storage_volume_12_months": 285899.164,
        "avg_storage_volume_5_years": 361587.357,
        "avg_storage_volume_10_years": 293878.021,
        "avg_percentage_full_12_months": 79.99,
        "avg_percentage_full_5_years": 86.28,
        "avg_percentage_full_10_years": 72.75,
        "avg_storage_inflow_12_months": 10787.147,
        "avg_storage_inflow_5_years": 17989.072,
        "avg_storage_inflow_10_years": 13856.297,
        "avg_storage_release_12_months": 10300.151,
        "avg_storage_release_5_years": 17650.067,
        "avg_storage_release_10_years": 13271.383
    }
]
```

Same field set as `specific_dam_analysis`, minus `dam_id`.

---

### `GET /api/overall_dam_analysis/<analysis_date>`
Single overall analysis by date. `analysis_date` must be `YYYY-MM-DD` (returns 400 if malformed, 404 if not found).

**Response** — single object (same shape as above).

---

### `GET /api/dam_groups`
List all dam groups.

**Response** — array:
```json
[
    { "group_name": "sydney_dams" },
    { "group_name": "large_dams" },
    { "group_name": "small_dams" },
    { "group_name": "popular_dams" },
    { "group_name": "greatest_released" }
]
```

| Field | Type | Notes |
|---|---|---|
| `group_name` | string | Primary key |

---

### `GET /api/dam_groups/<group_name>`
Single group by name. Returns 404 if not found.

**Response** — single object (same shape as above).

---

### `GET /api/dam_group_members`
All dam-to-group associations.

**Response** — array:
```json
[
    {
        "group_name": "small_dams",
        "dam_id": "203042"
    }
]
```

| Field | Type | Notes |
|---|---|---|
| `group_name` | string | FK to dam_groups |
| `dam_id` | string | FK to dams |

A single dam can belong to multiple groups, and a group can contain multiple dams.

---

### `GET /api/dam_group_members/<group_name>`
All members of a specific group. Returns 404 if no members found.

**Response** — array of member objects (same shape as above).

---

## Known Data Notes

- `percentage_full` can exceed 100 — this represents dams operating above rated capacity and is present in the source data.
- `storage_inflow` can be negative for some dams in certain months (observed in Glenbawn and Glennies Creek). Treat as net flow if displaying.
- Some dams (e.g. Nepean, Avon, Warragamba) consistently report `0.0` for both inflow and release — flow data may not be collected for these.
- Current groups in the database: `sydney_dams`, `large_dams`, `small_dams`, `popular_dams`, `greatest_released`.
