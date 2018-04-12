import os
import time


class Foo():
    def GetInfo(self, path):
        name_list = os.listdir(path)   #tworzy listę plików w folderze
        files = []
        for i in name_list:
            info = os.stat('{}/{}'.format(path, i))     #pobiera dostępne informacje o każdym pliku
            file_info = [i, info.st_size, info.st_mtime]     #tworzy tablicę z danymi o pliku
            files.append(file_info)     #dodaje dane do listy z plikami
        return files

    def ConvertInfo(self, rough):
        readable = ['name - size - modification time']
        for i in rough:
            size = '{} MB'.format(round(i[1]/8/1024**2, 2))     #konweetuje rozmiar z b na MB
            tm1 = time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(i[2]))  #konwertuje czas modyfikacji z sekund na datę
            #tm2 = time.asctime(time.localtime(i[2]))        zwraca format Wed Apr  6 09:07:04 2016
            record = '{} - {} - {}'.format(i[0], size, tm1)
            readable.append(record)
        return readable

music_file = 'C:/pliki_py/music'  #sicezka folderu z muzyka
x = Foo()
rough = x.GetInfo(music_file)
fine = x.ConvertInfo(rough)
print(fine)
