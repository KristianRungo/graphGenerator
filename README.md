# graphGenerator
Generates DAG graphs and drawings if you ask very nicely :)

Installation for windows

Run in command prompt
- pip install networkx[default] 

Add C:\Users\\$YourUser\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts to the Path environment variable in your system variables 

If the dir above doesn't resolve to anything, go hunting for the files. The folder you wanna find contains the following files

f2py.exe

fonttools.exe

pyftmerge.exe

pyftsubset.exe

ttx.exe


Installing networkx is only necessary if you want your graphs drawn. If you don't want them drawn, just run generatorNoDrawings

Will create .in files, and images, in the directory the python file is located equal to the amount of test cases you request.
