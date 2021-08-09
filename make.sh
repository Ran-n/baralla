#! /bin/sh
# -----------------------------------
#+ Autor:	Ran#
#+ Creado:	09/08/2021 18:27:28
#+ Editado:	09/08/2021 18:41:59
# -----------------------------------

pytest --cov=src
#coverage report
coverage html
cp .coverage tests/.coverage
mv htmlcov tests/htmlcov

# -----------------------------------
