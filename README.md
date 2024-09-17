# instruccion para python anywhere

Lo primero que hay que hacer en la terminal es: 

https://lukecolman.pythonanywhere.com


```sh

pip install --user pythonanywhere
 https://github.com/LucasColmanLener/my-first-blog.git

```


# Instrucciones para tu compu (ambiente local) dev environment


1. Primero crear el virtualenv: `python -m venv myvirtualenv`
2. Activar el virtualenv: `source myvirtualenv/bin/activate`
3. instalar dependencias: `pip install -r requirements.txt`
4. Crear superuser: `python manage.py createsuperuser`

Para ejecutar tu servidor local de desarrollo

```sh
python manage.py runserver
```

127.0.0.1 == localhost => Esto es una ip que refiere a tu propia maquina, y lo segundo es un dominio a tu propia maquina.

:8000 => puerto 8000

http://localhost:8000/
http://127.0.0.1:8000/