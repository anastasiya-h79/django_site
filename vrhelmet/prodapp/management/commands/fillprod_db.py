from django.core.management.base import BaseCommand
from prodapp.models import Category, Helmets, Carusel
import os




class Command(BaseCommand):

    def handle(self, *args, **options):
        #Category.objects.all().delete()
        #Helmets.objects.all().delete()
        #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        categ = Category.objects.create(name='автономные VR-шлемы')   #url=os.path.join(BASE_DIR, 'prodapp/templates/prodapp/helmets_category.html')
        #
        # Helmets.objects.create(name='Автономный шлем виртуальной реальности Oculus Go (32 ГБ)',
        #                        description='Oculus Rift GO (32 ГБ) - недорогой способ погружения в VR. Будущее VR за автономными устройствами, которые не требуют подключения к смартфону или компьютеру. Разработчики утверждают, что отсутствие подключения не будет отрицательно сказываться на работе системы. Она будет функционировать так же, как и гарнитуры, работающие в связке с компьютером. Дисплей шлема имеет разрешение 2560х1440 пикселей. Новинка компании нисколько не уступает Oculus Rift по углу обзора, а также прочих визуальных характеристик. В Oculus Go установлены встроенные динамики, которые обеспечивают качественное пространственное звучание, а также присутствует 3,5 мм разъём для использования гарнитуры. В устройстве нет датчиков отслеживания положения тела пользователя и его движений, но вместо этого в комплекте поставляется небольшой и удобный в работе контроллер. Игры и видеоконтент приобретаются отдельно в виртуальном магазине развлечений Oculus Home.',
        #                        price='20 700р',
        #                        stock='Достаточно',
        #                        guarantee='12 месяцев',
        #                        text='Широкий угол обзора. Качественное пространственное звучание',
        #
        #                        category=categ)
        #
        # Helmets.objects.create(name='Автономный шлем HTC Vive Focus Plus',
        #                        description='Автономный шлем HTC Vive Focus Plus – портативное и мощное многоцелевое устройство, которое идеально подойдет для шоу-румов, VR-конференций и обучающих тренингов. Оборудование выгодно отличается от других VR-шлемов эргономичностью и улучшенной графикой. HTC Vive Focus Plus получил новую систему трекинга – контроллеры с 6 степенями свободы с интуитивно понятным управлением. Более точное взаимодействие с объектами обеспечивается повышенной чувствительностью триггера (отслеживается уровень нажатия). Благодаря новым линзам шлем выдает достаточно реалистичную картинку. По сравнению с базовой версией серьезно улучшилась эргономика, поэтому VR-сеансы станут еще дольше и комфортнее. При производстве шлема используются мягкие и немаркие материалы.',
        #                        price='82 900р',
        #                        stock='Достаточно',
        #                        guarantee='12 месяцев',
        #                        text='Идеально для шоу-румов, VR конференций и обучающих тренингов',
        #
        #                        category=categ)
        #
        categ = Category.objects.create(name='VR-шлемы для ПК и консолей')
        # Helmets.objects.create(name='Шлем виртуальной реальности Oculus Rift S',
        #                        description='Шлем виртуальной реальности Oculus Rift S – новое поколение игровых гарнитур на базе ПК. Устройство получило современную оптику, более эргономичный дизайн и высокоточные контроллеры Oculus Touch. Гарнитура Oculus Rift S оснащается новыми линзами и более четким дисплеем. Шлем удобно держится на голове и не слетает даже при резких движениях. Устройство не использует внешние датчики, однако прекрасно отслеживает все перемещения пользователя. Для более глубокого погружения в VR-игры в комплекте идут высокоточные ручные контроллеры. Встроенный в шлем динамик позволяет общаться с напарниками по команде и слышать все звуки окружающего VR-мира. Oculus Rift S 2019 способен запускать все современные игры виртуальной реальности на ПК с самыми различными конфигурациями.',
        #                        price='70 900р',
        #                        stock='Много',
        #                        guarantee='2 года',
        #                        sale='15%',
        #                        text='Новое поколение игровых гарнитур на базе ПК',
        #                        category=categ)
        #
        # Helmets.objects.create(name='Шлем виртуальной реальности HTC Vive',
        #                        description='Шлем виртуальной реальности HTC Vive – это современное устройство, которое позволит насладиться цифровыми мирами крутейших игр! Очки оснащены датчиками отслеживания вашего положения в комнате, а стабилизаторы картинки гарантируют максимально четкое изображение, даже при низком показателе ФПС! HTC Vive VR оснащен встроенным микрофоном, передающим ваш голос без помех, гироскопом, акселерометром и датчиком приближения. Допустимый угол обзора 110 градусов, дисплей с частотой обновления в 90 Гц и разрешением дисплеев для каждого глаза в 1200х1080. Чтобы комфортно работать и играть с очками, вам потребуется соблюдать рекомендуемые системные требования для ПК с процессором i5 4590, видеокартой GTX 1060 или аналогом от AMD, Radeon R9 290 и оперативной памятью не ниже 4 Гб (либо иметь более производительный ПК).',
        #                        price='66 900р',
        #                        stock='Под заказ',
        #                        guarantee='12 месяцев',
        #                        sale='10%',
        #                        text='Максимально четкое изображение, даже при низком ФПС',
        #                        category=categ)

        # Carusel.objects.create(image1 = os.path.join(BASE_DIR, 'media/carusel/11.jpeg'),
        #                        image2 = os.path.join(BASE_DIR, 'media/carusel/123.jpg'),
        #                        image3 = os.path.join(BASE_DIR, 'media/carusel/124.jpg'))

