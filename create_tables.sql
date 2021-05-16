CREATE TABLE public.global_temperature_raw(
	date date,
	avg_land_temperature numeric,
	min_land_temperature numeric,
	max_land_temperature numeric
);

CREATE TABLE public.country_temperature_raw(
	date date,
	avg_land_temperature numeric,
	country varchar(256)
);

CREATE TABLE public.co2_emissions_raw(
	year numeric,
	country_name varchar(256),
	co2 numeric
);

CREATE TABLE public.world_population_raw(
	country_code varchar(10),
	indicator varchar(256),
	year numeric,
	population numeric
);

CREATE TABLE public.country_codes(
	country_name varchar(256),
	country_code varchar(10)
);

CREATE TABLE public.aggregation(
	aggregation_id numeric,
	aggregation_type varchar(256)
);

CREATE TABLE public.world_climate_change(
	date date,
	country_code varchar(10),
	aggregation_id numeric,
	co2 numeric,
	avg_land_temperature numeric,
	min_land_temperature numeric,
	max_land_temperature numeric,
	population numeric
);	