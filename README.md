# PythonInstallable
Simple project to demonstrate creation of executable from a python file


conda install pyinstaller

in the folder where the file is located
pyinstaller --onefile --add-binary **\ibm_db.dll;.\ibm_db_dlls test_python.py
pyinstaller --onefile --add-binary **\ibm_db.dll;.\ibm_db_dlls test_python.spec