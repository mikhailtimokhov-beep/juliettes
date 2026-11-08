"""Генератор страницы «10 концепций соцсетей, детальная прорисовка» (v2).
Фото подставляет scripts/build-visual.py из imgs-social.json (ключи IMG_<ПАПКА>_<N>).
Запуск: python3 -I social/build/concepts_v2.py > social/concepts-v2.template.html
"""
import html as H

def e(s): return H.escape(s, quote=False)

SVG_CAR = '<svg viewBox="0 0 24 24" class="ic"><rect x="7" y="3" width="14" height="14" rx="2" fill="none" stroke="#fff" stroke-width="2"/><rect x="3" y="7" width="14" height="14" rx="2" fill="#fff" fill-opacity=".9"/></svg>'
SVG_REEL = '<svg viewBox="0 0 24 24" class="ic"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="#fff" stroke-width="2"/><path d="M10 8.5v7l6-3.5z" fill="#fff"/></svg>'
SVG_PIN = '<svg viewBox="0 0 24 24" class="ic"><path d="M14 3l7 7-3 1-4 4 1 4-2 1-4-4-4 4-1-1 4-4-4-4 1-2 4 1 4-4z" fill="#fff"/></svg>'
BADGE = {'car': SVG_CAR, 'reel': SVG_REEL, 'pin': SVG_PIN}

USED = set()
# Комплаенс-метка на плитке/в био: «пример» — вымышленный текст, «сверить» — факт ждёт подтверждения владельца.
def mark(s='сверить'): return f'<em class="chk">{e(s)}</em>'
def photo(img, cap='', badge='', pos='center', extra='', chk=''):
    USED.add(img)
    b = BADGE.get(badge, '')
    c = f'<span class="cap">{cap}</span>' if cap else ''
    m = mark(chk) if chk else ''
    return f'<div class="tile ph {extra}"><i class="img {img}" style="background-position:{pos}"></i>{c}{b}{m}</div>'
def text(inner, cls='', badge='', chk=''):
    m = mark(chk) if chk else ''
    return f'<div class="tile tx {cls}">{inner}{BADGE.get(badge,"")}{m}</div>'
def frame(label, badge=''):
    return f'<div class="tile fr"><span>кадр:<br>{e(label)}</span>{BADGE.get(badge,"")}</div>'
def polar(img, cap, rot=-3, chk=''):
    USED.add(img)
    m = mark(chk) if chk else ''
    return f'<div class="tile pol"><div class="pf" style="transform:rotate({rot}deg)"><i class="img {img}"></i><b>{cap}</b></div><span class="tape"></span>{m}</div>'
def mini(img):
    USED.add(img); return f'<i class="img {img} mn"></i>'

C = []
# ───────────── 1. Мастерская изнутри
C.append(dict(n=1, key='c1', name='Мастерская изнутри', idea='Документальный сериал о том, как рождается браслет: этап за этапом, монохромно, с номерами этапов.',
 pal=['#121212','#EDEAE4','#C9A45C','#6E6A64'], fonts='Oswald · IBM Plex Mono',
 avatar='<b class="av-j">J</b><small>мастерская</small>',
 bio=['<b>Juliette\'s · ювелирная мастерская</b>','Делаем браслеты с вашими детьми вручную','Этап за этапом — в историях ↓','Москва · доставка по России'],
 cta='Заказ', hl=[('01','Эскиз'),('02','Воск'),('03','Литьё'),('04','Закрепка'),('05','Гравировка')],
 tiles=[
  text('<small>серия «Как рождается браслет» · 1/6</small><b>ЭТАП 01<br>ЭСКИЗ</b>', 'k-big', 'pin'),
  frame('эскиз с именами детей на верстаке', 'reel'),
  photo('IMG_ENGRAVE_07','ЗАГОТОВКА · 925', chk='металл сверить'),
  photo('IMG_ENGRAVE_12','ГРАВИРОВКА','reel'),
  frame('восковая модель фигурки под лампой'),
  text('<small>ОТК · перед отправкой</small><ul><li>проба</li><li>замок</li><li>гравировка</li><li>полировка</li></ul>','k-list'),
  photo('IMG_HEELS22_08','ПАРТИЯ · НЕДЕЛЯ 45'),
  frame('руки мастера: закрепка камня под микроскопом','reel'),
  photo('IMG_RINGS_03','ИМЕНА ВНУТРИ'),
  text('<b>до 10</b><small>рабочих дней живёт ваш заказ в мастерской · по сайту</small>','k-num'),
  photo('IMG_ENGRAVE_04','ИМЯ · ДАТА · РОСТ · ВЕС'),
  frame('литьё: металл в опоке','reel'),
  photo('IMG_PUGOVKI_00','ПУГОВКА · ПОЛИРОВКА'),
  text('<small>вопрос мастеру</small><p>— Можно добавить фигурку в готовый браслет?</p><p>— Да. Мастер впаяет новую.</p>','k-qa','car', chk='сверить'),
  photo('IMG_WHITE_06','КРАСНОЕ ЗОЛОТО 585', chk='металл сверить'),
  photo('IMG_ENGRAVE_15','ГОТОВО'),
  frame('упаковка: бирка и коробка'),
  text('<small>серия · 6/6</small><b>ЭТАП 06<br>ВРУЧЕНИЕ</b>','k-big')]))
