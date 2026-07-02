# Write your MySQL query statement below
WITH TotalBought AS (
    SELECT stock_name, SUM(price) AS spent
    FROM Stocks
    WHERE operation = 'Buy'
    GROUP BY stock_name
),
TotalSold AS (
    SELECT stock_name , SUM(price) AS gained
    FROM Stocks
    WHERE operation = 'Sell'
    GROUP BY stock_name
)

SELECT B.stock_name, gained - spent AS capital_gain_loss
FROM TotalBought AS B
JOIN TotalSold AS S
ON B.stock_name = S.stock_name