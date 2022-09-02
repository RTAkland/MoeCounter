# 这里是API接口的开发文档

> 所有接口前缀都为`/api/`
> 返回类型除了 `export` 都是JSON

# 接口

## query

* 参数: `name`

```bash
$ curl -X GET 'http://127.0.0.1/api/query/test'
```

### 返回数据

```json
{
  "test": 0
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
  "test": 114514,
  "test1": 1919810
}
```

## query-theme

* 参数: `name`

```bash
$ curl -X GET 'http://127.0.0.1/api/query-theme/lewd'
```

* ***注:返回的base64文本开头没有添加`data:image/gif;base64,`清手动添加***

### 返回数据

```json
[
  [
    "lewd/0",
    "base64...",
    45,
    100
  ],
  ...
]
```

### export

* 参数: 无

```bash
$ curl -X GET 'http://127.0.0.1/api/export/'
```

> 此接口返回文件
