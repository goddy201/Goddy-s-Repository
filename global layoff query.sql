select* from layoffs;
/*1. Remove duplicates
2. Standardize the Data
3. Null values or blank values
Remove any columns*/

create table layoffs_copy
like layoffs;

select *
from layoffs_copy;

INSERT layoffs_copy
SELECT *
FROM layoffs;

select *,
row_number() over(partition by company, industry, total_laid_off, percentage_laid_off, 'date')
as row_num
from layoffs;

with duplicate_cte as
(
select *,
row_number() over(partition by company, location, industry, total_laid_off, percentage_laid_off, 'date', stage, country, funds_raised_millions)
as row_num
from layoffs
)
select *
from duplicate_cte
where row_num > 1;

select *
from layoffs
where company = 'Casper';

CREATE TABLE `layoffs2` (
  `company` text,
  `location` text,
  `industry` text,
  `total_laid_off` int DEFAULT NULL,
  `percentage_laid_off` text,
  `date` text,
  `stage` text,
  `country` text,
  `funds_raised_millions` int DEFAULT NULL,
  `row_num` int
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

select *
from layoffs2
where row_num > 1;

insert into layoffs2
select *,
row_number() over(partition by company, location, industry, total_laid_off, percentage_laid_off, 'date', stage, country, funds_raised_millions)
as row_num
from layoffs;

set sql_safe_updates = 0;

delete
from layoffs2
where row_num > 1;
select *
from layoffs2
where row_num > 1;

select *
from layoffs2;

/* standardizing data*/

select company, trim(company)
from layoffs2;

select distinct industry
from layoffs2
order by 1;

select *
from layoffs2
where industry like 'Crypto%';

update layoffs2
set company = trim(company);

update layoffs2
set industry = 'Crypto'
where industry like 'Crypto%';

select *
from layoffs2 
where country like 'United States%'
order by 1;

select distinct country, trim(trailing '.' from country)
from layoffs2
order by 1;

update layoffs2
set country = trim(trailing '.' from country)
where country like 'United States%';

select `date`
from layoffs2;

update layoffs2
set `date` = str_to_date(`date`, '%m/%d/%Y');

alter table layoffs2
modify column `date` date;

select *
from layoffs2;

select *
from layoffs2 
where total_laid_off is null
and percentage_laid_off is null;

update layoffs2
set industry = null
where industry = '';

select *
from layoffs2
where industry is null
or industry = '';

select *
from layoffs2 t1
join layoffs2 t2
	on t1.company = t2.company
where (t1.industry is null or t1.industry = '')
and t2.industry is not null;

select t1.industry, t2.industry
from layoffs2 t1
join layoffs2 t2
	on t1.company = t2.company
where (t1.industry is null or t1.industry = '')
and t2.industry is not null;

update layoffs2 t1
join layoffs2 t2
	on t1.company = t2.company
set t1.industry = t2.industry
where t1.industry is null
and t2.industry is not null;

select *
from layoffs2
where company = 'Airbnb';

select *
from layoffs2
where total_laid_off is null
and percentage_laid_off is null;

alter table layoffs2
drop column row_num;

delete
from layoffs2
where total_laid_off is null
and percentage_laid_off is null;

select *
from layoffs2;