# ───────────── 2. Семейные истории
C.append(dict(n=2, key='c2', name='Семейные истории', idea='Журнал о семьях клиентов: фото и цитата, по пятницам одна большая история.',
 pal=['#F6EFE6','#3B2A20','#B0552F','#D9C7B2'], fonts='Playfair Display · Lora',
 avatar='<b class="av-j">J’s</b>',
 bio=['<b>Juliette\'s jewelry</b>','Браслеты с вашими детьми · своя мастерская','Каждую пятницу — история одной семьи','Расскажите свою — напишите нам'],
 cta='Рассказать', hl=[('IMG_FRIENDS20_10','Три дочки'),('IMG_CROSS23_15','Папа'),('IMG_HOME_13','Мама'),('IMG_FRIENDS20_11','Сыновья'),('IMG_NY22_01','Новый год')], hlphoto=True,
 tiles=[
  photo('IMG_FRIENDS20_10','<em>История №12</em> · «Три девочки и один браслет»','car', chk='пример'),
  text('<q>Я ношу их имена на запястье с того дня, как родилась младшая</q><small>Анна, мама троих · пример</small>','q'),
  photo('IMG_CROSS23_06'),
  photo('IMG_FRIENDS20_02','«Он заказал его, пока я была в роддоме»','car', chk='пример'),
  text('<small>пятничная история</small><b>Как Миша выбирал браслет жене за три дня до выписки</b>','t-title', chk='пример'),
  photo('IMG_HOME_13'),
  photo('IMG_FRIENDS20_11'),
  text('<q>На обороте — рост, вес и 05:40 утра. Это время я не забуду</q><small>пример</small>','q'),
  photo('IMG_CROSS23_10','','reel'),
  photo('IMG_NY22_01'),
  text('<b>Ваша история</b><small>Расскажите, как появился ваш браслет. Опубликуем с вашего согласия</small>','t-cta'),
  photo('IMG_FRIENDS20_14'),
  photo('IMG_HOME_05'),
  photo('IMG_CROSS23_00'),
  text('<q>Добавили третью фигурку — теперь все в сборе</q><small>пример</small>','q'),
  photo('IMG_FRIENDS20_15'),
  photo('IMG_NY22_15'),
  photo('IMG_CROSS23_15','','car')]))
