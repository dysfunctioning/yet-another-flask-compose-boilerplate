# yet-another-flask-compose-boilerplate

Gets all the backbones built so you can get to building fully-featured python projects faster

## Requirements

* Docker: https://www.docker.com/
* PostgreSQL
* `uv` (`brew install uv`)

## Basics:

Check the Dockerfile & compose file to get started. The `Makefile` has some helpful commands to get you up and running faster

## FAQ

**Q: OK, but why?**

**A:** Flask, SQlAlchemy, and Docker are powerful technologies, but getting them all configured to work properly takes time. Adding compose adds another layer of complexity. Use this project to save time and get to building good things quickly.

**Q: Why uv over pyenv/pip/poetry?**

**A**: After numerous benchmark testings, `uv` packaging is blazing fast (due to its Rust build over traditional python) and quite easy to use in both new and existing projects

**Q: Why Flask?**

**A** While not as "API-Forward" as FastAPI or Flask's little brother Quart, Flask offers some flexibility to extend custom ORM's and customize your architecture for your needs.

**Q: Why not use Flask-SQLAlchemy for a more library-supported implementation?**

**A**: Good question! While Flask-SQLAlchemy would allow you to get off the ground quicker, SQLAlchemy has trended toward the more pythonic Declarative Base which makes everything more explicit. Also, its less tech debt to upgrade these libraries individually. Suppose you wanted to move off of Flask and onto Django, FastAPI or some of the other tremendous python frameworks: this allows you to rip out Flask easier ;)

## Instructions:


### Working in the environment locally:

`IPython` (interactive python) was added to this project for convenience - enter the `main` container with:

`docker exec -it compose_flask_boilerplate bash`

Then open a shell with `ipython` (TODO: add a command with initializers to have DB ready)



### Adding a dependency:

Don't ever touch the `uv.lock` file directly.  Head on over to the Makefile and call `make uv-update` to automatically update your Docker containers to have your new dependency

### Updating the database:

I use Alembic to manage database migrations as its built by the SQLAlchemy team, but you may opt to replace this with Atlas in the future.  Some helpful alembic commands:

```
alembic init alembic  # generates README env.py script.py.mako and versions folder (already done for this repo)
```

Autogenerate a migration - this project is built for `autogenerate` and may require some extra config for regular revisioning:
```
alembic revision --autogenerate -m "initial-migration"
```

Here, we are using `autogenerate` to automatically pick up what changes to make to the database based on a change SQLAlchemy's DeclarativeBase.  Its generally easier this way, though there are some exceptions (for example, post-Python 3.11 `Enum` handling). In any case, you may want to check the migration file and ensure it looks okay before migrating.


#### Making a change to the database:
* Create a new model (make sure to update `__init__py` so the Metadata picks up on this) or update the model in ~/backend/db/models/
* Run the following command to generate the next migration:
```
alembic revision --autogenerate -m "add-user-my-column"
```
* Migrate the DB with either `head` or the latest `revision_identifier`:
```
alembic upgrade head
```


### DB Troubleshooting:

The first migration can be messy with alembic, so if you run into any issues, the auto-created alembic_version table has to be dropped. To fix this - enter the postgres container:

```
docker ps
docker exec -it compose_flask_boilerplate_postgres bash
psql -U root -d compose_flask_boilerplate

DROP TABLE IF EXISTS alembic_version;
```

List databases:
```
psql -U root -d postgres
SELECT datname from pg_catalog.pg_database
```

TIP: `SELECT * from public.user;` can be used in the DB as a sanity check
