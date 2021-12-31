# Remove pkg-resources==0.0.0 from pip freeze output
# According to https://github.com/pypa/pip/issues/4022, this is a bug resulting from Ubuntu providing incorrect metadata to pip.  
freeze:
	pip freeze | grep -v "pkg_resources" > requirements.txt