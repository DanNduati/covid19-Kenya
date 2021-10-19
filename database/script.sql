CREATE TABLE data (
    id INT AUTO_INCREMENT,
	country_name VARCHAR(10) NOT NULL,
	total_cases INT(255) NOT NULL,
    new_cases INT(255),
    total_deaths INT(255),
    new_deaths INT(255),
    total_recovered INT(255),
    new_recovered INT(255),
    active_cases INT(255),
    serious_cases INT(255),
    total_cases_per_m INT(255),
    deaths_per_m INT(255),
    total_tests INT(255),
    tests_per_m INT(255),
    population INT(255),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
) ENGINE=INNODB;