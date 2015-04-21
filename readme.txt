Сейчас это очень сырая реализация чата. Тем не менее, работает авторизация, запиминаются куки и всё в принципе готово для расщирения.

Как запускать: перейти в директорию cgi-bin и выполнить в ней эти команды: 
sudo chmod +x cookie.py
sudo chmod +x form.py
sudo chmod +x hello.py
sudo chmod +x wall.py

дальше перейти в корень и выполнить 
python3 -m http.server --cgi