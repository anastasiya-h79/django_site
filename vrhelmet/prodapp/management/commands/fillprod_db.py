from django.core.management.base import BaseCommand
from prodapp.models import Category, Helmets, Carusel
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.filter(name='автономные VR-шлемы-3').delete()
        Category.objects.filter( name='автономные VR-шлемы-2' ).delete()
        #Helmets.objects.all().delete()
        #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        #categ = Category.objects.create(name='автономные VR-шлемы-3')   #url=os.path.join(BASE_DIR, 'prodapp/templates/prodapp/helmets_category.html')
        # Helmets.objects.create(name='Автономный шлем виртуальной реальности Oculus Go (32 ГБ)',
        #                        description='Oculus Rift GO (32 ГБ) - недорогой способ погружения в VR. Будущее VR за автономными устройствами, которые не требуют подключения к смартфону или компьютеру. Разработчики утверждают, что отсутствие подключения не будет отрицательно сказываться на работе системы. Она будет функционировать так же, как и гарнитуры, работающие в связке с компьютером. Дисплей шлема имеет разрешение 2560х1440 пикселей. Новинка компании нисколько не уступает Oculus Rift по углу обзора, а также прочих визуальных характеристик. В Oculus Go установлены встроенные динамики, которые обеспечивают качественное пространственное звучание, а также присутствует 3,5 мм разъём для использования гарнитуры. В устройстве нет датчиков отслеживания положения тела пользователя и его движений, но вместо этого в комплекте поставляется небольшой и удобный в работе контроллер. Игры и видеоконтент приобретаются отдельно в виртуальном магазине развлечений Oculus Home.',
        #                        price=20700,
        #                        stock='Достаточно',
        #                        guarantee='12 месяцев',
        #                        text='Широкий угол обзора. Качественное пространственное звучание',
        #                        category=categ)
        #
        # Helmets.objects.create(name='Автономный шлем HTC Vive Focus Plus',
        #                        description='Автономный шлем HTC Vive Focus Plus – портативное и мощное многоцелевое устройство, которое идеально подойдет для шоу-румов, VR-конференций и обучающих тренингов. Оборудование выгодно отличается от других VR-шлемов эргономичностью и улучшенной графикой. HTC Vive Focus Plus получил новую систему трекинга – контроллеры с 6 степенями свободы с интуитивно понятным управлением. Более точное взаимодействие с объектами обеспечивается повышенной чувствительностью триггера (отслеживается уровень нажатия). Благодаря новым линзам шлем выдает достаточно реалистичную картинку. По сравнению с базовой версией серьезно улучшилась эргономика, поэтому VR-сеансы станут еще дольше и комфортнее. При производстве шлема используются мягкие и немаркие материалы.',
        #                        price=82900,
        #                        stock='Достаточно',
        #                        guarantee='12 месяцев',
        #                        text='Идеально для шоу-румов, VR конференций и обучающих тренингов',
        #                        category=categ)
        #
        # categ = Category.objects.create(name='VR-шлемы для ПК и консолей')
        # Helmets.objects.create(name='Шлем виртуальной реальности Oculus Rift S',
        #                        description='Шлем виртуальной реальности Oculus Rift S – новое поколение игровых гарнитур на базе ПК. Устройство получило современную оптику, более эргономичный дизайн и высокоточные контроллеры Oculus Touch. Гарнитура Oculus Rift S оснащается новыми линзами и более четким дисплеем. Шлем удобно держится на голове и не слетает даже при резких движениях. Устройство не использует внешние датчики, однако прекрасно отслеживает все перемещения пользователя. Для более глубокого погружения в VR-игры в комплекте идут высокоточные ручные контроллеры. Встроенный в шлем динамик позволяет общаться с напарниками по команде и слышать все звуки окружающего VR-мира. Oculus Rift S 2019 способен запускать все современные игры виртуальной реальности на ПК с самыми различными конфигурациями.',
        #                        price=70900,
        #                        stock='Много',
        #                        guarantee='2 года',
        #                        sale='15',
        #                        text='Новое поколение игровых гарнитур на базе ПК',
        #                        category=categ)
        #
        # Helmets.objects.create(name='Шлем виртуальной реальности HTC Vive',
        #                        description='Шлем виртуальной реальности HTC Vive – это современное устройство, которое позволит насладиться цифровыми мирами крутейших игр! Очки оснащены датчиками отслеживания вашего положения в комнате, а стабилизаторы картинки гарантируют максимально четкое изображение, даже при низком показателе ФПС! HTC Vive VR оснащен встроенным микрофоном, передающим ваш голос без помех, гироскопом, акселерометром и датчиком приближения. Допустимый угол обзора 110 градусов, дисплей с частотой обновления в 90 Гц и разрешением дисплеев для каждого глаза в 1200х1080. Чтобы комфортно работать и играть с очками, вам потребуется соблюдать рекомендуемые системные требования для ПК с процессором i5 4590, видеокартой GTX 1060 или аналогом от AMD, Radeon R9 290 и оперативной памятью не ниже 4 Гб (либо иметь более производительный ПК).',
        #                        price=66900,
        #                        stock='Под заказ',
        #                        guarantee='12 месяцев',
        #                        sale='10',
        #                        text='Максимально четкое изображение, даже при низком ФПС',
        #                        category=categ)


        #Carusel.objects.create(image1=os.path.join(BASE_DIR, 'media/carusel/image4.jpeg'),
        # (image2=os.path.join(BASE_DIR, 'media/carusel/11_oPY6oTs_9ORUXiF'),
                               #image3=os.path.join(BASE_DIR, 'media/carusel/image2.jpeg'))
        # categ = Category.objects.create(
        #     name='очки смешанной реальности' )  # url=os.path.join(BASE_DIR, 'prodapp/templates/prodapp/helmets_category.html')
        # Helmets.objects.create( name='Magic Leap One Personal Bundle',
        #                         description='Комплект Magic Leap для личного пользования – это новинка в мире дополненной и смешанной реальности. Очки компактны, весят намного меньше шлемов виртуальной реальности, поэтому очень удобны в использовании. Посредством функционирования фотоников генерируется свет на разных глубинах, благодаря чему создаются реалистичные цифровые объекты. Уникальный набор датчиков на Magic Leap One Personal Bundle обнаруживает поверхности, плоскости и объекты, что позволяет проводить цифровую реконструкцию физического окружения. Результатом является параллельное существование двух миров: физического и виртуального. Устройство предоставляет уникальные возможности для пространственных вычислений и сканирования пространства. Специальная технология маппинга создаёт качественную цифровую копию окружающей физической среды. Сенсоры обнаруживают и сохраняют предельно точное расположение стен, поверхностей и прочих объектов.',
        #                         price=299990,
        #                         stock='На заказ',
        #                         guarantee='3 года',
        #                         text='Очки компактны, весят намного меньше шлемов виртуальной реальности,',
        #                         category=categ )
        #
        # Helmets.objects.create( name='Шлем смешанной реальности Samsung HMD Odyssey Plus',
        #                         description='Шлем HMD Odyssey+ оснащён продвинутой системой АKG Premium Аudio. Она характеризуется отличным уровнем звучания, работой встроенных микрофонов и позволяет полностью погрузиться в игровой процесс. Добавьте к этому отличную периферию, гироскоп, сенсор приближения, две камеры Windows MR Cаmerа, акселерометр, и вы получите устройство для получения наслаждения от виртуальной реальности. Настройка работы шлема занимает несколько минут: достаточно подключиться к совместимому компьютеру. Вы можете загружать приложения и игры из магазина Microsoft и SteаmVRLibrаry, чтобы исследовать ещё больше миров.',
        #                         price=48990,
        #                         stock='Достаточно',
        #                         guarantee='12 месяцев',
        #                         text='Шлем HMD Odyssey+ оснащён продвинутой системой АKG Premium Аudio',
        #                         category=categ )
        # Helmets.objects.create( name='Очки смешанной реальности Dell Windows Mixed Reality',
        #                         description='Dell Windows Mixed Reality - это классического вида гарнитура гибридной реальности. Шлем довольно элегантный и эстетически совершенен и имеет хорошее преимущество в условиях длительной эксплуатации. Конструкция шлема довольно удобна, разработчики позаботились о распределении массы шлема для комфортного пребывания в нем, так же он имеет мягкие подушечки там, где соприкасается с головой и присутствует кабельный канал для проводов.',
        #                         price=41600,
        #                         stock='Достаточно',
        #                         guarantee='12 месяцев',
        #                         text='Шлем довольно элегантный и имеет хорошее преимущество в условиях длительной эксплуатации',
        #                         category=categ )
        # Helmets.objects.create( name='Очки смешанной реальности HP Windows Mixed Reality',
        #                         description='Шлем HP Windows Mixed Reality — пропуск к миру новых ощущений видеоигр, позволяющий получить уникальный опыт погружения в виртуальную реальность. Очки не слишком требовательны к ресурсам современного компьютера и их приобретение доступно для домашнего, демонстрационного и массово-развлекательного использования. Основная настройка устройства при подключении производится автоматически. Корпус устройства выполнен в темном минималистичном дизайне с гладкими формами. Эргономика гарнитуры заключается в наличии внутреннего мягкого покрытия, смягчающего контакт с лицом, форменной полости для носа и удобной регулировке положения с помощью фиксирующих ремней. Это позволяет каждому пользователю настроить прибор под себя. За безопасность применения на игровой площадке отвечают внешние датчики трекинга, которые следят за тем, чтобы игрок не вышел из обозначенной зоны.',
        #                         price=49900,
        #                         stock='Достаточно',
        #                         guarantee='12 месяцев',
        #                         text='Позволяют получить уникальный опыт погружения в виртуальную реальность',
        #                         category=categ )
        #
        # Helmets.objects.create( name='Комплект HTC Vive Pro с базовыми станциями и контроллерами Steam VR Tracking 2.0',
        #                         description='Комплект HTC Vive Pro: уникальный комплект для VR погружения – это набор устройств виртуальной реальности с новейшим технологичным шлемом HTC Vive PRO. С помощью этого комплекта Вы можете без лишних затрат и покупки дополнительного оборудования полноценно пользоваться VR шлемом. Комплект HTC Vive Pro состоит из нескольких частей: шлема, контроллеров и базовых станций. Вкупе они обеспечивают комфортное и беспроблемное использование приложений и игр виртуальной реальности.',
        #                         price=114890,
        #                         stock='На заказ',
        #                         guarantee='2 года',
        #                         text='Набор vr-устройств с новейшим технологичным шлемом HTC Vive PRO',
        #                         category=categ )
        #
        # Helmets.objects.create( name='Шлем виртуальной реальности Vive Cosmos',
        #                         description='HTC Vive Cosmos – новая гарнитура от известного тайваньского бренда HTC со встроенными камерами и повышенной комфортностью. Устройство работает со стационарными компьютерами и ноутбуками VR Ready. Компания HTC позиционирует новые очки виртуальной реальности Vive Cosmos как новый шаг во всей отрасли - это очки с самым высоким разрешением изображения из линейки шлемов Vive на конец 2019г. и встроенными 6-ью камерами в шлем. Шлем полностью готов к работе прямо из коробки и не требует дополнительных настроек.',
        #                         price=69900,
        #                         stock='Достаточно',
        #                         guarantee='12 месяцев',
        #                         text='Новая гарнитура со встроенными камерами и повышенной комфортностью',
        #                         category=categ )

