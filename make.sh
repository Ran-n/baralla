#! /bin/sh
# -----------------------------------
#+ Autor:	Ran#
#+ Creado:	09/08/2021 18:27:28
#+ Editado:	09/08/2021 18:58:51
# -----------------------------------

pytest --cov=src
#coverage report
coverage html
cp .coverage tests/.coverage
mkdir -p tests/htmlcov
mv htmlcov/* tests/htmlcov/.
rm -rf htmlcov

# -----------------------------------