# ───────────── 3. Тихая роскошь
C.append(dict(n=3, key='c3', name='Тихая роскошь', idea='Золото в полумраке: тёмные кадры, много воздуха, почти без слов. Работает на средний чек.',
 pal=['#0E1512','#E9E4D8','#B9975B','#2A332E'], fonts='Cormorant Garamond · Jost',
 avatar='<b class="av-j">J</b>',
 bio=['<b>JULIETTE’S</b>','Золото 585 · камни · ручная работа','Консультация ювелира — по записи '+mark('формат сверить'),'Москва'],
 cta='Записаться', hl=[('Au','Золото'),('◇','Камни'),('J','На заказ'),('▢','Упаковка'),('✉','Контакты')],
 tiles=[
  photo('IMG_NY21_06'),
  text('<span class="ln"></span><b>Две фигурки.<br>Одна история.</b>','lx'),
  photo('IMG_HEELS22_05'),
  photo('IMG_CROSS23_09','','reel'),
  photo('IMG_NY22_05'),
  text('<b class="big">585</b><small>красное · белое · лимонное</small>','lx'),
  photo('IMG_HEELS22_00'),
  photo('IMG_NY22_02'),
  photo('IMG_NY21_02'),
  text('<small>деталь</small><b>Камни вставляет мастер вручную, по одному</b>','lx'),
  photo('IMG_NY22_03'),
  photo('IMG_HEELS22_03','','reel'),
  photo('IMG_CROSS23_07'),
  text('<small>по записи</small><b>Консультация ювелира: видеозвонок или встреча</b>','lx', chk='формат сверить'),
  photo('IMG_NY21_07'),
  photo('IMG_HOME_12'),
  photo('IMG_HEELS22_06'),
  text('<b class="mono">J</b>','lx')]))
# ───────────── 4. Архив первых шагов
C.append(dict(n=4, key='c4', name='Архив первых шагов', idea='Лента как семейная картотека: карточки с метрикой, архивные фото коллекций, «пополнение» — новая фигурка в браслет.',
 pal=['#EFE9DC','#2B2B2B','#B23A2E','#C8BDA6'], fonts='PT Mono · PT Serif',
 avatar='<b class="av-j">J</b><small>архив</small>',
 bio=['<b>Juliette\'s · архив первых шагов</b>','Храним имена, рост, вес и время рождения — в золоте и серебре','Добавить фигурку в браслет → «Пополнение»'],
 cta='Карточка', hl=[('2019','2019'),('2021','2021'),('×2','Двойни'),('+1','Пополнение'),('Ab','Гравировка')],
 tiles=[
  text('<small>КАРТОЧКА № 0127</small><dl><dt>Имя</dt><dd>Дарья</dd><dt>Время</dt><dd>22:15</dd><dt>Рост</dt><dd>52 см</dd><dt>Вес</dt><dd>3 200 г</dd><dt>Металл</dt><dd>кр. золото 585</dd></dl><span class="stamp">ВЫДАНО</span><em>пример</em>','card','pin'),
  photo('IMG_ENGRAVE_15','ОБРАЗЕЦ № 214'),
  photo('IMG_PILLOW_00','АРХИВ · 2019'),
  photo('IMG_ENGRAVE_12','ДВЕ ДАТЫ'),
  text('<small>ПОПОЛНЕНИЕ</small><b>В браслет добавлена третья фигурка</b><span class="stamp">+1</span><em>пример</em>','card'),
  photo('IMG_RINGS_03','ИМЕНА ВНУТРИ КОЛЬЦА'),
  photo('IMG_PILLOW21_08','АРХИВ · 2021'),
  text('<small>ЧТО ГРАВИРУЕМ</small><ol><li>имя</li><li>дату</li><li>время</li><li>рост</li><li>вес</li></ol>','card','car'),
  photo('IMG_ENGRAVE_09','СЕРДЦЕ · ИМЯ'),
  photo('IMG_PILLOW_06','АРХИВ · 2019'),
  text('<small>КАРТОЧКА № 0128</small><dl><dt>Имена</dt><dd>Иван, Мария</dd><dt>Примечание</dt><dd>двойня</dd></dl><span class="stamp">×2</span><em>пример</em>','card'),
  photo('IMG_ENGRAVE_13'),
  photo('IMG_NEW24_02','ПЛАСТИНА'),
  text('<small>ГОД НАЗАД</small><b>Ровно год назад мы сделали этот браслет. С первым днём рождения, Вера!</b><em>пример</em>','card'),
  photo('IMG_ENGRAVE_00'),
  photo('IMG_PILLOW21_05','АРХИВ · 2021'),
  text('<small>ВАША КАРТОЧКА</small><dl><dt>Имя</dt><dd>__________</dd><dt>Время</dt><dd>__________</dd><dt>Рост, вес</dt><dd>__________</dd></dl>','card'),
  photo('IMG_RINGS_05')]))
