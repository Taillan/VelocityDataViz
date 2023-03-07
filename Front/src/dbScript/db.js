const mariadb = require('mariadb');

const pool = mariadb.createPool({
  host: '192.168.1.11', 
  user:'root', 
  password: 'rootroot',
  connectionLimit: 5
});

async function initTable() {
  let conn;
  try {
    console.log("trying connection");
    conn = await pool.getConnection();
    console.log("connected");
    const DB = await conn.query("USE VelocityAppDB;");
    createTable(conn);
    console.log("Table créé");
  } catch (err) {
    conn.end();
	  throw err;
  } finally {
    console.log("finally");
	  if (conn) return conn.end();
    console.log("closed");
    return;
  }
}

async function createTable(conn) {
  console.log("createTable");
  return conn.query(`
  CREATE TABLE IF NOT EXISTS velocityData
  (
    exercise                VARCHAR(30),
    set_number              INT,
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

module.exports = initTable();