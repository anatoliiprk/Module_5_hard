from time import sleep

print('------ \nЗадание "Свой YouTube"\n------')


class User:
    def __init__(self, nickname: str, password, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title: str, duration: int, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title


class UrTube:
    def __init__(self, current_user: User = None):
        self.users = []
        self.videos = []
        self.current_user = current_user

    def log_in(self, nickname, password):
        password = hash(password)
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user
        return self.current_user

    def register(self, nickname, password, age):
        password = hash(password)
        flag = False
        if self.users == []:
            flag = True
        else:
            for user in self.users:
                if nickname == user.nickname:
                    flag = False
                    break
                else:
                    flag = True
        if flag:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user
        else:
            sleep(1)
            print(f'Пользователь {nickname} уже существует.')
            print('Текущий пользователь', end=' ')
        return self.current_user

    def log_out(self):
        self.current_user = None
        sleep(1)
        return print('Авторизируйтесь для входа')

    def add(self, *new_videos: Video):
        for new_video in new_videos:
            if self.videos == []:
                self.videos.append(new_video)
            else:
                for video in self.videos:
                    if new_video.title != video.title:
                        self.videos.append(new_video)
        return self.videos

    def get_videos(self, search_word):
        search_list = []
        search_word = search_word.lower()
        for video in self.videos:
            lower_title = video.title.lower()
            if search_word in lower_title:
                search_list.append(video.title)
        sleep(1)
        return search_list

    def watch_video(self, name):
        if self.current_user is None:
            sleep(1)
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for video in self.videos:
                if name == video.title:
                    if video.adult_mode and self.current_user.age < 18:
                        sleep(1)
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        sleep(1)
                        print('\nВоспроизведение видео')
                        for sec in range(video.duration):
                            print(video.time_now, end=' ')
                            video.time_now += 1
                            sleep(1)
                        print('\nКонец видео\n')
                        continue
        return self.videos


#------

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')