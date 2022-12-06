select *
from covid_death cd 
where continent is not null 
order by 3, 4

-- select *
-- from covid_vaccinations cv 
-- order by 3, 4

-- select data that we are going to be using

select location, `date` , total_cases, new_cases, total_deaths, population 
from covid_death cd
where continent is not null
order by 1, 2

-- Total Cases vs Total Deaths
-- Shows likelihood of dying if you contract covid in your country

select location, 
	`date`,
	total_cases,
	total_deaths,
	(total_cases/total_deaths)*100 as death_percentage
from covid_death cd
where location like '%Indonesia%'
and continent is not null 
order by 1, 2

-- Looking at Total Cases Vs Population
-- shows what percentage of population got covid

select location, 
	`date`,
	population,
	total_cases,
	(total_cases/population)*100 as cases_percentage
from covid_death cd
where location like '%Indonesia%'
and continent is not null
order by 1, 2

-- Looking at countries with Highest Infection Rate compared to Population 

select location, 
	population,
	MAX(total_cases) as highest_infected_count,
	MAX((total_cases/population))*100 as cases_percentage
from covid_death cd
where continent is not null 
group by location, population
order by cases_percentage desc 

-- Showing countries with Highest Death Count per Population

select location, 
	MAX(total_deaths) as total_death_count
from covid_death cd
where continent is not null
group by location 
order by total_death_count desc

-- LET'S BREAK THINGS DOWN by CONTINENT


-- Showing continents with the Highest Death Count per Population

select continent, 
	MAX(total_deaths) as total_death_count
from covid_death cd
where continent is not null
group by continent  
order by total_death_count desc


-- Global Number

select `date`,
	SUM(new_cases) as total_new_cases,
	SUM(new_deaths) as total_new_death,
	SUM(new_cases)/SUM(new_deaths)*100 as death_percentage
from covid_death cd 
where continent is not null 
group by `date` 
order by 1, 2

-- Global Total Number

select
	SUM(new_cases) as total_new_cases,
	SUM(new_deaths) as total_new_death,
	SUM(new_cases)/SUM(new_deaths)*100 as death_percentage
from covid_death cd 
where continent is not null  
order by 1, 2


-- Looking at Total Population vs Vaccinations

select 
	cd.continent,
	cd.location,
	cd.`date`,
	cd.population,
	cv.new_vaccinations,
	SUM(CAST(cv.new_vaccinations as DOUBLE)) OVER (partition by cd.location order by cd.location, cd.`date`) as rolling_people_vaccinated
from covid_death cd
join covid_vaccinations cv
	on cd.location = cv.location
	and cd.date = cv.date
where cd.continent is not null
order by 2, 3

-- USE CTE(Temporary Table)

create temporary table PopvsVac(
select
	cd2.continent,
	cd2.location,
	cd2.`date`,
	cd2.population,
	cv2.new_vaccinations,
	SUM(CAST(cv2.new_vaccinations as DOUBLE)) OVER (partition by cd2.location order by cd2.location, cd2.`date`) as rolling_people_vaccinated
from covid_death cd2 
join covid_vaccinations cv2
	on cd2.location = cv2.location 
	and cd2.date = cv2.date
where cd2.continent is not null
)

select *, (rolling_people_vaccinated/population)*100
from PopvsVac


-- Creating view to store data later visualizations

create view PercentPopulationVaccinated as
select
	cd2.continent,
	cd2.location,
	cd2.`date`,
	cd2.population,
	cv2.new_vaccinations,
	SUM(CAST(cv2.new_vaccinations as DOUBLE)) OVER (partition by cd2.location order by cd2.location, cd2.`date`) as rolling_people_vaccinated
from covid_death cd2 
join covid_vaccinations cv2
	on cd2.location = cv2.location 
	and cd2.date = cv2.date
where cd2.continent is not null

select *
from percentpopulationvaccinated p 