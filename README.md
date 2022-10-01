# MayaProtect - Microservice GetHiveDatas

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=MayaProtect_GetHiveDatas&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=MayaProtect_GetHiveDatas) [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=MayaProtect_GetHiveDatas&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=MayaProtect_GetHiveDatas) [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=MayaProtect_GetHiveDatas&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=MayaProtect_GetHiveDatas) [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=MayaProtect_GetHiveDatas&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=MayaProtect_GetHiveDatas)

This microservice is used to get metrics datas from hive.

## How to build

### Build with docker

```bash
docker build -t mayaprotect/gethivedatas .
```

## Usage

### Environment variables
MONGO_HOST: The host of the mongo database
MONGO_PORT: The port of the mongo database
MONGO_DB: The name of the mongo database
PROMETHEUS_URL: The url of the prometheus server

### Run in environment

`python run.py`

### Run with docker

```bash
docker run -d -p 8080:8080 mayaprotect/gethivedatas
```

## Contributors
Peter Fontaine - contact@peterfontaine.fr

## Licence

```plaintext
GetHiveDatas - Microservice to get metrics datas from hive
Copyright (C) 2022 Peter Fontaine

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
```
