"use strict";

var fs = require("fs");

var mysql = require("mysql");

var fastcsv = require("fast-csv");

var stream = fs.createReadStream("./RepOne_Data_Export.csv");
var csvData = [];
var csvStream = fastcsv.parse().on("data", function (data) {
  csvData.push(data);
}).on("end", function () {
  // remove the first line: header
  csvData.shift(); // create a new connection to the database

  var connection = mysql.createConnection({
    host: "192.168.1.11",
    user: "root",
    password: "rootroot",
    database: "VelocityAppDB"
  }); // open the connection

  connection.connect(function (error) {
    if (error) {
      console.error(error);
    } else {
      var query = "INSERT INTO category (exercise,set_number,rep,weight,metric,rpe,tags,start_time,rest_time,avg_velocity,rom,peak_velocity,peak_velocity_location,duration_of_rep) VALUES ?";
      connection.query(query, [csvData], function (error, response) {
        console.log(error || response);
      });
    }
  });
});
stream.pipe(csvStream);