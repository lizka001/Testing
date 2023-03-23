# Вы можете расположить сценарий своей игры в этом файле.
# Определение персонажей игры.
define Lukashenko = Character('Александр Рыгорыч', color="#ffffff")
define Narrator = Character('Неизвестный голос',
                            window_background="gui/narrator_screen.png",
                            color="#ffffff")
default score_chance = 0


#image library = 'bg/street.png'
image office = 'bg/office.jpg'
image lukash = 'lukash.png'
image photo = 'photo1.png'
image blood = 'overlayer/blood.png'
image gray = 'overlayer/grayover.png'
image blood_over = 'overlayer/over.png'
define audio.first = "audio/first.mp3"
define audio.firstquestion = "audio/quest1.mp3"
define audio.second = "audio/second.mp3"
define audio.scary = "audio/sound/scary_sound.wav"
define audio.trans = "audio/sound/trans.wav"
define audio.slide = "audio/sound/slide.wav"
define audio.photo = "audio/sound/phtos.wav"

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    play music first volume 0.05
    play sound scary volume 0.2 loop

    scene office

    show lukash:
        xzoom 0.5
        yzoom 0.5
        xalign 0.5
        yalign 0.45
    show gray onlayer gray
    show blood onlayer blood with dissolve
    show blood_over onlayer blood_overlay

    centered "Вот и всё. Ты дошутился."


    centered "Ты приехал в Беларусь всего неделю назад, \
              но рискуешь остаться здесь до конца своей жизни.\
              Всё началось с невинной фотографии возле флага,\
              просто ты не знал, что этот флаг запрещён \
              на территории Беларуси." with dissolve
    centered "А теперь тебя обвиняют в терроризме и использовании экстремистской символики" with dissolve

    centered "P.S. Флаг не запрещён, но кого волнует закон в Беларуси?" with dissolve

    centered "Чтобы избежать смертной казни, тебе необходимо принести свои извинения президенту и доказать ему, что ты \
    любишь Беларусь, а самое главное - любишь и восхищаешься правящим лидером" with dissolve

    centered "Правила игры:\
    \
    необходимо применить свои навыки красноречия и знания о Беларуси, которые у тебя есть.\
    Некоторых вопросов можно избежать, если заболтать президента, но если он поймёт, что ты его специально пытаешься увести от темы, то отнимет у тебя шансы на свободу."
    with dissolve
    centered "Во время игры ты набираешь проценты свободы, в конце шанс твоего помилования равен проценту свободы. \
            То есть если за всю игру ты набрал 100 свободы, то ты освобождаешься без сомнения, \
              если набрал 89 шансов, то тебя помилуют с 89 процентной вероятностью." with dissolve

    centered "НО не всё так просто..." with dissolve
    jump scene_first

    return

label scene_first:
    play sound trans volume 0.01
    hide gray onlayer gray with dissolve
    hide blood onlayer blood with dissolve
    hide blood_over onlayer blood_overlay with dissolve

    play music second volume 0.05 fadeout 1.0


    scene office

    show lukash:
        xzoom 0.5
        yzoom 0.5
        xalign 0.5
        yalign 0.45

    Lukashenko "Наконец ты очнулась"
    Lukashenko "Добро пожаловать в мою резиденцию. Здесь я разбираюсь с такими, как ты и решаю вашу дальнейшую судьбу."
    menu:
        "То есть либо тюрьма, либо свобода?":
            Lukashenko "Ахахаха"
            Lukashenko "Где это видано, чтобы за оскорбление президента было такое неинтересно наказание?"
            Lukashenko  "Нет, в моей стране всё иначе: либо смертная казнь, либо я буду столь великодушен и подарю тебе свободу"
            menu:
                    "Смертная казнь? То есть вы меня убьёте? Но я же вообще ничего не сделала... Я даже не умею чи...":
                        Lukashenko "Ничего не сделала? Ахахахаха"
                        Lukashenko "Давай посмотрим твоё дело"
                        play sound slide volume 0.15
                        Lukashenko "Полина Ефремова... 2 октября... это всё неинтересно"
                        play sound slide volume 0.15
                        Lukashenko "О, нашёл, взгляни-ка, узнаёшь кого-нибудь?"
                        menu:
                                "Посмотреть фото":
                                    jump photo
                                "Это ошибка, я не буду ничего смотреть!":
                                    Lukashenko "Нет, ты всё же посмотри"
                                    jump photo




label photo:
        play sound photo volume 0.1
        scene office
        show photo
        'Фото, которое тебе дал Рыгорыч'
        jump scene_second

label scene_second:
    play sound photo volume 0.1
    scene office
    show lukash:
        xzoom 0.5
        yzoom 0.5
        xalign 0.5
        yalign 0.45
    menu:
        "Это фотошоп, посмотрите, как пропорции лица поехали. Я не виновата!":
            Lukashenko "Фотошоп или не фотошоп уже определили эксперты. Раз ты тут, то вывод очевиден"
            Lukashenko "Короче, давай без чая з варэннем. Отвечай на мои вопросы честно и если мне понравятся твои ответы, то я тебя помилую"
            Lukashenko "Ну что выбираешь? Смерть или вопросы?"
            menu:
                'Вопросы...':
                    Lukashenko 'Молодец, девочка. Правильный выбор.'
                    jump question1
                "Не буду я отвечать на ваши глупые вопросы":
                    Lukashenko 'Шкада, как говорят в Беларуси, но ты сама выбрала свой путь'
                    jump death
                "А может можно как-то по-другому... ну... вы понимаете...":
                    Lukashenko 'Что ты себе позволяешь? Я тебе дал только два выбора.'
                    menu:
                        'Я поняла, извините... Выбираю вопросы':
                            Lukashenko 'Лучше бы сразу выбрала этот вариант.'
                            Lukashenko "Итак, вопрос первый"
                            jump question1
                        'Ёмаё, ну тогда я лучше умру':
                            jump death

label question1:
    show gray onlayer gray
    show blood_over onlayer blood_overlay
    play music firstquestion volume 0.02 loop
    scene office
    play music firstquestion volume 0.02 loop
    scene office
    show lukash:
        xzoom 0.5
        yzoom 0.5
        xalign 0.5
        yalign 0.45
    centered 'Вопрос 1 \
    Как правильно писать название нашей страны на русском языке?'
    menu:

        'Беларусь':
            $ score_chance= score_chance + 10
            Lukashenko 'Ты меня удивила, переходим к следующему вопросу'
            "Получено 10 шансов"
            jump question2
        'Белоруссия':
            $ score_chance = score_chance + 0
            Lukashenko 'Правительство России так не считает, все документы о союзных государствах и подобные используют название "Республика Беларусь"'
        'Белорусь':
            $ score_chance = score_chance + 0
            Lukashenko 'Хм, а ты на самом деле не умеешь читать'
        'Дядя, а может не надо?':
            Lukashenko 'Хорошо, пропустим этот вопрос, но отнимем шансы'
            $ score_chance = score_chance - 10
            "Ты потеряла 10 шансов"
label question2:

    show lukash:
        xzoom 0.5
        yzoom 0.5
        xalign 0.5
        yalign 0.45
    '123'

label death:

    show lukash:
        xzoom 0.5
        yzoom 0.5
        xalign 0.5
        yalign 0.45
    '123'
