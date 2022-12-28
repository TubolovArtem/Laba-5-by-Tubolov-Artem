from nasa_api import nasa
from pochta_api import pochta
from weather_api import weather

while True:
    to_do = input('Чтобы узнать погоду, введите weather\n'
                  'Чтобы отследить посылку, введите pochta\n'
                  'Чтобы посмотреть картинку дня от Наса, введите что угодно другое\n'
                  '>>> ')
    if to_do == 'weather':
        weather()
    elif to_do == 'pochta':
        try:
            pochta()
        except Exception as exception:
            print(f'Произошла ошибка: {exception}\n')
    else:
        print('Чтобы потом продолжить выполнение этого скрипта, закройте открывшееся окно\n')
        nasa()
