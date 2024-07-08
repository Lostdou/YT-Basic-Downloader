from pytube import YouTube

my_proxies= {
    "http":"20.84.109.185:80"
}

video_url = input('Ingrese la url del video: ')

yt = YouTube(video_url, 
             proxies=my_proxies,
             use_oauth=True,
             allow_oauth_cache=True)
stream = yt.streams.get_highest_resolution()
stream.download()

print('Descarga completada')