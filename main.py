import yt_dlp


def file_download(URLS, codec):

    ydl_opts = {
        'format': 'bestaudio/best',
        'ffmpeg_location': 'C:/ffmpeg/bin',
        # 'outtmpl': 'C:/Users/adria/Music/Pobrane yt',
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': codec,
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(URLS)

# type 0 - zwraca liczbę, type 1 zwraca opcje


def menu(title, options, type):

    print()
    print(title)
    print()

    for i in range(len(options)):
        print(str(i+1) + " | " + options[i])

    print()

    while True:

        command = input(": ")

        try:
            n = int(command)
        except:
            print("\nNieprawidlowa wartosc\n")
            continue

        if n > 0 and n <= len(options):
            if type == 0:
                return n
            elif type == 1:
                return options[n-1]
        else:
            print("\nNieprawidlowa wartosc\n")


while True:

    URLS = []

    codec = menu("Wybierz kodek", ('mp3', 'm4a', 'wav'), 1)

    print("\nPodawaj linki, na koniec wpisz 0\n")

    while True:
        url = input(": ")

        if url == "0":
            break
        else:
            URLS.append(url)

    print("\nLinki dodane!\n")

    file_download(URLS, codec)

    command = menu("Co dalej?", ('Dalej', 'Koniec'), 0)

    if command == 2:
        break
