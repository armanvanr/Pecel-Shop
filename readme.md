# Pecel Shop
## Instalasi

Untuk menjalankan project pastikan sudah menginstall phyton.

Buka directory project dan jalankan command dibawah
```sh
pip install -r requirements.txt
```
Perintah diatas digunakan untuk menginstall semua dependency yang dibutuhkan project ini. Setelah itu untuk menjalankan project bisa menjalankan perintah.

Linux :
```sh
gunicorn wsgi:app
```

Windows :
```sh
waitress-serve --listen=*:5000 wsgi:app
```

project bisa dibuka di [http://localhost:5000][localhost]

## Alur deploy heroku
Saat proses deploy heroku akan otomatis menginstall dependency yang ada di file `requirements.txt` dan kemudian menjalankan perintah yang ada di file `Procfile`

## Error saat deploy
Apabila ada pesan error `Your account has reached its concurrent builds limit.`

bisa merestart menggungkan perintah heroku CLI
```sh
heroku restart
```
kemudian deploy ulang.

## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [localhost]: <http://localhost:5000/>
