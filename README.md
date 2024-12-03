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
|:-:|:-------------------:|:------------|:-------------|
| 1 | Client	            | client_id  | **Идентификатор** <br/> Тип данных: UUID  <br/> Пример: ‘a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11’ <br/> Ограничение на возможные значения: Обязательный атрибут 
| 
|   |                     | Name       | |
|   |                     | Surname    | |
|   |                     | Patronymic | |
|   |                     | Phone_main | |
|   |                     | Phone_add  | |
|   |                     | Email      | |
| 2 | Client_passport	    | client_id           | |
|   |                     | Series              | |
|   |                     | Number              | |
|   |                     | Issue_Date          | |
|   |                     | Department_Code     | |
|   |                     | Issued_by           | |
|   |                     | Bitrh_Date          | |
|   |                     | Birth_Place         | |
|   |                     | Registration_Region | |
| 3 | Client_job        	| client_id         | |
|   |                     | Region            | |
|   |                     | Organization_Name | |
|   |                     | INN               | |
|   |                     | Position_Name     | |
|   |                     | Salary            | |
|   |                     | Start_Date        | |
| 4 | Application	        | application_id | |
|   |                     | Product_Type   | |
|   |                     | Loan_Purpose   | |
|   |                     | Amount         | |
|   |                     | Bet_Size       | |
|   |                     | Loan_Period    | |
|   |                     | Total_Sum      | |
| 5 | Application_Service | service_id     | |
|   |                     | application_id | |
|   |                     | Price          | |
| 6 | Extra_Service	      | service_id   | |
|   |                     | Service_Type | |
|   |                     | Price        | |
| 7 | Credit_Product	    | Product_Type | |
|   |                     | Bet_Size     | |
|   |                     | Information  | |
| 8 | Loan_Purpose	      | Loan_Purpose | |
