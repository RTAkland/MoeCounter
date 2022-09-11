# py 版访问次数计数器

> 翻自 [journey-ad](https://github.com/journey-ad/Moe-counter) 的计数器

# 预览

<img src="https://counter-main.run.goorm.io/test" alt="preview">

# 新特性

* 使用了异步Web框架`FastAPI`来提高效率 ***注:数据库部分使用了同步***
* 可以自定义显示图片的数量(长度)
* 支持API接口以便自行开发
* 支持MySQL数据库链接
> data.sql https://pac.rtst.tech/schema/counter/data.sql  
> image.sql  https://pac.rtst.tech/schema/counter/image.sql

# 失去的特性

* 不支持MongoDB

# 安装&运行

```bash
$ pip3 install -r requirements.txt
$ uvicorn src:create_app --factory  or 
$ python3 main.py  # 两条命令等价
```

# 使用

* 访问`127.0.0.1:8000/<any name you want>`

## 参数
* `length`
* `theme`

# 单元测试

* 没有单元测试(没写)

# 开源

- 本项目以[Apache-2.0](./LICENSE)许可开源, 即:
    - 你可以直接使用该项目提供的功能, 无需任何授权
    - 你可以在**注明来源版权信息**的情况下对源代码进行任意分发和修改以及衍生