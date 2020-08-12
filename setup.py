from cx_Freeze import setup, Executable

setup(name = 'Client',
      version = '0.1',
      executables = [Executable('client.py'), Executable('server.py')])

