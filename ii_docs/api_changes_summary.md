# Сводка изменений в API

Сравнение старой версии (`api-merged.yaml`) с новой (`combined (3).yaml`).

## Эндпоинты (Маршруты)

### 🟢 Добавлены новые эндпоинты:
- **DELETE /rvc/{rvcId}/fiscaldb/barcodes/{objnum}/{barcode}** - Удалить штрихкод
- **DELETE /rvc/{rvcId}/fiscaldb/marks/{code}** - Удалить марку
- **GET /rvc/{rvcId}/fiscaldb/barcodes/{objnum}** - Получить штрихкоды позиции меню
- **GET /rvc/{rvcId}/fiscaldb/health** - Проверка работоспособности FiscalDB сервиса
- **GET /rvc/{rvcId}/fiscaldb/marks/byobjnum/{objnum}** - Получить марки для позиции меню
- **GET /rvc/{rvcId}/fiscaldb/marks/sold** - Выгрузка марок из проданных чеков
- **GET /rvc/{rvcId}/fiscaldb/marks/{code}** - Получить марку по коду
- **GET /rvc/{rvcId}/fiscaldb/menuitems** - Получить все позиции меню RVC
- **GET /rvc/{rvcId}/fiscaldb/menuitems/{objnum}** - Получить позицию меню по objnum
- **POST /rvc/{rvcId}/fiscaldb/barcodes** - Добавить штрихкод
- **POST /rvc/{rvcId}/fiscaldb/barcodes/batch** - Пакетное добавление штрихкодов
- **POST /rvc/{rvcId}/fiscaldb/marks** - Добавить марку ЕГАИС
- **POST /rvc/{rvcId}/fiscaldb/marks/batch** - Пакетное добавление марок
- **PUT /rvc/{rvcId}/fiscaldb/menuitems/egais** - Обновить ЕГАИС-данные позиции меню
- **PUT /rvc/{rvcId}/fiscaldb/menuitems/egais/batch** - Пакетное обновление ЕГАИС-данных

### 🔴 Удалены эндпоинты:
- **DELETE /rvc/{rvcId}/egais/barcodes/{objnum}/{barcode}**
- **DELETE /rvc/{rvcId}/egais/marks/{code}**
- **GET /rvc/{rvcId}/egais/barcodes/{objnum}**
- **GET /rvc/{rvcId}/egais/health**
- **GET /rvc/{rvcId}/egais/marks/byobjnum/{objnum}**
- **GET /rvc/{rvcId}/egais/marks/{code}**
- **GET /rvc/{rvcId}/egais/menuitems**
- **GET /rvc/{rvcId}/egais/menuitems/{objnum}**
- **POST /rvc/{rvcId}/egais/barcodes**
- **POST /rvc/{rvcId}/egais/barcodes/batch**
- **POST /rvc/{rvcId}/egais/marks**
- **POST /rvc/{rvcId}/egais/marks/batch**
- **PUT /rvc/{rvcId}/egais/menuitems/egais**
- **PUT /rvc/{rvcId}/egais/menuitems/egais/batch**

### 🟡 Изменены эндпоинты (параметры/описание):
- **DELETE /admin/cache**
- **DELETE /admin/cache/family-groups**
- **DELETE /admin/cache/major-groups**
- **DELETE /admin/cache/menu-items**
- **DELETE /admin/cache/report-groups**
- **DELETE /admin/cache/rvc-hierarchy**
- **DELETE /admin/cache/screen-lookups**
- **DELETE /admin/cache/stats/reset**
- **DELETE /menu-item/{stringNumberId}**
- **GET /admin/cache/stats**
- **GET /checks/check**
- **GET /checks/check-details**
- **GET /menu-item/{stringNumberId}/master-data**
- **GET /referencedata/family-groups**
- **GET /referencedata/major-groups**
- **GET /referencedata/report-groups**
- **GET /referencedata/rvc-hierarchy**
- **GET /referencedata/screenlookups**
- **GET /rvc/menu-items**
- **GET /tables/list**
- **GET /tables/tablesclass**
- **PATCH /menu-item**
- **PATCH /menu-item/{stringNumberId}/reprice**
- **PATCH /menu-items**
- **POST /admin/cache/config**
- **PUT /menu-item**
- **PUT /menu-items**

## Схемы данных (Models/Schemas)

### 🟢 Добавлены новые схемы:
- `FiscalDBSoldMark`
- `FiscalDbAddBarcodeDto`
- `FiscalDbAddMarkDto`
- `FiscalDbApiResponse`
- `FiscalDbBatchApiResponse`
- `FiscalDbHealthResponse`
- `FiscalDbMark`
- `FiscalDbMenuItemResponse`
- `UpdateMenuItemFiscalDbDto`

### 🔴 Удалены схемы:
- `AddBarcodeDto`
- `AddMarkDto`
- `CacheConfigRequest`
- `CacheInfo`
- `DiningTableItem`
- `DiningTableListResponse`
- `EgaisApiResponse`
- `EgaisBatchApiResponse`
- `EgaisHealthResponse`
- `EgaisMark`
- `EgaisMenuItemResponse`
- `MenuItemClass`
- `RvcMenuData`
- `UpdateMenuItemEgaisDto`


Глобальный рефакторинг: Переход от egais к fiscaldb
Самое значимое изменение — полная замена терминологии и путей, связанных с ЕГАИС, на FiscalDB:

Удалены все 14 эндпоинтов по пути /rvc/{rvcId}/egais/*.
Добавлены 15 новых эндпоинтов по пути /rvc/{rvcId}/fiscaldb/* с аналогичным функционалом (работа с марками, штрихкодами, позициями меню и проверка статуса сервиса), а также новый эндпоинт GET /rvc/{rvcId}/fiscaldb/marks/sold для выгрузки марок из проданных чеков.
📦 Изменения в схемах данных (Models/Schemas)
Схемы данных были переименованы в соответствии с изменениями путей:

Удалены: EgaisApiResponse, EgaisBatchApiResponse, EgaisHealthResponse, EgaisMark, EgaisMenuItemResponse, UpdateMenuItemEgaisDto, AddBarcodeDto, AddMarkDto и другие.
Добавлены: FiscalDbApiResponse, FiscalDbBatchApiResponse, FiscalDbHealthResponse, FiscalDbMark, FiscalDbMenuItemResponse, UpdateMenuItemFiscalDbDto, FiscalDbAddBarcodeDto, FiscalDbAddMarkDto, а также новая схема FiscalDBSoldMark.
Помимо этого, были удалены несколько устаревших схем, таких как CacheConfigRequest, CacheInfo, DiningTableItem, MenuItemClass и RvcMenuData.

🟡 Изменения существующих эндпоинтов
У 28 эндпоинтов изменились параметры, описания или структуры ответов/запросов. Среди них:

Эндпоинты управления кэшем (/admin/cache/*)
Эндпоинты работы с позициями меню (/menu-item, /menu-item/{stringNumberId}*, /menu-items)
Эндпоинты справочников (/referencedata/*)
Эндпоинты работы с чеками (/checks/check, /checks/check-details)
Эндпоинты столов (/tables/list, /tables/tablesclass)