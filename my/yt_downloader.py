from os import startfile
from pytube import YouTube
from pre import cls 
cls()

url=input('Video url: ')

vdo=YouTube(url)
print(vdo.author)

extension=input('MP3/MP4: ')

s=vdo.streams

if extension[0].lower()=='v' or extension[2]=='4':
    tipo='mp4'
    s=s.get_highest_resolution()
elif extension[0].lower()=='a' or extension[2]=='3':
    tipo='mp3'
    s=s.filter(only_audio=True)
    s=s.first()

name=input('Save as: ')+'.'

path='C:/Users/32165/Desktop/Downloads/'+tipo+'/'+name+tipo

print(path)

s.download('C:/Users/32165/Desktop/Downloads/'+tipo,name+tipo)
startfile(path)

print(s)
