SELECT Country, SUM(Profit) AS Total_Profit
FROM sales_data
GROUP BY Country
ORDER BY Total_Profit DESC;




SELECT Year, SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY Year;


SELECT Segment, SUM(Profit) AS Total_Profit
FROM sales_data
GROUP BY Segment;

SELECT Product, SUM(Profit) AS Total_Profit
FROM sales_data
GROUP BY Product
ORDER BY Total_Profit DESC
LIMIT 5;
