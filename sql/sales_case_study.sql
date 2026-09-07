-- SQL Business Case Study: Sales Performance
-- Goal: identify top categories, regions and products.

-- 1. Total revenue
SELECT SUM(units * unit_price) AS total_revenue
FROM sales;

-- 2. Revenue by category
SELECT category,
       SUM(units * unit_price) AS revenue
FROM sales
GROUP BY category
ORDER BY revenue DESC;

-- 3. Revenue by region
SELECT region,
       SUM(units * unit_price) AS revenue
FROM sales
GROUP BY region
ORDER BY revenue DESC;

-- 4. Monthly revenue
SELECT DATE_TRUNC('month', sale_date) AS month,
       SUM(units * unit_price) AS revenue
FROM sales
GROUP BY DATE_TRUNC('month', sale_date)
ORDER BY month;

-- 5. Rank categories by revenue
WITH category_sales AS (
    SELECT category,
           SUM(units * unit_price) AS revenue
    FROM sales
    GROUP BY category
)
SELECT category,
       revenue,
       RANK() OVER (ORDER BY revenue DESC) AS revenue_rank
FROM category_sales;

-- Adapt DATE_TRUNC syntax for MySQL/SQL Server if needed.
