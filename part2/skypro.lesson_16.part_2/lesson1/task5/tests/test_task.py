import unittest

import sqlalchemy

data = [{'user': 2, 'surname': 'Васечкин', 'full_name': 'Андрей Васечкин', 'tours_count': 5,
         'bio': 'Я обожаю Москву, и изучаю город с необычных ракурсов. С радостью поделюсь с вами своими лучшими открытиями. Мы поднимемся на сталинские высотки и посмотрим на исторический центр сверху. Я покажу вам то, что скрыто от глаз большинства туристов и даже жителей города. Маршруты подобра индивидуально под ваш запрос. Для влюбленных доступна услуга свидания на крыше.',
         'is_pro': True, 'company': 1},
        {'user': 1, 'surname': 'Новикова', 'full_name': 'Людмила Новикова', 'tours_count': 2,
         'bio': 'Я петербурженка в 7-м поколении. Люблю делиться историями и секретами дореволюционных петербургских зданий и особняков. Поделюсь историями моей бабушки. Вместе со мной работает небольшая дружная команда влюбленных в Петербург местных гидов. Мы раскроем вам секреты старинных домов и покажем то, что скрыто от глаз большинства туристов и жителей города.',
         'is_pro': True, 'company': 2},
        {'user': 3, 'surname': 'Беридзе', 'full_name': 'Георги Беридзе', 'tours_count': 5,
         'bio': 'Филолог-журналист по образованию. За плечами более 9 лет экскурсий по Грузии и барменский опыт. Писатель. Перфекционист. И просто увлеченный человек. Родился и вырос в Тбилиси. Более 10-поколений тут. Люблю этот райский уголок на планете и свою работу. Мама-кулинар привила любовь ко вкусной еде.',
         'is_pro': True, 'company': None},
        {'user': 4, 'surname': 'Ласкина', 'full_name': 'Оксана Ласкина', 'tours_count': 2,
         'bio': 'Я всегда увлекалась историей и, как следствие, получила образования гида-экскурсовода. С удовольствием знакомлю гостей города с историей, татарской культурой и традициями. Вы влюбитесь в наш край.',
         'is_pro': True, 'company': 5},
        {'user': 5, 'surname': 'Горячий', 'full_name': 'Иван Горячий', 'tours_count': 7,
         'bio': 'Работал учителем истории более 10 лет, последние 5 лет живу в Сочи и уже третий год провожу экскурсии, орагнизовываю туры. На моих прогулках и турах вы узнаете не только об экскурсионных объектах, но и о том, чем живет современный Сочи: о ценах, недвижимости, об интересных местах города и его необычных заведениях. Есть туры разного уровня сложности и комфорта, где можно с детьми и без. Бесплатным бонусом ко всем экскурсиям станет фотосессия на зеркальный фотоаппарат.',
         'is_pro': True, 'company': 4},
        {'user': 6, 'surname': 'Ивлева', 'full_name': 'Яна Ивлева', 'tours_count': 5,
         'bio': 'Я живу в Стамбуле много лет. По образованию филолог и историк. О Стамбуле читаю, пишу, живуэтим городом и люблю его. Раскрою его вам таким, какой он есть: великолепный, приветливый, неизменно интересный и всегда загадочный. Ваше путешествие по этому сказочному городу навсегда осталось в памяти и сердце. ',
         'is_pro': True, 'company': 1},
        {'user': 7, 'surname': 'Самидзе', 'full_name': 'Ирина Самидзе', 'tours_count': 1,
         'bio': 'Живу в Риме уже более десяти лет и с каждым днем влюбляюсь в этот город все больше и больше. Моя миссия в том, чтобы и вы почувствовали после нашей прогулки то же самое. Приглашаю вас познакомиться с Вечным городом и увидеть его глазами местного жителя, прочувствовать всю атмосферу и колорит столицы. Насладиться видами, едой и историей этого города.',
         'is_pro': False, 'company': None},
        {'user': 8, 'surname': 'Ванькин', 'full_name': 'Владислав Ванькин', 'tours_count': 1,
         'bio': 'Хеллоу! 11 лет писал для тревел-журналов, потом кризис среднего возраста, желание перемен и внезапный переезд в Псков, где впервые почувствовал себя дома. Провожу экскурсии-погружения по местам, которые не оставят вас равнодушным. Приглашаю вас в путешествие по Изборску и живописным окрестностям — на пару часов или дней. Показываю и открываю самые живописные тропы, знакомлю с местными жителями — фермерами и ремесленниками, а из множества исторических фактов — выбираю действительно важные и интересные ;)',
         'is_pro': False, 'company': None},
        {'user': 9, 'surname': 'Левинова', 'full_name': 'Дина Левинова', 'tours_count': 1,
         'bio': 'Авторизированный гид, член Ассоциации профессиональных гидов Хельсинки, член клуба Знатоков города и рабочей комиссии университета. По жизни: живу в Финляндии 35 лет. 23 из них - работала в турсфере, а также гидом для души, т.к. очень люблю это дело. Исходила город вдоль и поперек, замучала рассказами родных и друзей, прочитала сотню, а то и больше книг, и провела сотни часов в архивах. Н не перестаю находить новые интересные факты, истории, места, которые и хочу показать гостям. Покажу город дркгим, не так как о его обычно показывают и описывают в экскурсияя на один день из Питера и пишут в большистве путеводителей. Открою вам новый Хельсинки, каким его вижу я: с плюсами и минусами, поделюсь радостными и печальными фактами истории, а также секретами, легендами, реалиями сегодняшнего дня.',
         'is_pro': True, 'company': None},
        {'user': 10, 'surname': 'Звонкий', 'full_name': 'Марк Звонкий', 'tours_count': 1,
         'bio': 'Спорю, что такой экскурсии у вас еще не было. Я организую туры с закрытыми глазами. Да-да, вы все верно прочитали. Но какой в этом смыcл, если ничего не видно? Без одного из главных органов восприятия, город ощущается совсем иначе. Вас ждет по-настоящему необычное путешествие, которое надолго запомнится своими хорошими эмоциями.',
         'is_pro': False, 'company': None}]


class TestCase(unittest.TestCase):
    def test(self):
        try:
            from task import do_request, Guide
        except ImportError:
            self.fail("Не правильное имя класса do_request, Guide")
        except sqlalchemy.exc.ArgumentError:
            self.fail("Ошибка в синтаксисе модели, не задан атрибут primaryKey или что-то еще")
        try:
            from task import db
        except ImportError:
            self.fail("Отсутствует переменная db, которая была изначально")

        db.drop_all()
        db.create_all()

        for d in data:
            guide = Guide(id=d.get("user"),
                          surname=d.get("surname"),
                          full_name=d.get("full_name"),
                          tours_count=d.get("tours_count"),
                          bio=d.get("bio"),
                          is_pro=d.get("is_pro"),
                          company=d.get("company"),
                          )
            with db.session.begin():
                db.session.add(guide)

        result = do_request()
        solution = [3, 7, 8, 9, 10]
        self.assertTrue(len(result) == len(solution), msg="Запрос написан не корректно")
        for r in result:
            self.assertTrue(r.id in solution, msg="Запрос написан не корректно")