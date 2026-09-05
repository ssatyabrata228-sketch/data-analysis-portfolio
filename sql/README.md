# 🗄️ SQL for Data Analysis

Use this folder for SQL practice and case studies.

## Core Topics

### Querying
```sql
SELECT column1, column2
FROM table_name
WHERE condition
ORDER BY column1 DESC;
```

### Aggregation
```sql
SELECT category, COUNT(*) AS records, AVG(amount) AS avg_amount
FROM sales
GROUP BY category
HAVING COUNT(*) > 10;
```

### JOINs
```sql
SELECT c.customer_id, c.customer_name, o.order_id, o.amount
FROM customers c
LEFT JOIN orders o
  ON c.customer_id = o.customer_id;
```

### CASE
```sql
SELECT customer_id,
       CASE
         WHEN total_spend >= 10000 THEN 'High Value'
         WHEN total_spend >= 5000 THEN 'Medium Value'
         ELSE 'Low Value'
       END AS segment
FROM customer_summary;
```

### CTE
```sql
WITH monthly_sales AS (
    SELECT DATE_TRUNC('month', order_date) AS month,
           SUM(amount) AS revenue
    FROM orders
    GROUP BY 1
)
SELECT *
FROM monthly_sales
ORDER BY month;
```

### Window Function
```sql
SELECT customer_id,
       order_date,
       amount,
       SUM(amount) OVER (
           PARTITION BY customer_id
           ORDER BY order_date
       ) AS running_spend
FROM orders;
```

## Analyst Checklist
- Understand the grain of every table.
- Check NULLs and duplicate records.
- Validate JOIN keys before calculating KPIs.
- Avoid accidental row multiplication.
- Use CTEs to make complex analysis readable.
- Explain assumptions and business meaning.

## Suggested Case Studies
- Sales performance
- Customer retention
- E-commerce funnel
- Employee attrition
- Marketing campaign performance
- Product performance
