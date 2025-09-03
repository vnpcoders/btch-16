-- Retrieve all cities from the City table where the population is greater than 1 million.

use world;
select name from city
where population>1000000;

-- 2) Get all countries from the Country table where the life expectancy is greater than
-- 75 years.

select name from country
where lifeExpectancy>75
group by name;

-- 3) Find all cities in the City table that belong to the country with the code 'USA'.

select name from city
where countrycode='usa'
group by name;
-- 4) List all countries where the government form is a republic.

select name from country
where GovernmentForm="republic" 
group by name;

-- 5) Retrieve all languages from the CountryLanguage table where the language is
-- spoken by more than 50% of the population.
