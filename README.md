# Тестовое задание на должность стажера Аналитик-проектировщик
## Задание 1

Рис.1 Физическая модель данных (Нотация Crow’s foot):

Таблица 1. Описание сущностей.

| № п/п | Название сущности | Описание          |
|:---:|:-------------------:|:------------------|
| 1 | Client	            | Человек, который берет заем в банке | 
| 2 | Client_passport	    | Информация о паспортных данных клиента | 
| 3 | Client_job        	| Информация о месте работы клиента | 
| 4 | Client_Application	| Вспомогательная таблица, связывающая id заявки с id клиента. (Показывает то, какие заявки какой клиент оставлял) | 
| 5 | Application	        | Заявка на получение кредита | 
| 6 | Application_Service	| Вспомогательная таблица, связывающая id заявки с id доп. услуги. (Показывает какие доп. услуги включены в данную заявку) | 
| 7 | Extra_Service	      | Дополнительные услуги | 
| 8 | Credit_Product	    | Кредитные продукты | 
| 9 | Loan_Purpose	      | Цель кредита | 


### Описание атрибутов каждой сущности, описание доменов, которым принадлежат атрибуты сущностей, с указанием ограничений на возможные значения

Таблица 2. Описание атрибутов.

| № п/п | Название сущности | Атрибут   | Описание |
|:-:|:-------------------:|:------------:|:-------------|
| 1 | Client	            | client_id  | **Идентификатор** <br/> Тип данных: UUID  <br/> Пример: ‘a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11’ <br/> Ограничения: PRIMARY KEY | 
|   |                     | Name       | Тип данных: varchar(50) <br/> Пример: ‘Иван’ <br/> Ограничения: NOT NULL                  |
|   |                     | Surname    | Тип данных: varchar(50) <br/> Пример: ‘Петров’ <br/> Ограничения: NOT NULL                |
|   |                     | Patronymic | Тип данных: varchar(50) <br/> Пример: ‘Иванович’ <br/> Ограничения: NOT NULL             |
|   |                     | Phone_main | Тип данных: varchar(16) <br/> Пример: ‘+7(901)230-12-20’ <br/> Ограничения: NOT NULL, UNIQUE|
|   |                     | Phone_add  | Тип данных: varchar(16) <br/> Пример: ‘+7-912-345-6780’ <br/>                             |
|   |                     | Email      | Тип данных: varchar(50) <br/> Пример: ‘peson.mail@gmail.com’ <br/> Ограничения: NOT NULL,UNIQUE   |
| 2 | Client_passport	    | client_id           | **Идентификатор** <br/> Тип данных: UUID  <br/> Пример: ‘a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11’ <br/> Ограничения: PRIMARY KEY, FOREIGN KEY |
|   |                     | Series              | Тип данных: varchar(4) <br/> Пример: ‘1945’ <br/> Ограничения:  PRIMARY KEY |
|   |                     | Number              | Тип данных: varchar(6) <br/> Пример: ‘300122’ <br/> Ограничения:  PRIMARY KEY |
|   |                     | Issue_Date          | Тип данных: date <br/> Пример: ‘2020-02-01’ <br/> Ограничения: NOT NULL    |
|   |                     | Department_Code     | Тип данных: varchar(7) <br/> Пример: ‘123-012’ <br/> Ограничения: NOT NULL |
|   |                     | Issued_by           |Тип данных: varchar(255) <br/> Пример: ‘УФМС’ <br/> Ограничения: NOT NULL   |
|   |                     | Bitrh_Date          | Тип данных: date <br/> Пример: ‘1990-01-01’ <br/> Ограничения: NOT NULL    |
|   |                     | Birth_Place         | Тип данных: varchar(255) <br/> Пример: ‘Новосибирск’ <br/> Ограничения: NOT NULL |
|   |                     | Registration_Region | Тип данных: varchar(255) <br/> Пример: ‘Новосибирская область’ <br/> Ограничения: NOT NULL |
| 3 | Client_job        	| client_id         | **Идентификатор** <br/> Тип данных: UUID  <br/> Пример: ‘a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11’ <br/> Ограничения: PRIMARY KEY, FOREIGN KEY |
|   |                     | Region            | Тип данных: varchar(255) <br/> Пример: ‘Новосибирская область’ <br/> Ограничения: NOT NULL |
|   |                     | Organization_Name | Тип данных: varchar(255) <br/> Пример: ‘ООО "Рога и Копыта"’ <br/> Ограничения: NOT NULL  |
|   |                     | INN               | Тип данных: varchar(12) <br/> Пример: ‘7149913174’ <br/> Ограничения: NOT NULL             |
|   |                     | Position_Name     | Тип данных: varchar(50) <br/> Пример: ‘Специалист’ <br/> Ограничения: NOT NULL             |
|   |                     | Salary            | Тип данных: float <br/> Пример: ‘35000.00’ <br/> Ограничения: NOT NULL                     |
|   |                     | Start_Date        | Тип данных: date <br/> Пример: ‘2019-01-01’ <br/> Ограничения: NOT NULL                    |
| 4 | Application	        | application_id | **Идентификатор** <br/> Тип данных: UUID  <br/> Пример: ‘a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11’ <br/> Ограничения: PRIMARY KEY |
|   |                     | Product_Type   | Тип данных: varchar(255) <br/> Пример: ‘Кредит наличными’ <br/> Ограничения: NOT NULL, FOREIGN KEY |
|   |                     | Loan_Purpose   | Тип данных: varchar(255) <br/> Пример: ‘Покупка товаров/услуг’ <br/> Ограничения: FOREIGN KEY |
|   |                     | Amount         | Тип данных: float <br/> Пример: ‘100000.00’ <br/> Ограничения: NOT NULL |
|   |                     | Bet_Size       | Тип данных: float <br/> Пример: ‘7.70’ <br/> Ограничения: NOT NULL, Значение в диапазоне (0,100)|
|   |                     | Loan_Period    | Тип данных: integer <br/> Пример: ‘36’ <br/> Ограничения: NOT NULL |
|   |                     | Total_Sum      | Тип данных: float <br/> Пример: ‘140000.00’ <br/> Ограничения: NOT NULL |
| 5 | Application_Service | service_id     | **Идентификатор** <br/> Тип данных: UUID  <br/> Пример: ‘a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11’ <br/> Ограничения: PRIMARY KEY, FOREIGN KEY |
|   |                     | application_id | **Идентификатор** <br/> Тип данных: UUID  <br/> Пример: ‘a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11’ <br/> Ограничения: PRIMARY KEY, FOREIGN KEY |
|   |                     | Price          | Тип данных: float <br/> Пример: ‘25000.00’ <br/> Ограничения: NOT NULL |
| 6 | Extra_Service	      | service_id   | **Идентификатор** <br/> Тип данных: UUID  <br/> Пример: ‘a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11’ <br/> Ограничения: PRIMARY KEY |
|   |                     | Service_Type | Тип данных: varchar(255) <br/> Пример: ‘Страхование жизни’ <br/> Ограничения: NOT NULL |
|   |                     | Price        | Тип данных: float <br/> Пример: ‘25000.00’ <br/> Ограничения: NOT NULL |

| 7 | Credit_Product	    | Product_Type | Тип данных: varchar(255) <br/> Пример: ‘Кредит наличными’ <br/> Ограничения: NOT NULL  |
|   |                     | Bet_Size     | Тип данных: float <br/> Пример: ‘7.70’ <br/> Ограничения: NOT NULL, Значение в диапазоне (0,100)|
|   |                     | Information  | Тип данных: varchar(255) <br/> Пример: ‘Информация о продукте’ <br/> |
| 8 | Loan_Purpose	      | Loan_Purpose | **Идентификатор** <br/> Тип данных: varchar(255) <br/> Пример: ‘Покупка товаров/услуг’ <br/> Ограничения: PRIMARY KEY|
