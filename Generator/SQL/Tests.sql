CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

INSERT INTO "System"("Power", "Details", "Name")
VALUES ('5v', 'Holds serveral meterological services', 'Meterological');

INSERT INTO "System"("Power", "Details", "Creation Date", "Name", "System", "Unique Identifier", "Modification Date")
VALUES ('5v', 'Primamry system in charge of site monitoring. Holds deployments related to montiorting the state of the site. Data collection from this system is for Quality Assurance purposes.', 'Site Monitoring');


INSERT INTO "Site_Network"("Started Date", "Name", "Original Funding Agency", "Grant Number String",  "Alias", "Unique Identifier", "Institution Name")
VALUES ('01-16-2019', 'NevCAN', 'NSF', 'IIA000000', 'NevCAN', uuid_generate_v4(), 'University of Nevada, Reno')
