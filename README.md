# Ibis: steps to reproduce timestamp issue

Please run below commands

```bash
docker compose up -d

poetry install

poetry run python runme.py

```

Error log

```
Traceback (most recent call last):
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/sqlalchemy/engine/base.py", line 1900, in _execute_context
    self.dialect.do_execute(
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/trino/sqlalchemy/dialect.py", line 365, in do_execute
    cursor.execute(statement, parameters)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/trino/dbapi.py", line 439, in execute
    result = self._query.execute()
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/trino/client.py", line 765, in execute
    self._result.rows += self.fetch()
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/trino/client.py", line 780, in fetch
    status = self._request.process(response)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/trino/client.py", line 581, in process
    raise self._process_error(response["error"], response.get("id"))
trino.exceptions.TrinoUserError: TrinoUserError(type=USER_ERROR, name=NOT_SUPPORTED, message="Timestamp precision (3) not supported for Iceberg. Use "timestamp(6)" instead.", query_id=20230105_111531_00005_593ik)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/arun/Documents/python/ibis_issue/runme.py", line 23, in <module>
    connection.create_table("iceberg_table", schema=first)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/src/ibis/ibis/backends/base/sql/alchemy/__init__.py", line 218, in create_table
    table.create(bind=bind, checkfirst=force)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/sqlalchemy/sql/schema.py", line 962, in create
    bind._run_ddl_visitor(ddl.SchemaGenerator, self, checkfirst=checkfirst)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/sqlalchemy/engine/base.py", line 2211, in _run_ddl_visitor
    visitorcallable(self.dialect, self, **kwargs).traverse_single(element)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/sqlalchemy/sql/visitors.py", line 524, in traverse_single
    return meth(obj, **kw)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/sqlalchemy/sql/ddl.py", line 895, in visit_table
    self.connection.execute(
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/sqlalchemy/engine/base.py", line 1380, in execute
    return meth(self, multiparams, params, _EMPTY_EXECUTION_OPTS)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/sqlalchemy/sql/ddl.py", line 80, in _execute_on_connection
    return connection._execute_ddl(
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/sqlalchemy/engine/base.py", line 1472, in _execute_ddl
    ret = self._execute_context(
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/sqlalchemy/engine/base.py", line 1943, in _execute_context
    self._handle_dbapi_exception(
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/sqlalchemy/engine/base.py", line 2124, in _handle_dbapi_exception
    util.raise_(
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/sqlalchemy/util/compat.py", line 211, in raise_
    raise exception
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/sqlalchemy/engine/base.py", line 1900, in _execute_context
    self.dialect.do_execute(
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/trino/sqlalchemy/dialect.py", line 365, in do_execute
    cursor.execute(statement, parameters)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/trino/dbapi.py", line 439, in execute
    result = self._query.execute()
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/trino/client.py", line 765, in execute
    self._result.rows += self.fetch()
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/trino/client.py", line 780, in fetch
    status = self._request.process(response)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/trino/client.py", line 581, in process
    raise self._process_error(response["error"], response.get("id"))
sqlalchemy.exc.ProgrammingError: (trino.exceptions.TrinoUserError) TrinoUserError(type=USER_ERROR, name=NOT_SUPPORTED, message="Timestamp precision (3) not supported for Iceberg. Use "timestamp(6)" instead.", query_id=20230105_111531_00005_593ik)
[SQL: 
CREATE TABLE iceberg_table (
        a TIMESTAMP
)

]
(Background on this error at: https://sqlalche.me/e/14/f405) 
```

Now change timestamp [here](https://github.com/arun-k-bharathan/ibis_issue/blob/main/runme.py#L22) to timestamp(6) in [runme.py](https://github.com/arun-k-bharathan/ibis_issue/blob/main/runme.py)

then run
```bash
poetry run python runme.py
```

Error log
```
Traceback (most recent call last):
  File "/home/arun/Documents/python/ibis_issue/runme.py", line 22, in <module>
    first = ibis.schema({"a": "timestamp(6)"})
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/src/ibis/ibis/expr/api.py", line 277, in schema
    return sch.schema(pairs)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/multipledispatch/dispatcher.py", line 278, in __call__
    return func(*args, **kwargs)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/src/ibis/ibis/expr/schema.py", line 408, in schema_from_mapping
    return Schema.from_dict(d)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/src/ibis/ibis/expr/schema.py", line 204, in from_dict
    return cls(names, types)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/src/ibis/ibis/common/grounds.py", line 23, in __call__
    return cls.__create__(*args, **kwargs)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/src/ibis/ibis/common/grounds.py", line 99, in __create__
    kwargs = cls.__signature__.validate(*args, **kwargs)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/src/ibis/ibis/common/annotations.py", line 261, in validate
    this[name] = param.validate(value, this=this)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/src/ibis/ibis/common/annotations.py", line 115, in validate
    return self.annotation(arg, this=this)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/toolz/functoolz.py", line 304, in __call__
    return self._partial(*args, **kwargs)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/src/ibis/ibis/common/validators.py", line 193, in container_of
    return type(inner(item, **kwargs) for item in arg)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/src/ibis/ibis/common/validators.py", line 193, in <genexpr>
    return type(inner(item, **kwargs) for item in arg)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/toolz/functoolz.py", line 304, in __call__
    return self._partial(*args, **kwargs)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/src/ibis/ibis/expr/schema.py", line 43, in datatype
    return dt.dtype(arg)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/multipledispatch/dispatcher.py", line 278, in __call__
    return func(*args, **kwargs)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/src/ibis/ibis/expr/datatypes/parse.py", line 249, in from_string
    return parse(value)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/src/ibis/ibis/expr/datatypes/parse.py", line 243, in parse
    return ty.parse(text)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/parsy/__init__.py", line 87, in parse
    (result, _) = (self << eof).parse_partial(stream)
  File "/home/arun/.cache/pypoetry/virtualenvs/ibis-trino-iceberg-issue-JyJ77i8h-py3.10/lib/python3.10/site-packages/parsy/__init__.py", line 101, in parse_partial
    raise ParseError(result.expected, stream, result.furthest)
parsy.ParseError: expected '(\'[^\n\'\\\\]*(?:\\\\.[^\n\'\\\\]*)*\'|"[^\n"\\\\"]*(?:\\\\.[^\n"\\\\]*)*")' at 0:10
```

If we try to cast timestamp to timestamp(6) same issue as above this will happen.