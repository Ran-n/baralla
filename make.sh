#! /bin/sh
# -----------------------------------
#+ Autor:	Ran#
#+ Creado:	09/08/2021 18:27:28
#+ Editado:	09/08/2021 19:55:08
# -----------------------------------

#pytest --cov=src --cov-report=html
pytest --cov=src
coverage html
#coverage report
cp .coverage tests/.coverage
mkdir -p tests/htmlcov
mv htmlcov/* tests/htmlcov/.
rm -rf htmlcov

# -----------------------------------