# ───────────── 5. Гид для пап
C.append(dict(n=5, key='c5', name='Гид для пап', idea='Понятные инструкции для тех, кто дарит: шаги, чек-листы, сроки и бюджет. Оранжевый — как ваша упаковка.',
 pal=['#14213D','#FFFFFF','#F26B2A','#E5E8EF'], fonts='Unbounded · Golos Text',
 avatar='<b class="av-j">J</b><small>гид</small>',
 bio=['<b>Juliette\'s — подарок, который попадёт точно</b>','Как выбрать браслет жене за 5 минут ↓','Срочное изготовление — 4 рабочих дня'],
 cta='Подобрать', hl=[('Ø','Размер'),('Au','Металл'),('4д','Сроки'),('₽','Цены'),('▣','Упаковка')],
 tiles=[
  text('<small>шаг 1</small><b>МЕТАЛЛ</b><span>посмотрите на её кольца</span>','o','car'),
  photo('IMG_PACK_04','Упакуем — дарить можно сразу'),
  text('<small>День матери · 29.11</small><b>21 день</b><span>до праздника</span>','n', chk='сроки заказа сверить'),
  photo('IMG_PUGOVKI_08','«Пуговки» — для пап тоже'),
  text('<small>спросите незаметно</small><ul><li>какой металл</li><li>обхват запястья</li><li>имена и даты</li></ul>','w','car'),
  photo('IMG_ALISANY25_04'),
  text('<small>шаг 2</small><b>ФИГУРКИ</b><span>по одной на каждого ребёнка</span>','o','car'),
  photo('IMG_CROSS23_15','Подарок от вас и детей'),
  text('<b>4 рабочих дня</b><span>срочное изготовление · по сайту</span>','n', chk='доплату сверить'),
  photo('IMG_PACK_01'),
  text('<small>бюджет</small><ul class="pr"><li>серебро <b>от 17 400 ₽</b></li><li>золото <b>от 54 200 ₽</b></li></ul><em>цены сверить</em>','w'),
  photo('IMG_NY22_07','','reel'),
  text('<small>шаг 3</small><b>ГРАВИ&shy;РОВКА</b><span>имена, даты, рост и вес</span>','o','car'),
  photo('IMG_PUGOVKI_09','Себе тоже можно'),
  text('<b>Перешлите пост нам</b><span>— поможем выбрать за 5 минут</span>','n', chk='пример'),
  photo('IMG_ALISANY25_01'),
  text('<small>шаг 4</small><b>РАЗМЕР</b><span>ювелир подскажет, как узнать незаметно</span>','o','car'),
  photo('IMG_PACK_03')]))
# ───────────── 6. Конструктор семьи
eq1 = '<div class="eq">'+mini('IMG_NEW24_07')+'<i>+</i>'+mini('IMG_PILLOW21_05')+'<i>+</i>'+mini('IMG_NEW24_01')+'</div><b>= ваш браслет</b>'
eq2 = '<div class="eq">'+mini('IMG_HEELS22_07')+'<i>+</i>'+mini('IMG_HEELS22_07')+'<i>+</i>'+mini('IMG_HEELS22_07')+'</div><b>= трое</b>'
sk = '<div class="sk"><span class="draw">эскиз</span><i>→</i>'+mini('IMG_PILLOW21_08')+'</div><b>эскиз № 34 → готово</b>'
mos = '<div class="mos">'+mini('IMG_NEW24_00')+mini('IMG_NEW24_03')+mini('IMG_PILLOW_06')+mini('IMG_NEW24_04')+'</div><b>собрано на этой неделе</b>'
C.append(dict(n=6, key='c6', name='Конструктор семьи', idea='Игра в сборку: фигурки, сердца и пяточки как детали. Бесплатный эскиз по слову «ЭСКИЗ».',
 pal=['#F9D5DC','#D9CCF5','#CFEBDF','#FFF0B8','#3A2E5A'], fonts='Comfortaa · Nunito',
 avatar='<b class="av-j">J</b><span class="dots"><i></i><i></i><i></i><i></i></span>',
 bio=['<b>Juliette\'s · собери свою семью</b>','Мальчик + девочка + сердце = ваш браслет','Напишите ЭСКИЗ — нарисуем бесплатно'],
 cta='ЭСКИЗ', hl=[('✎','Эскизы'),('☺','Фигурки'),('♡','Сердца'),('✓','Собрано'),('?','Как заказать')],
 tiles=[
  text(eq1,'eqt pk','pin'),
  photo('IMG_NEW24_00'),
  photo('IMG_NEW24_03'),
  text(sk,'eqt lv','car'),
  photo('IMG_PILLOW_02'),
  text('<div class="bub">ЭСКИЗ</div><b>напишите нам одно слово</b><small>нарисуем ваш браслет бесплатно</small>','eqt mt', chk='условия и срок сверить'),
  photo('IMG_PILLOW_06'),
  photo('IMG_NEW24_04','','reel'),
  photo('IMG_PILLOW21_03','выбери сердце'),
  photo('IMG_PILLOW_08'),
  photo('IMG_NEW24_07'),
  text('<b>Какую деталь добавить?</b><ul class="poll"><li>звезду</li><li>сердце</li><li>пяточку</li></ul>','eqt bt'),
  photo('IMG_PILLOW21_04'),
  photo('IMG_PILLOW_09'),
  text(eq2,'eqt mt'),
  photo('IMG_NEW24_08'),
  photo('IMG_PILLOW21_09','','reel'),
  text(mos,'eqt pk')]))
