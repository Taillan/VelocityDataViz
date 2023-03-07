"use strict";

var mariadb = require('mariadb');

var pool = mariadb.createPool({
  host: '192.168.1.11',
  user: 'root',
  password: 'rootroot',
  connectionLimit: 5
});

function initTable() {
  var conn, DB;
  return regeneratorRuntime.async(function initTable$(_context) {
    while (1) {
      switch (_context.prev = _context.next) {
        case 0:
          _context.prev = 0;
          console.log("trying connection");
          _context.next = 4;
          return regeneratorRuntime.awrap(pool.getConnection());

        case 4:
          conn = _context.sent;
          console.log("connected");
          _context.next = 8;
          return regeneratorRuntime.awrap(conn.query("USE VelocityAppDB;"));

        case 8:
          DB = _context.sent;
          createTable(conn);
          console.log("Table créé");
          _context.next = 17;
          break;

        case 13:
          _context.prev = 13;
          _context.t0 = _context["catch"](0);
          conn.end();
          throw _context.t0;

        case 17:
          _context.prev = 17;
          console.log("finally");

          if (!conn) {
            _context.next = 21;
            break;
          }

          return _context.abrupt("return", conn.end());

        case 21:
          console.log("closed");
          return _context.abrupt("return");

        case 24:
        case "end":
          return _context.stop();
      }
    }
  }, null, null, [[0, 13, 17, 24]]);
}

function createTable(conn) {
  return regeneratorRuntime.async(function createTable$(_context2) {
    while (1) {
      switch (_context2.prev = _context2.next) {
        case 0:
          console.log("createTable");
          return _context2.abrupt("return", conn.query("\n  CREATE TABLE IF NOT EXISTS velocityData\n  (\n    exercise                VARCHAR(30),\n    set_number              INT,\n    rep                     INT,\n    weight                  INT,\n    metric                  VARCHAR(5),\n    rpe                     VARCHAR(3),\n    tags                    VARCHAR(50),\n    start_time              VARCHAR(20),\n    rest_time               VARCHAR(10),\n    avg_velocity            FLOAT,\n    rom                     INT,\n    peak_velocity           FLOAT,\n    peak_velocity_location  INT,\n    duration_of_rep         FLOAT\n  )\n"));

        case 2:
        case "end":
          return _context2.stop();
      }
    }
  });
}

module.exports = initTable();