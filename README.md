# Problems with Tortoise/aerich

The aerich does not upgrade the database for some reason:

```
(venv) ➜  sqlAlchemyExporiment git:(master) sqlite3 main.sqlite3

SQLite version 3.37.0 2021-12-09 01:34:53
Enter ".help" for usage hints.
sqlite> PRAGMA table_info(items);
0|id|INTEGER|1||1
1|name|TEXT|1||0
2|current_status|VARCHAR(3)|1||0
sqlite> ^D

(venv) ➜  sqlAlchemyExporiment git:(master) aerich upgrade

Success upgrade 1_20220923163900_update.py

(venv) ➜  sqlAlchemyExporiment git:(master) sqlite3 main.sqlite3

SQLite version 3.37.0 2021-12-09 01:34:53
Enter ".help" for usage hints.
sqlite> PRAGMA table_info(items);
0|id|INTEGER|1||1
1|name|TEXT|1||0
2|current_status|VARCHAR(3)|1||0

sqlite> SELECT * FROM aerich;

1|0_20220923150936_init.py|models|{"models.Item": {"name": "models.Item", "app": "models", "table": "items", //
3|1_20220923163900_update.py|models|{"models.Item": {"name": "models.Item", "app": "models", "table": "items", //
```

Migrations seem to be applied, but not reflected in the actual database state.
