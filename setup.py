from cx_Freeze import setup, Executable

setup(name='web_to_text',
      version='1.0',
      description='Dada una url devuelve la web en texto y en el portapapeles',
      executables=[Executable('web_to_text.py')],
      options={
          'build_exe': {
              'packages': ['os', 'requests', 'sys', 'bs4', 'pyperclip'],
              'include_files': []
          }
      }
      )



