# 📊 Power BI

## Core Skills

- Importing data
- Power Query transformations
- Data type and quality checks
- Relationships and cardinality
- Star-schema fundamentals
- Measures vs calculated columns
- DAX fundamentals
- Filter context
- Time-based analysis
- KPI cards
- Tables and matrices
- Bar, line and combo charts
- Slicers and drill-through
- Report navigation
- Dashboard storytelling

## Recommended Workflow

**Connect → Profile → Transform → Model → Create Measures → Visualize → Validate → Publish/Present**

## DAX Practice

```DAX
Total Sales = SUM(Sales[SalesAmount])

Total Orders = DISTINCTCOUNT(Sales[OrderID])

Average Order Value = DIVIDE([Total Sales], [Total Orders])
```

## Dashboard Quality Checklist
- Use a clear business objective.
- Keep the number of visuals purposeful.
- Use meaningful titles and units.
- Validate measures against source calculations.
- Keep relationships simple and documented.
- Prefer measures for reusable business logic.
- Make filters and interactions understandable.
- End the report with decisions or recommendations, not just charts.
