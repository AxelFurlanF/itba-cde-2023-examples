Esta carpeta posee el módulo "mymodule". Un módulo básico con una función que se llama `hello()`.

Para instalar el módulo, dirigirse al path de este archivo en la terminal, y correr:
```shell
pip install .
```

Para instalar los extras, tenes que:
```shell
pip install .[dev]
```

Para usar la función, importarla y llamarla como lo siguiente:

```python
from mymodule import somefunctions as f
f.hello()
```

Para ejecutar los tests:
```shell
python -m pytests tests/*
```
