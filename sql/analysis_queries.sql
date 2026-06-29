SELECT COUNT(*) AS total_jobs
FROM jobs_sql;

SELECT COUNT(DISTINCT company_name) AS total_companies
FROM jobs_sql;

SELECT COUNT(DISTINCT industry) AS total_industries
FROM jobs_sql;

SELECT COUNT(DISTINCT sector) AS total_sectors
FROM jobs_sql;

SELECT
    company_name,
    COUNT(*) AS total_jobs
FROM jobs_sql
GROUP BY company_name
ORDER BY total_jobs DESC
LIMIT 10;

SELECT
    location,
    COUNT(*) AS total_jobs
FROM jobs_sql
GROUP BY location
ORDER BY total_jobs DESC
LIMIT 10;

SELECT
    industry,
    COUNT(*) AS total_jobs
FROM jobs_sql
GROUP BY industry
ORDER BY total_jobs DESC;

SELECT
    sector,
    COUNT(*) AS total_jobs
FROM jobs_sql
GROUP BY sector
ORDER BY total_jobs DESC;

SELECT
    ROUND(AVG(avg_salary),2) AS avg_salary
FROM jobs_sql;

SELECT
    job_title,
    ROUND(AVG(avg_salary),2) AS avg_salary
FROM jobs_sql
GROUP BY job_title
ORDER BY avg_salary DESC
LIMIT 10;

SELECT
    industry,
    ROUND(AVG(avg_salary),2) AS avg_salary
FROM jobs_sql
GROUP BY industry
ORDER BY avg_salary DESC;

SELECT
    sector,
    ROUND(AVG(avg_salary),2) AS avg_salary
FROM jobs_sql
GROUP BY sector
ORDER BY avg_salary DESC;

SELECT
    location,
    ROUND(AVG(avg_salary),2) AS avg_salary
FROM jobs_sql
GROUP BY location
ORDER BY avg_salary DESC
LIMIT 10;

SELECT
    company_name,
    ROUND(AVG(avg_salary),2) AS avg_salary
FROM jobs_sql
GROUP BY company_name
HAVING COUNT(*) >= 3
ORDER BY avg_salary DESC
LIMIT 10;

SELECT
    company_name,
    ROUND(AVG(rating),2) AS rating
FROM jobs_sql
GROUP BY company_name
ORDER BY rating DESC
LIMIT 10;

SELECT
    size,
    ROUND(AVG(avg_salary),2) AS avg_salary
FROM jobs_sql
GROUP BY size
ORDER BY avg_salary DESC;

SELECT
    company_age,
    ROUND(AVG(avg_salary),2) AS avg_salary
FROM jobs_sql
GROUP BY company_age
ORDER BY company_age;

SELECT
    job_title,
    avg_salary,
    DENSE_RANK() OVER(
        ORDER BY avg_salary DESC
    ) AS salary_rank
FROM jobs_sql;

SELECT
    company_name,
    COUNT(*) AS jobs,
    DENSE_RANK() OVER(
        ORDER BY COUNT(*) DESC
    ) AS hiring_rank
FROM jobs_sql
GROUP BY company_name;

SELECT
    avg_salary,
    AVG(avg_salary) OVER(
        ORDER BY avg_salary
    ) AS running_avg_salary
FROM jobs_sql;

SELECT
    job_title,
    COUNT(*) AS total_jobs,
    ROUND(AVG(avg_salary),2) AS avg_salary
FROM jobs_sql
GROUP BY job_title
HAVING COUNT(*) >= 5
ORDER BY avg_salary DESC
LIMIT 10;

SELECT
sector,
ROUND(AVG(avg_salary) ,2) AS avg_salary
FROM jobs_sql
GROUP BY sector
ORDER BY avg_salary DESC
LIMIT 10;

SELECT
industry,
ROUND(AVG(avg_salary) ,2) AS avg_salary
FROM jobs_sql
GROUP BY industry
ORDER BY avg_salary DESC
LIMIT 10;

SELECT
size,
ROUND(AVG(avg_salary) ,2) AS avg_salary
FROM jobs_sql
GROUP BY size
ORDER BY avg_salary DESC
LIMIT 10;

SELECT
ROUND(AVG(avg_salary),2) AS average_salary
FROM jobs_sql;

SELECT
COUNT(DISTINCT company_name) 
FROM jobs_sql;

SELECT
ROUND(AVG(rating),2) AS average_rating
FROM jobs_sql;

SELECT
    industry,
    ROUND(AVG(rating),2) AS avg_rating
FROM jobs_sql
GROUP BY industry
ORDER BY avg_rating DESC
LIMIT 10;

SELECT
    size,
    COUNT(*) AS total_jobs
FROM jobs_sql
GROUP BY size
ORDER BY total_jobs DESC;


SELECT
    easy_apply,
    COUNT(*) AS total_jobs
FROM jobs_sql
GROUP BY easy_apply;
