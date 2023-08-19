# API аутентификации по номеру телефона

Этот проект реализует аутентификацию по номеру телефона с следующей функциональностью:

- Пользователи могут аутентифицироваться, используя свой номер телефона и получить код подтверждения.
- Пользователи могут ввести код подтверждения для аутентификации.
- Пользователи сохраняются в базе данных, если они ранее не аутентифицировались.
- Пользователям присваивается случайно сгенерированный 6-символьный инвайт-код при первой аутентификации.
- Пользователи могут ввести инвайт-код другого пользователя в своем профиле, и только один инвайт-код может быть активирован у каждого пользователя.
- API профиля пользователя отображает список пользователей (номеров телефона), которые ввели инвайт-код текущего пользователя.

## API-эндпоинты

### Аутентификация по номеру телефона (Первый запрос)

- **Эндпоинт**: `/api/auth/`
- **Метод**: POST
- **Описание**: Инициирует аутентификацию по номеру телефона и отправляет код подтверждения.
- **Тело запроса**:
  ```json
  {
    "phone_number": "номер_телефона_пользователя"
  }
  ```
- **Ответ**: 200 OK

### Проверка кода подтверждения (Второй запрос)

- **Эндпоинт**: `/api/verify_code/`
- **Метод**: POST
- **Описание**: Проверяет введенный код подтверждения.
- **Тело запроса**:
  ```json
  {
    "phone_number": "номер_телефона_пользователя",
    "verification_code": "код_подтверждения_пользователя"
  }
  ```
- **Ответ**:
  - 200 OK с данными профиля пользователя при успешной проверке
  - 400 Bad Request при ошибке проверки

### Добавление инвайт-кода

- **Эндпоинт**: `/api/add_invitation/`
- **Метод**: POST
- **Описание**: Позволяет пользователям добавить инвайт-код другого пользователя.
- **Тело запроса**:
  ```json
  {
    "invitation_code": "инвайт_код_для_добавления",
    "phone_number": "номер_телефона_пользователя"
  }
  ```
- **Ответ**:
  - 200 OK при успешном добавлении инвайт-кода
  - 400 Bad Request при ошибке добавления

### Профиль пользователя

- **Эндпоинт**: `/api/profile/`
- **Метод**: GET
- **Описание**: Получает информацию о профиле пользователя.
- **Параметры запроса**:
  - `phone_number`: Номер телефона пользователя
  - `login_code`: Код подтверждения пользователя
- **Ответ**:
  - 200 OK с данными профиля пользователя при совпадении кода подтверждения
  - 400 Bad Request при неправильном коде подтверждения

## Интерфейс на Django Templates
- **Эндпоинт**: `/`

## Использование

1. Установите зависимости проекта:

   ```bash
   pip install -r requirements.txt
   ```

2. Запустите сервер разработки Django:

   ```bash
   python manage.py runserver
   ```
    Или через docker 
    ```bash
    docker-compose build
    docker-compose up
   ```

## Коллекция Postman

Для удобного тестирования доступна коллекция Postman с запросами для всех API. Вы можете импортировать ее в Postman, следуя этим шагам:

1. Откройте Postman.
2. Нажмите кнопку "Import".
3. Загрузите предоставленный файл с коллекцией Postman.

В коллекции будут предварительно настроены запросы для каждого из эндпоинтов API.

http://adelashkurtaj.pythonanywhere.com/ 