# ───────────── 7. Письма из студии
C.append(dict(n=7, key='c7', name='Письма из студии', idea='Голос мастерской: раз в неделю письмо от руки, полароиды, сургуч. Личная интонация вместо рекламы.',
 pal=['#F7E8E4','#5A2E3A','#A8323E','#E7C9C0'], fonts='Marck Script · Literata',
 avatar='<b class="av-j">J</b>',
 bio=['<b>Juliette\'s · письма из студии</b>','Раз в неделю пишем о том, что происходит в мастерской','Отвечаем лично — пишите'],
 cta='Написать', hl=[('1','Письмо'),('✦','Мастер'),('✉','Ваши письма'),('✿','Новинки'),('✎','Как работаем')],
 tiles=[
  text('<i class="hand">Дорогие мамы!</i><p>На этой неделе в мастерской пахнет воском и ёлкой — начинаем новогодние заказы.</p><span class="seal">J</span>','let','pin'),
  polar('IMG_ALISA25_00','для Веры',-4, chk='пример'),
  photo('IMG_ALISA25_04'),
  text('<i class="hand">P.S.</i><p>Хотите добавить фигурку? Просто ответьте на это письмо.</p>','let'),
  polar('IMG_ALISA25_13','упаковали',3),
  photo('IMG_ALISA25_06'),
  text('<span class="env"></span><b>Письмо № 7</b><small>о гравировке</small>','envt','car'),
  photo('IMG_ALISA25_14','','reel'),
  polar('IMG_BALLOONS_03','сердце',-2),
  text('<i class="hand">С любовью,</i><p>ваша мастерская Juliette’s</p><span class="seal">J</span>','let'),
  photo('IMG_ALISA25_11'),
  polar('IMG_ALISA25_05','в коробке',4),
  text('<i class="hand">Вопрос недели</i><p>Как ухаживать за серебром? Ответ — в карусели</p>','let','car'),
  photo('IMG_BALLOONS_07'),
  polar('IMG_ALISA25_15','пионы',-3),
  text('<i class="hand">Спасибо,</i><p>что пишете нам. Каждое письмо читаем сами.</p>','let'),
  photo('IMG_ALISA25_07'),
  polar('IMG_BALLOONS_01','на руке',2)]))
