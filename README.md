# Система электронного документооборота для ДТ "Кванториум Саров"


*Автор:* Кванториум Саров(Дата-квантум)

*Создан:* 27/02/2023

*Версия:* 1.0.0

*О проекте:* На этом сервисе пользователи смогут загружать, редактировать, удалять, 
подписывать документы. Будут иметь возможность обмениваться личными и групповыми сообщениями.
А также смогут просматривать список персонала и работать с мероприятиями.
***
## Оглавление
1. Документ
2. Главная страница
3. Страница пользователя
4. Страница документа
5. Подпись документа
6. Сообщения
7. Уведомления
8. Регистрация и вторизация
9. Что могут делать авторизированные пользователи
10. Что может делать администратор
***
## 1. Документ
Документ может быть загружен, заполнив следующие поля:

* Автор документа
* Кто увидит данный документ
* Кто должен его подписать

Все поля обязательны для заполнения
***
##2. Главная страница
Страница доступна только авторизированным пользователям.

Содержимое главной страницы:
* Список первых 10 документов, отсортированных по дате добавления(от новых к старым). 
Остальные документы доступны на следующих страницах: внизу страницы есть навигация по страницам.

* В левом краю страницы есть блок с графами:
    * Все документы
    * Мои документы
    * Отчёты
    * Мероприятия
    * Персонал
* В шапке сайта - логотип с названием квантума(для наставников), логотип кванториум(для остальных работников).
Поисковая строка.Вкладка сообщения, уведомления.
* В подвале сайта - Уменьшенный логотип. Адрес. Контакты.
***
## 3. Страница пользователя
Страница доступна только авторизированным пользователям.

На странице - имя пользователя, должность, контакты, возможность отправить пользователю сообщение.

## 4. Страница документа
Страница доступна только авторизированным пользователям.

На странице - документ в уменьшенном формате, кнопка "Скачать", кнопка "Подписать".
***
## 5. Подпись документа
Подпись документа доступна только авторизированному пользователю.

Сценарий поведения пользователя: пользователь переходит на страницу документа, нажимает кнопку "Подписать", и 
документ автоматически отправляется администратору.

Документ скачивается в форматах: txt, pdf, docx, doc
***
## 6. Сообщения
Страница доступна только авторизированным пользователям.

На странице - список чатов. 

Возможность начать новую переписку, выбрав сотрудника. 

Возможность создать групповой чат.
***
## 7. Уведомления
Страница доступна только авторизированным пользователям.

На странице - список уведомлений(добавление/изменение документа, добавление/изменение мероприятия, добавление/изменение
персонала).
***
## 8. Регистрация и авторизация
Зарегистрироваться могут только сотрудники ДТ "Кванториум"

Обязательные поля для пользователей:
* Фамилия
* Имя
* Отчество
* Email
* Телефон
* Должность
* Логин
* Пароль

Уровни доступа:
* Авторизированный пользователь
* Администратор
***
## 9. Что могут делать авторизированные пользователи
* Входить в систему под своим логином и паролем
* Выходить из системы
* Менять свой пароль
* Добавлять/редактировать/удалять собственные документы
* Просматривать документы на главной
* Просматривать страницы сотрудников
* Подписывать документ
* Скачивать документ
* Обменивать сообщениями
* Получать уведомления
* Просматривать список мероприятий, добавлять новые
***
## 10. Что может делать администратор
Администратор обладает всеми правами авторизированного пользователя.

Доп. права:
* Создавать/блокировать/удалять аккаунты пользователей
* Редактировать/удалять любые документы/мероприятия/отчёты
