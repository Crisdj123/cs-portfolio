CREATE TABLE title_basics (
  tconst TEXT PRIMARY KEY,
  titleType TEXT,
  primaryTitle TEXT,
  originalTitle TEXT,
  isAdult BOOLEAN,
  startYear INT,
  endYear INT,
  runtimeMinutes INT,
  genres TEXT
);

CREATE TABLE title_ratings (
  tconst TEXT PRIMARY KEY,
  averageRating NUMERIC(3,1),
  numVotes INT
);

CREATE TABLE name_basics (
    nconst TEXT PRIMARY KEY,
    primaryName TEXT,
    birthYear INT,
    deathYear INT,
    primaryProfession TEXT,
    knownForTitles TEXT
);

CREATE TABLE title_principals (
    tconst TEXT,
    ordering INT,
    nconst TEXT,
    category TEXT,
    job TEXT,
    characters TEXT,
    PRIMARY KEY (tconst, ordering)
);
