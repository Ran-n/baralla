#! /bin/sh
# -----------------------------------
#+ Autor:	Ran#
#+ Creado:	09/08/2021 18:27:28
#+ Editado:	09/08/2021 18:54:57
# -----------------------------------

pytest --cov=src
#coverage report
coverage html
cp .coverage tests/.coverage
mv -n htmlcov/ tests/

# -----------------------------------