# ───────────── 8. Серебро каждый день
C.append(dict(n=8, key='c8', name='Серебро каждый день', idea='Светлый дневной лайфстайл: украшение, которое не снимают. Модели в наличии, понятная цена.',
 pal=['#F4F6F8','#1C2430','#9EC5E8','#C9D1DA'], fonts='Onest',
 avatar='<b class="av-j">J</b>',
 bio=['<b>Juliette\'s · серебро на каждый день</b>','Готовые модели с гравировкой: по Москве 1–3 рабочих дня, регионы — дольше '+mark('по сайту · сверить'),'Серебро 925'],
 cta='В наличии', hl=[('●','В наличии'),('₽','До 25 000'),('◐','На руке'),('✧','Уход'),('★','Отзывы')],
 tiles=[
  photo('IMG_MODEL20_00','серебро 925', chk='металл сверить'),
  photo('IMG_NY21_03','в наличии', chk='наличие сверить'),
  text('<b>Носить.<br>Не снимать.</b>','s1'),
  photo('IMG_HOME_04'),
  photo('IMG_MODEL20_02','','reel'),
  photo('IMG_WHITE_01','в наличии', chk='наличие сверить'),
  text('<small>уход</small><b>3 правила для серебра</b><span>→</span>','s2','car'),
  photo('IMG_HOME_08'),
  photo('IMG_BALLOONS_00'),
  photo('IMG_NY21_08','в наличии', chk='наличие сверить'),
  text('<small>образ дня</small><b>Белая рубашка + браслет с детками</b>','s1'),
  photo('IMG_HOME_02','','reel'),
  photo('IMG_MODEL20_07'),
  photo('IMG_WHITE_03','в наличии', chk='наличие сверить'),
  text('<small>подборка</small><b>Серебро до 25 000 ₽</b><span>→</span>','s2','car'),
  photo('IMG_BALLOONS_04'),
  photo('IMG_HOME_06'),
  photo('IMG_WHITE_09','в наличии', chk='наличие сверить')]))
# ───────────── 9. Три поколения
tree = '<div class="tree">'+mini('IMG_CROSS23_05')+'<i>→</i>'+mini('IMG_FRIENDS20_00')+'<i>→</i>'+mini('IMG_HOME_05')+'</div><b>бабушка · мама · дочь</b>'
C.append(dict(n=9, key='c9', name='Три поколения', idea='Наследство и семейная память: подарки бабушкам с внуками, маме от взрослых детей. Винтажная плёнка.',
 pal=['#E8DFCF','#4A3B2A','#3E5C4A','#C7B79B'], fonts='Yeseva One · Old Standard TT',
 avatar='<b class="av-j">J</b>',
 bio=['<b>Juliette\'s · от бабушки к внукам</b>','Украшения, которые передают по наследству','Браслет бабушке с внуками — в «Подарках»'],
 cta='Подарок', hl=[('IMG_CROSS23_05','Бабушке'),('IMG_NY21_04','Маме'),('IMG_HOME_14','Внукам'),('IMG_FRIENDS20_13','Наследство'),('IMG_NY22_12','Семья')], hlphoto=True,
 tiles=[
  text(tree,'vt','pin', chk='пример'),
  photo('IMG_NY21_04'),
  photo('IMG_CROSS23_05'),
  text('<q>Этот браслет я подарила маме. Теперь на нём её внуки</q><small>пример</small>','vt'),
  photo('IMG_HOME_09','','reel'),
  photo('IMG_FRIENDS20_13'),
  frame('руки бабушки и внучки с браслетом'),
  photo('IMG_NY22_08'),
  text('<b>Подарок бабушке</b><small>фигурки всех внуков на одном браслете</small>','vt','car'),
  photo('IMG_HOME_01'),
  photo('IMG_FRIENDS20_00'),
  photo('IMG_NY22_12'),
  text('<b>Семейная реликвия</b><small>как сохранить золото для внуков</small>','vt','car'),
  photo('IMG_HOME_14'),
  frame('старое семейное фото рядом с браслетом'),
  photo('IMG_FRIENDS20_04'),
  photo('IMG_CROSS23_03'),
  text('<b class="big">1 · 3</b><small>один браслет · три поколения</small>','vt')]))
# ───────────── 10. Ювелирный ликбез
def ann(img, labels, badge='', chk='сверить'):
    USED.add(img)
    ls = ''.join(f'<span class="call" style="top:{t}%;left:{l}%">{e(x)}</span>' for (x,t,l) in labels)
    m = mark(chk) if chk else ''
    return f'<div class="tile ph an"><i class="img {img}"></i>{ls}{BADGE.get(badge,"")}{m}</div>'
