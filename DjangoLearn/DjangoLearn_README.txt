Note:
    1> create project: django-admin.py startproject   pro_name
    2> modify settings.py:
        a>  ALLOWED_HOSTS=['*']
        b>  MIDDLEWARE=[]
        c>  DATABASES=[
         /*default is necessary. When you use python manage.py inspectdb --database db1 */
            'default':{},
            'db1':{},
            'db2':{},
            ]
        d>  INSTALLED_APPS=[
                'rest_framework',
            ]
    3>  create app:  python manage.py startapp app_aname;  add app_name to INSTALLED_APPS=[]
    4>  copy url.py  to  app_name
    5>  Configure url.py of app_name
    5>  start project: python manage.py runserver 0.0.0.0:8000
    6>  http://ip:8000/admin
    7>  How to modify the name of project?
        please modify manage.py