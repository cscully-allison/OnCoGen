# OnCoGen
A repository for a code-generating software package that takes an ontology descriptive of classes of scientific metadata and generates database tables and services.

# Dependencies
This software relies on two packages which must be downloaded and configured before use.

1. Docker
 * Installation Instructions: https://docs.docker.com/install/overview/

2. Python & Pip
  * Python Installation Instructions: https://www.python.org/downloads/
  * Pip Installation Instructions: https://pip.pypa.io/en/stable/installing/

# Installation Instructions

1. From the top level directory of this project enter the following code on the command line

```
pip install -r requirements.txt
```

# Running Instructions

## Linux or Mac
1. Navigate to the "Generator/" directory in the command line.
2. From the "Generator/" directory run the following lines of code:

```
chmod 700 BuildAndRun.sh
./BuildAndRun.sh
```
  * The first line make the bash script executable
  * The second line runs the code generation driver, runs and configures generated docker containers and navigates the user into the database container.

3. To test and view tables, from inside the DataBase Container, run the following code:

```
psql <DataBaseName> OnCoGen
```

* Note: <DataBaseName> will be the string contained in the "nrdcrsh:abbreviation" tag in the ontology xml with a "\_DB" appended to the end of it. Using the default ontology bundled with this software <DataBaseName> will be "NRDC_DB".

4. Generated tables can be seen by typing:
```
\dt
```

5. To load default test data into the tables input the following

```
\i <filename>.sql
```

 * Note: The default test SQL file which loads data into the default NRDC_DB is called "Tests.sql". If you wish to modify this file or add your own file to test your own schema, you may add an additional file to this directory or modify this file freely. The container will detect any new added files or modifications to exiting files in this directory.

  5. a. To exit the sql program use the following command:
```
\quit
```

  5. b. To exit the container run the following command:
```
\exit
```


6. If you desire to spin down generated containers or clean out generated files run the following lines of code from the OnCoGen/Generator/ directory:

```
chmod 700 Clean.sh
./Clean.sh
```  