C.append(dict(n=10, key='c10', name='Ювелирный ликбез', idea='Экспертный разбор без сложных слов: пробы, камни, родий, из чего складывается цена. Чертёжная сетка и выноски.',
 pal=['#EAF0F7','#0F2A4A','#2F6FE0','#FFE45C'], fonts='Golos Text · JetBrains Mono',
 avatar='<b class="av-j">J</b><small>585 · 925</small>',
 bio=['<b>Juliette\'s · ювелирный ликбез</b>','Пробы, камни, гравировка — без сложных слов','Задайте вопрос — разберём в карусели'],
 cta='Спросить', hl=[('585','Пробы'),('◇','Камни'),('Ab','Гравировка'),('✧','Уход'),('₽','Цена')],
 tiles=[
  text('<b class="big">585</b><span>= 58,5% золота</span><small>остальное — лигатура (серебро, медь и другие металлы): она даёт прочность и цвет</small>','bp','pin'),
  ann('IMG_RINGS_00',[('бриллиант',12,8),('пяточки',70,50)]),
  ann('IMG_RINGS_01',[('аметист',12,8)]),
  text('<small>сравнение</small><table><tr><th></th><th>блеск</th><th>цена</th></tr><tr><td>фианит</td><td>●●○</td><td>₽</td></tr><tr><td>кристалл</td><td>●●○</td><td>₽₽</td></tr><tr><td>бриллиант</td><td>●●●</td><td>₽₽₽</td></tr></table>','bp','car'),
  ann('IMG_ENGRAVE_12',[('гравировка',14,6),('замок',78,52)], chk=''),
  ann('IMG_WHITE_06',[('красное золото',10,6)],'reel'),
  text('<small>родий</small><b>Почему белое золото блестит холодно</b><span>покрытие родием</span>','bp','car'),
  ann('IMG_RINGS_06',[('гранат',12,8)]),
  ann('IMG_PUGOVKI_02',[('серебро 925',12,6)]),
  text('<small>формула цены</small><b>металл + камни + работа + гравировка</b>','bp hl'),
  ann('IMG_RINGS_07',[('камень',12,8)], chk=''),
  ann('IMG_ENGRAVE_09',[('сердце',16,8),('имя',60,46)], chk=''),
  text('<b class="big">925</b><span>= 92,5% серебра</span>','bp'),
  ann('IMG_RINGS_09',[('чёрный бриллиант',12,6)]),
  ann('IMG_WHITE_00',[('серебро',12,6)]),
  text('<small>как проверить</small><b>клеймо пробы + УИН в ГИИС ДМДК</b>','bp','car', chk='УИН на бирке сверить'),
  ann('IMG_RINGS_08',[('аметист',12,8)]),
  ann('IMG_ENGRAVE_13',[('кр. золото',12,6)])]))

def phone(c, tiles, first):
    h = ''
    if first:
        hl = ''
        for a,b in c['hl']:
            if c.get('hlphoto'):
                USED.add(a); inner = f'<i class="img {a}"></i>'
            else: inner = f'<span>{e(a)}</span>'
            hl += f'<div class="hl"><div class="hlc">{inner}</div><small>{e(b)}</small></div>'
        bio = ''.join(f'<p>{x}</p>' for x in c['bio'])
        h = f'''<div class="ig-top"><b>mamy_braslets</b><span class="ig-ic">＋ ☰</span></div>
<div class="prof"><div class="av">{c["avatar"]}</div><div class="st"><div><b>1 284</b><small>публикации</small></div><div><b>30,3K</b><small>подписчики</small></div><div><b>212</b><small>подписки</small></div></div></div>
<div class="bio">{bio}</div>
<div class="btns"><span>Подписаться</span><span>Сообщение</span><span class="cta">{e(c["cta"])}</span></div>
<div class="hls">{hl}</div>
<div class="tabs"><span class="on">▦</span><span>▷</span><span>◫</span></div>'''
    else:
        h = '<div class="ig-top"><b>mamy_braslets</b><span class="ig-ic">‹ прокрутка</span></div>'
    return f'<div class="phone {c["key"]}"><div class="sb"><span>9:41</span><span>●●● ◔</span></div>{h}<div class="grid">{"".join(tiles)}</div></div>'

def logo_block(c):
    hl = ''
    for a,b in c['hl']:
        inner = (f'<i class="img {a}"></i>' if c.get('hlphoto') else f'<span>{e(a)}</span>')
        hl += f'<div class="hl"><div class="hlc">{inner}</div><small>{e(b)}</small></div>'
    sw = ''.join(f'<i style="background:{p}" title="{p}"></i>' for p in c['pal'])
    return f'''<div class="side">
<div class="lg {c["key"]}"><div class="av big">{c["avatar"]}</div><div class="av sm">{c["avatar"]}</div></div>
<div class="cap-s">Логотип-аватар · крупно и в размере ленты</div>
<div class="hlrow {c["key"]}">{hl}</div>
<div class="cap-s">Обложки «Актуального»</div>
<div class="sw">{sw}</div><div class="cap-s">Палитра · шрифты: {e(c["fonts"])}</div></div>'''

