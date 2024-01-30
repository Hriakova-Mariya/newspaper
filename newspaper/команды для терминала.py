from news.models import *
# объявление пользователей
u1=User.objects.create_user(username='Иван Петров')
u2=User.objects.create_user(username='Инна Горина')
# создание авторов
Author.objects.create(author=u1)
Author.objects.create(author=u2)

# создание категорий
Category.objects.create(name='Sport')
Category.objects.create(name='Politics')
Category.objects.create(name='Education')
Category.objects.create(name='Medicine')

# 1й пост и присвоение ему категорий
Post.objects.create(author=Author.objects.get(id=1), title='Революция в спорте: будущее за метавселенными', text='Спорт всегда был неотъемлемой частью жизни человечества, объединяя людей разных возрастов и социальных слоев. Но с развитием технологий и появлением метавселенных, спорт претерпевает кардинальные изменения, которые могут привести к революционному прорыву в этой сфере. В данной статье мы рассмотрим, как метавселенные могут изменить спорт, какие возможности они открывают и какие вызовы встают перед профессионалами и любителями спорта. Метавселенные и спорт: новые возможности    Виртуальная реальность и дополненная реальность: Метавселенные открывают новые перспективы для виртуального спорта. Игроки смогут соревноваться в виртуальных играх и турнирах, используя технологии виртуальной и дополненной реальности.    Интерактивность и геймификация: Метавселенные позволяют сделать спорт более интерактивным, создавая игровую атмосферу и стимулируя взаимодействие между участниками.    Обучение и развитие: Технологии метавселенных позволят тренерам и спортсменам разрабатывать и тестировать новые методики обучения и тренировок, а также проводить анализ спортивных результатов.    Вовлечение болельщиков: Метавселенные предоставляют возможность болельщикам стать частью спортивных событий, участвовать в голосовании, делать ставки на результаты и даже принимать участие в соревнованиях.')
Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
Post.objects.get(id=1).postCategory.add(Category.objects.get(id=3))
Post.objects.get(id=1).postCategory.add(Category.objects.get(id=4))
# комментарий к 1 посту
Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).author, text='у метавселенных есть и свои недостатки. Например, виртуальная реальность может создавать иллюзию безопасности, которая может привести к снижению уровня физической активности и ухудшению здоровья. Кроме того, использование метавселенных может увеличить разрыв между теми, кто имеет доступ к новым технологиям, и теми, кто его не имеет. Также существуют опасения по поводу возможного негативного влияния на окружающую среду из-за использования новых технологий.')

# 2й пост и категории
Post.objects.create(author=Author.objects.get(id=2), categoryType='NW', title='МИД Казахстана после слов Канделаки про русский язык позвал ее посетить страну', text='«Пусть приедут в нашу страну и посмотрят, как мы живем. Чем выдумывать какие-то темы и вступать в конфликты в социальных сетях, лучше давайте продолжим нашу общую работу», - отметил Айбек Смадияров')
Post.objects.get(id=2).postCategory.add(Category.objects.get(id=2))
Post.objects.get(id=2).postCategory.add(Category.objects.get(id=3))
#комментарий ко 2му посту
Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=1).author, text='Смадияров какой-то странный. Вначале приглашает Канделаки посетить Казахстан и тут же говорит, что надо запретить ей въезд.')

# 3й пост и категории
Post.objects.create(author=Author.objects.get(id=1), title='Пломбирование в стоматологии', text='Пломбирование в стоматологии - это процесс установки пломбы на зуб, чтобы закрыть полость или отверстие, которое может образоваться в результате кариеса или другой проблемы. Пломбы могут быть изготовлены из различных материалов, таких как цемент, композит или амальгама, и они служат для защиты зуба от дальнейшего разрушения и восстановления его формы и функции.    В зависимости от материала, из которого изготовлена пломба, она может иметь различные свойства и особенности. Например, цементные пломбы являются наиболее доступными и долговечными, но они могут быть менее эстетичными, чем другие типы пломб. Композитные пломбы обладают высокой прочностью и устойчивостью к износу, а также могут быть легко адаптированы к форме и цвету зуба. Амальгамные пломбы содержат металл, который обеспечивает высокую прочность и долговечность, но они также могут вызывать некоторые побочные эффекты, такие как аллергические реакции.     Выбор типа пломбы зависит от многих факторов, включая состояние зуба, предпочтения пациентаи доступность различных материалов. Врач-стоматолог может порекомендовать наиболее подходящий тип пломбы для каждого конкретного случая.    Процесс установки пломбы может включать в себя несколько этапов. Сначала врач проводит осмотр и диагностику зуба, чтобы определить, требуется ли пломбирование. Затем он проводит очистку зуба и удаляет пораженные ткани, если это необходимо. После этого он подготавливает полость зуба и устанавливает пломбу, которая может быть изготовлена заранее или непосредственно во время процедуры. В завершение врач полирует пломбу и дает пациенту рекомендации по уходу за зубами и пломбами.')
Post.objects.get(id=3).postCategory.add(Category.objects.get(id=3))
Post.objects.get(id=3).postCategory.add(Category.objects.get(id=4))
# комментарии к 3му посту
Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=2).author, text='Недолговечны эти пломбы, лучше протез')
Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=1).author, text='Зато дешевле!')

# Создание рейтинга
Post.objects.get(id=1).like()
Post.objects.get(id=1).like()
Post.objects.get(id=1).like()
Post.objects.get(id=1).like()
Post.objects.get(id=2).like()
Post.objects.get(id=2).like()
Post.objects.get(id=2).dislike()
Post.objects.get(id=3).like()
Post.objects.get(id=3).like()
Comment.objects.get(id=1).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).dislike()
Comment.objects.get(id=4).like()
Comment.objects.get(id=4).like()

# Обновление рейтинга пользователей
Author.objects.get(id=1).update_rating()
Author.objects.get(id=2).update_rating()

# вывод данных
first_author=Author.objects.order_by('-rating_author')[:1]
for i in first_author:
    i.author.username
    i.rating_author

best_post=Post.objects.order_by('-rating')[:1]
for i in best_post:
    i.dateCreation
    i.author.author.username
    i.rating
    i.title
    i.preview()

comment=Comment.objects.filter(commentPost=best_post)
for i in comment:
    i.dateCreation
    i.commentUser.username
    i.rating
    i.text
