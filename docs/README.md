# 这里是API接口的开发文档

# config.py

* 文件内的`Config`类的`database`属性数据库类型, 已经支持了 `SQLite` `MySQL`
* 使用sqlite, 直接填写为`sqlite3` 即默认
* 使用mysql, 需要按照以下格式填写: user:pwd@host:port/db

# 使用

* 访问`http://127.0.0.1:8000/<any name you want>`

> 示例: http://127.0.0.1:8000/_redirect?length=10&theme=moebooru

## 参数

* `length`

> length:  1 ≤ x ≤ 10

* `theme`

> theme: `blacked` `lewd` `lisu` `moebooru` `asoul`

# 单元测试

* 没有单元测试(没写)

# 接口

> 所有接口前缀都为`/api/`
> 返回类型除了 `export` 都是RESTFul风格的api

* 部分数据可能不同

## query

* 参数: `name`

```bash
$ curl -X GET 'http://127.0.0.1/api/query/test'
```

### 返回数据

```json
{
  "code": 200,
  "time": 1668163249.493199,
  "data": {
    "name": "test",
    "times": 26
  }
}
```

## query-all

* 参数: 无

```bash
$ curl -X GET 'http://127.0.0.1/api/query-all/'
```

### 返回数据

```json
{
  "code": 200,
  "time": 1668163318.0312304,
  "data": [
    {
      "name": "dasd",
      "times": 26
    }
  ]
}
```

## query-theme

* 参数: `name`

```bash
$ curl -X GET 'http://127.0.0.1/api/query-theme/lewd'
```

* ***注:返回的base64文本开头没有添加`data:image/gif;base64,`清手动添加***

### 返回数据

* 省略了部分数据

```json
{
  "code": 200,
  "time": 1668163380.9702282,
  "data": [
    {
      "index": 0,
      "image": "...",
      "width": 68,
      "height": 150
    },
    {
      "index": 1,
      "image": "...",
      "width": 68,
      "height": 150
    }
  ]
}
```

### export

* 参数: 无

```bash
$ curl -X GET 'http://127.0.0.1/api/export/'
```

> 此接口返回文件
