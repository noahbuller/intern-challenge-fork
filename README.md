# Javelin Internship Final Coding Assessment

>PREFACE:
>This is NOT a final working solution of the FASTAPI and Next.js integration -- rather a checkpoint of current work. There are blocking factors, namely DB connection issues, preventing completion. This submission is meant to describe current work, while also serving as a proof-of-progress.

**NOTE: This repo is largely structured into two main directories: `app/` contains the configurations of the FASTAPI, and is largely complete. `nextjs-integration/` contains the framework to begin development of the second part of this assignment, however the majority of its functionality is unimplemented, as issues with database connection have complicated testing and development.**

## Description of Current File Structure (FASTAPI Portion/`app/...`)

- `/api/athletes.py`: This file is used to define the API routes that the FASTAPI uses. Currently, only 4 routes are defined, as the usage of the database is unknown. I decided to only implement 4 routes that I deemed most important, such as listing all the athletes with a GET request, or calculating the age of an athlete. I was unsure of the permissions of users within this application to POST/DELETE using this API, so I did not integrate these types of routes.

- `/api/database.py`: This file is relatively barebones, but is essential as it is used to instantiate environment variables and generate the DB URL and connection. There is an additional function that is used to properly handle DB session terminations.

- `/models/SQLAlchemyModels`: This file is very straightforward -- it contains the SQLAlchemy models of the DB based on the provided schema. There are commented out table restrictions as I had difficulty testing these without being able to directly connect to the database myself (see below for details on issue).

- `/utils/scoring.py`: This file contains the utility functions used to calculate how different weights and other factors listed in the `config/scoring_config` file. These are called in various other methods in the FASTAPI, and are used to modularize the codebase, allowing it to be easier to read and reducing overall file size.

- `main.py`: The main function of the FASTAPI, `main.py`, is used to call the `.env` variables to establish the database connection. Additionally, it is used to prefix all routes with the current development version (v1), so that routes can be tracked and eventually legacied as development advances. I found this was a good solution instead of constantly commenting out API routes on updates, we can change this prefix to match the dev version, and then slowly remove the functionality of older versions.

## Description of Current File Structure (Next.js Integration Portion/ `nextjs-integration/...`)
>
>Note: Since I am unable to connect to the database (see below), I am unable to check the functionality of this code, and therefore cannot guarantee it does not contain bugs/errors.

- `src/pages/api/athletes.ts`: This file establishes the route handler in Next.js to interact with the frontend. It fetches athlete data, weighted scores, etc.

- `src/interfaces/Athlete.ts`: This file defines a TypeScript interface for the data model of Athlete, and ensures type safety based on the provided schema.

- `src/pages/athletes.tsx`: This TypeScript React file begins the generation of a Next.js page that displays the list of all athletes by fetching the data from the /api/athletes endpoint and renders it. In current functionality, it serves no purpose as the DB cannot be connected to.

## Issues Establishing Database Connection

I want to reiterate that this is NOT the final working solution of this intern challenge. I have had difficulty connecting to the DB, and believe the issue to be with the `.env` variables, as I am unable to DNS resolve the host provided, even with multiple CLI tools such as `dig` and `ping`. This leads me to believe that there may be an error either with the `.env` file or with my system settings that I am unaware of.

With that in mind, I am unable to complete a portion of this assignment, as I am unable to test the previous functionality that I have implemented, such as the routes that attempt to grab athlete data.

Additionally, there is a significant portion of my code that is "unreachable" -- in the sense that without the database connection, I am unable to see the work that I have done being tested. This is especially prominent in the nextjs-integration (or lack thereof for several files), as there is no data for me to be rendering on this frontend.

## Design Decision - Omission of /test folder

- A continuation of the above discussion, but I have decided to omit the /test folder that is recommended in the provided file structure. This is due to my reasoning that without full functionality, or at least without a major component of being able to connect to the DB, the creation of tests that are guaranteed to fail seems unnecessary. In the event that I am able to fix the issue of connecting to the DB, I would add the /tests directory.

## Conclusion

I hope this repo conveys my work and skillset, as well as how this would me contibute to the Javelin team. I would be more than happy to continue development on this after I resolve the issue of DB connection, howeve I believe the resolution of this issue is beyond my abilities to resolve.

Noah
