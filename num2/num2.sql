-- СУБД: MS SQL SERVER
-- ---------------------------------------------------------------------------------------
-- Напишите SQL-запрос, который вернет список категорий проданных товаров со
-- стоимостью продаж более 150 000 рублей за последний год. Полученная выборка
-- должна быть отсортирована по доходу, и включать название категории и сам размер дохода.
-- ---------------------------------------------------------------------------------------

SELECT c.name, SUM(p.price * i.quantity) as [Доход]
FROM orders o inner join order_items i on o.ord_id = i.ord_id
			  inner join products p on p.prod_id = i.product_id
			  inner join categories c on p.cat_id = c.cat_id
WHERE YEAR(o.ordered_at) = YEAR(GETDATE()) and
	  o.status = 'done'
GROUP BY c.name
HAVING SUM(p.price * i.quantity) > 150000
ORDER BY [Доход] ASC

