# FastAPI con HTMX y SQLite/Postgress

Dependencias:

```sh
pip install fastapi uvicorn Jinja2
```

Dentro de la carpeta `tailwindcss` hay que hace un

```sh
npm i
```

Abrimos 2 teminales y en una ejecutaremos uvicorn y en otra tailwind

```sh
uvicorn main:app --reload
```

```sh
npx tailwind -i ./styles/app.css -o ../static/css/app.css --watch
```
