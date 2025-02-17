CREATE TABLE IF NOT EXISTS StateGDP (
    "id" INTEGER,
    "Stateid" INTEGER,
    "GDP" INTEGER,
    "Year" INTEGER,
    PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS States (
    "id" INTEGER,
    "State_Name" TEXT,
    "State_Initials" TEXT,
    "State_Code" TEXT,
    PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS Zones (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "state_id" TEXT NOT NULL,            -- State name (e.g., Illinois)
    "county" TEXT,                    -- County name (NULL if not applicable)
    "city" TEXT,                      -- City name (NULL if not applicable)
    "town" TEXT,                      -- Town name (NULL if not applicable)
    "district" TEXT,                   -- District name (NULL if not applicable)
    "population" INTEGER NOT NULL,     -- Population for this area
    FOREIGN KEY ("state_id") REFERENCES States("id")
);

CREATE TABLE IF NOT EXISTS ZipCode(
    "ZipCode" INTEGER,
    "Zone_id" INTEGER,
    FOREIGN KEY ("Zone_id") REFERENCES Zones("id")

)


CREATE TABLE Population (
    "State_Zone_id" INTEGER,
    "Number_of_people" INTEGER,
    FOREIGN KEY ("State_Zone_id") REFERENCES StateZones("id")
);