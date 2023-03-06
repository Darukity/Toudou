# Toudou

The best todo application!


## Installing

```bash
$ pip install -U toudou
```

## Usage

```bash
$ toudou
Usage: toudou [OPTIONS] COMMAND [ARGS]...

Options:
    --help  Show this message and exit.

Commands:
    create
    get
    get-all
    import-csv
    init-db
    update
```


## Contributing

Start coding using an editable project with:

```bash
$ python3 -m venv venv
$ source ./venv/bin/activate
(venv) $ pip install -e .
(venv) $ toudou
```

Or with PDM:

```bash
$ pdm install
$ pdm run toudou
```

Pour utiliser toudou en cli j'ai utilisé venv
Le projet est organisé en sous-dossiers (plus lisible)
Le fichier de la base de donnée est dans src/toudou/database, vous devez faire toudou init-db en cli pour l'initialiser si il n'est pas présent.
Les commandes click sont définies dans le fichier __init__.py dans src/toudou/views
L'app flask s'apelle webview.py et se situe dans le dossier src/toudou/views.
Pour lancer le serveur flask j'ai utilisé la commande :
python -m pdm run flask --app toudou.views.webview run

Pour importer des todo via un fichier csv il faut faire :
toudou tmport-csv (path absolue du fichier csv)
Les output csv sont dans le fichier src/toudou/csv
