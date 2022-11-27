# 第一章 需求
满足用户需求的前提下构建一个稳定、易维护、易拓展的系统。

---
# 第二章 框架基础和技术选型
WSGI协议：web服务器网关接口
任何实现该协议的web框架都可以在web服务器运行程序。

---

# 第五章
拆分settings以适应不同的运行环境
在项目里新建settings包，新建base.py、develop.py，将原先settings.py的内容
复制进入base.py，将数据库等其他相关配置放进develop.py中，修改manage.py和
wsgi.py，不同的运行环境就选用不同的配置。

ORM 对象关系映射：models.py 里定义的数据模型一一对应到数据库的表上。
字段类型：数值型、字符型、日期型、关系型
参数：db_column\db_index\unique\unique_for_date\validators

QuerySet对象：django 给 Model 提供了objects属性来提供数据操作的接口，会生成一个QerySet的对象。
102--107页对QuerySet接口有详细介绍。


# 第六章
Admin中自定义字段
save_model()
自定义过滤器 SimpleListFilter ，lookups()、queryset()
get_queryset()
找到数据源的位置

在admin中 可以自定义media类，加载静态资源。

定制站点，创建新类继承AdminSite, 在需要的模块上引入站点名，修改路由。

django 第三方认证系统

# 第七章
路由规则的改变：
1.0的路由 (?P<somrthing>)
2.0以后的路由<something>

function view
class-based view: View, TemplateView, DetailView, ListView
DetailView的接口: model, queryset, template_name, get_queryset,get_object, get_context_data,

# 第八章 前端框架Bootstrap
主要讲了网页的搭建，就像堆积木一样，一块一块的堆积起来。

# 第九章 完成整个博客系统
html 中 name value value 是name 的值
新增了一个博主列表侧边栏

了解一下 GenericForeignKey

自定义标签 templatetags

统计方式：基于后段实时处理、基于后端延迟处理、通过前端埋点处理、基于日志分析处理

区分用户：根据IP 浏览器类型生成MD5标记用户、系统生成唯一ID，放入cookie中、用户登陆

# 第十章 第三方插件

后台管理框架 simpleui

性能优化 django-autocomplete-light, 配置方式,处理数据,添加路由,添加form字段


# 第十一章 django-rest-framework

RESTful API: 把请求的实体当作资源,通过HTTP自带的方法(GET, POST, PUT, DELETE)进行
增删改查的操作.

ListCreateAPIView、RetrieveAPIView、viewsets

报错：'AutoSchema' object has no attribute 'get_link'
coreapi 被弃用了

另外使用 pip install -U drf-yasg
网址： https://github.com/axnsan12/drf-yasg#quickstart

分页方式： LimitOffsetPagination、PageNumberPagination、CursorPagination

# 第十二章 调试和优化
debug_toolbar 和 silk 以及 pdb大法

# 第十三章  mysql 和缓存
pymysql

缓存： 缓和较慢存储的高频词请求，加速慢存储的访问效率

DEBUG = False 后， 设置：
re_path('static/(?P<path>.*)', serve, {'document_root':settings.STATIC_ROOT})
STATIC_ROOT

# 第十四章 标准化打包和自动化部署

pypi-server run -p <port> /home/name/packages

setup 进行打包
使用twine 注册上传包