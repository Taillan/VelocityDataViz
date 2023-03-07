const fs = require("fs");
const {
  parse
} = require("csv-parse");
const db = require("./db");


function ImportCsv(db) {
  fs.createReadStream("RepOne_Data_Export.csv")
    .pipe(parse({
      delimiter: ",",
      from_line: 2
    }))
    .on("data", function (row) {
      db.serialize(function () {
        db.run(
          `INSERT INTO velocity VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`,
          [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13]],
          function (error) {
            if (error) {
              return console.log(error.message);
            }
            console.log(`Inserted a row with the id: ${this.lastID}`);
          }
        );
      });
    });
}
module.exports = ImportCsv();