from pathlib import Path
import pyAesCrypt

dir = Path('C:/Users/Rafael/Desktop/teste')
senha = 'root'

def encr():
    var = dir.glob('**/*')
    for arquivo in var:
        if arquivo.is_file():
            pyAesCrypt.encryptFile(str(arquivo), outfile=f'{arquivo}.pct', passw=senha, bufferSize=10000*1024)
            if not '.pct' in arquivo.name:
                arquivo.unlink()
            
            
def desc():
    var = dir.glob('**/*.pct')
    for arquivo in var:
        if arquivo.is_file():
            original = arquivo.with_suffix('')
            try:
                pyAesCrypt.decryptFile(str(arquivo), str(original), passw=senha, bufferSize=10000*1024)
                arquivo.unlink()
            except ValueError:
                print('Senha Incorreta')
            print(original)
            
#encr()
desc()
