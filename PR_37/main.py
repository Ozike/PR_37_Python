from random import randint
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.app import App
from kivy.config import Config
from kivy.uix.image import Image


Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'resizable', 'false')

number_correct_answers = 0
number_question = 1



question_list = [['https://zamanilka.ru/wp-content/uploads/2022/05/smeshariki-krosh-kartinki-23.jpg', 'Крош', 'Кролик', 'Зайка', 'Мики', 1],
                 ['https://mykaleidoscope.ru/x/uploads/posts/2022-09/1663635911_1-mykaleidoscope-ru-p-zloi-kar-karich-krasivo-1.jpg',
                     'Ворон', 'Кар-карыч', 'Каркун', 'Карыч', 2],
                 ['https://i.ytimg.com/vi/lPVtHWVwtWE/maxresdefault.jpg',
                     'Ежик', 'Колючка', 'Ежидзе', 'Клим', 1],
                 ['https://100-bal.ru/pars_docs/refs/131/130143/130143_html_371854c8.jpg', 'Филинн',
                  'Совунья', 'Сова', 'Совушка', 2],
                 ['https://phonoteka.org/uploads/posts/2023-03/1679946865_phonoteka-org-p-smeshariki-nyusha-oboi-krasivo-31.jpg',
                  'Мила', 'Нюша', 'Пигги', 'Свинка', 2],
                 ['http://edge2.dtlab.ru/image/screenshot/PSTGMLT014623.jpg',
                  'Бараш', 'Барашка', 'Баран', 'Баранидзе', 1],
                 ['https://webmg.ru/wp-content/uploads/2022/11/i-22-53.jpeg',
                  'Оленеш', 'Лоскут', 'Лосяш', 'Лось', 3],
                 ['https://mykaleidoscope.ru/x/uploads/posts/2022-09/1663252506_5-mykaleidoscope-ru-p-zloi-kopatich-oboi-5.jpg',
                  'Мишка', 'Медведь', 'Мишка фреди', 'Копатыч', 4],
                 ['https://flomaster.club/uploads/posts/2023-01/1674059143_flomaster-club-p-pin-smeshariki-risunok-pinterest-14.jpg',
                  'Пин', 'Пингвин', 'Пингвиша', 'Лоло', 1],
                 ['https://m.media-amazon.com/images/M/MV5BZjA1MDhiYmEtODk0ZS00NjAyLTgwYmItMjA0Y2M3ZGE5ZTNiXkEyXkFqcGdeQXVyNTc0NjY1ODk@._V1_FMjpg_UX1000_.jpg', 'Панди',
                  'Панда', 'Мила', 'Степаша', 1],
                 ['https://i.ytimg.com/vi/kkvOCjjzHp4/maxresdefault.jpg',
                  'Боба', 'Руби', 'Биба', 'Биби', 4],
                 ['https://avatars.dzeninfra.ru/get-zen_doc/5234097/pub_60f16a93a7eab75c27c7d17f_60f17de2cf9db26dda648fa1/scale_1200',
                  'Мышарик', 'Мышь', 'Крыс', 'Микки', 1],
                 ['https://i.ytimg.com/vi/WNzGSfqO5nE/maxresdefault.jpg',
                  'Железяка', 'Милли', 'Железная няня', 'Няня', 3],
                 ['https://vignette.wikia.nocookie.net/shararam-smeshi/images/a/a5/%D0%A5%D1%80%D1%83%D0%BC.png/revision/latest?cb=20180825013800&path-prefix=ru', 'Дракоша', 'Антошка', 'Хрум', 'Тимоша', 3],
                 ['https://sun9-66.userapi.com/impf/c626722/v626722802/162c7/3BqL9rlJZ5E.jpg?size=604x604&quality=96&sign=84cf662044a22014c6afa4f6d908a69a&type=album', 'Лягушка', 'Жаба', 'Лягуш', 'Шиша', 1]]


class MainWidget(BoxLayout):
    def new_question(self):
        img_result = None  # Initialize img_result to None

        if len(question_list) > 0:
            question = question_list[randint(0, len(question_list)-1)]
            self.ids['img_question'].source = question[0]
            self.ids['btn_answer1'].text = question[1]
            self.ids['btn_answer2'].text = question[2]
            self.ids['btn_answer3'].text = question[3]
            self.ids['btn_answer4'].text = question[4]
        else:
            text = '\n Результат: ' + str(number_correct_answers) + ' из 15.'
            self.ids['lbl_question'].text = text
            self.remove_widget(self.ids['img_question'])
            self.remove_widget(self.ids['layout_btns'])
            if number_correct_answers >= 12:
                text1 = 'Вы - Стильный бараш'
                self.ids['lbl_result'].text = text1
                self.ids['img_result'].source = 'source/Barash.jpg'
            elif number_correct_answers >= 9:
                text1 = 'Вы - Лосяш'
                self.ids['lbl_result'].text = text1
                self.ids['img_result'].source = 'source/Losyash.jpg'

            elif number_correct_answers >= 6:
                text1 = 'Вы - Ежидзе'
                self.ids['lbl_result'].text = text1
                self.ids['img_result'].source = 'source/Ezhidze.jpg'
                
            elif number_correct_answers >= 3:
                text1 = 'Вы - Крош'
                self.ids['lbl_result'].text = text1
                self.ids['img_result'].source = 'source/Krosh.jpg'

            elif number_correct_answers >= 0:
                text1 = 'Вы - Бунтующий ежик'
                self.ids['lbl_result'].text = text1
                self.ids['img_result'].source = 'source/Bunt.jpg'

            self.ids['img_result'].opacity = 1

    def btn_pressed(self, number_button):
        question: list
        for i in question_list:
            if (i[0] == self.ids['img_question'].source):
                question = i
                break  # Перебор списка, чтобы выбрать вопрос который выпал из списка
        global number_correct_answers
        global number_question
        if (number_button == question[5]):
            number_correct_answers += 1

        number_question += 1
        question_list.remove(question)
        self.new_question()


class MainApp(App):
    def build(self):
        app = MainWidget()
        app.new_question()  # вызываем new_question из build метода, когда окно приложения готово
        return app


if __name__ == '__main__':
    music = SoundLoader.load('Disco.mp3')
    music.volume = 0.1
    music.play()

    MainApp().run()
