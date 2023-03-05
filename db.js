const fs = require("fs");
const sqlite3 = require("sqlite3").verbose();
const filepath = "./velocityData.db";

function connectToDatabase() {
  if (fs.existsSync(filepath)) {
    return new sqlite3.Database(filepath);
  } else {
    const db = new sqlite3.Database(filepath, (error) => {
      if (error) {
        return console.error(error.message);
      }
      createTable(db);
      console.log("Connected to the database successfully");
    });
    return db;
  }
}

function createTable(db) {
    db.exec(`
    CREATE TABLE IF NOT EXISTS velocity
    (
      exercise                VARCHAR(30),
      set_number                     INT,
      rep                     INT,
      weight                  INT,
      metric                  VARCHAR(5),
      rpe                     VARCHAR(3),
      tags                    VARCHAR(50),
      start_time              VARCHAR(20),
      rest_time               VARCHAR(10),
      avg_velocity            FLOAT,
      rom                     INT,
      peak_velocity           FLOAT,
      peak_velocity_location  INT,
      duration_of_rep         FLOAT
    )
  `);
}

module.exports = connectToDatabase();