nav = ''.join(f'<a href="#k{c["n"]}">{c["n"]}. {e(c["name"])}</a>' for c in C)
secs = ''
for c in C:
    t = c['tiles']
    secs += f'''<section id="k{c["n"]}" class="concept">
<header class="ch"><span class="no">{c["n"]:02d}</span><div><h2>{e(c["name"])}</h2><p>{e(c["idea"])}</p></div></header>
<div class="row">{logo_block(c)}<div class="phones">{phone(c,t[:9],True)}{phone(c,t[9:],False)}</div></div></section>'''

THEME = open(__file__.replace('concepts_v2.py','concepts_v2.css'),encoding='utf-8').read()
imgcss = '\n'.join(f'.{k}{{background-image:url({{{{{k}}}}})}}' for k in sorted(USED))
print(f'''<title>Соцсети Juliette's: 10 концепций</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;700&family=IBM+Plex+Mono:wght@400;600&family=Playfair+Display:ital,wght@0,500;1,400;1,500&family=Lora:ital@0;1&family=Cormorant+Garamond:wght@300;500&family=Jost:wght@300;400&family=PT+Mono&family=PT+Serif:ital,wght@0,400;0,700;1,400&family=Unbounded:wght@600;800&family=Golos+Text:wght@400;600&family=Comfortaa:wght@500;700&family=Nunito:wght@400;700&family=Marck+Script&family=Literata:ital,wght@0,400;1,400&family=Onest:wght@300;400;600&family=Yeseva+One&family=Old+Standard+TT:ital,wght@0,400;1,400&family=JetBrains+Mono:wght@400;600&display=swap">
<style>{THEME}
{imgcss}</style>
<div class="wrap">
<header class="top"><span class="eyebrow">Juliette's jewelry · соцсети · SOC-001 · версия 2</span>
<h1>10 концепций соцсетей: детальная прорисовка</h1>
<p class="lead">Каждая концепция показана как живой профиль Instagram*: логотип-аватар, обложки «Актуального», шапка профиля и две страницы ленты — 18 публикаций. Все фото — из вашей медиатеки (съёмки 2019–2025). Где нужного кадра пока нет, стоит заглушка «кадр: …» — её закроет новый контент 2025–2026, который вы загрузите на диск. Цифры подписчиков и публикаций в шапке — для примера. Цены и сроки сверены с сайтом и материалами студии на 04.11.2026; жёлтая метка «сверить» — факт, который вы подтверждаете до публикации, «пример» — вымышленный текст. Тексты, рубрики, затраты и риски каждой концепции — в первой версии: https://claude.ai/artifact/Jw8647idr3Sy4veFC2bNxJ</p>
<nav class="nav">{nav}</nav></header>
{secs}
<section class="choose"><h2>Как выбрать</h2><p>Ответьте одной строкой: номер концепции или сочетание, например «Соцсети: 1 + 4» или «Соцсети: 6, но в цветах 3». После выбора агент соберёт контент-план и шаблоны по выбранной концепции; публикации стартуют только после вашего «да».</p>
<p class="foot">* Instagram — продукт компании Meta Platforms Inc., деятельность которой запрещена на территории Российской Федерации как экстремистская. Reels — функция Instagram*. Макеты — внутренний документ для выбора концепции. Цитаты, имена и истории с пометкой «пример» вымышлены и к людям на фото отношения не имеют; в реальных публикациях — только дословные отзывы и истории с согласия клиентов. Фото детей и семей — из съёмок бренда: перед каждой реальной публикацией каждого человека на фото сверяем с реестром согласий; фамилию, город и дату рождения ребёнка вместе не публикуем. Сроки — по странице «Доставка и оплата» на сайте; «срочно — 4 рабочих дня» публикуем после того, как вы подтвердите, есть ли доплата.</p></section>
</div>''')
