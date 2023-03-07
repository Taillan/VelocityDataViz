import React, { useState } from "react";
import "./App.css";
import BarChart from "./component/BarChart";
import { UserData } from "./Data";
import { dbFunction } from "./dbScript/db.js";

function App() {
  
  const [userData, setUserData] = useState({
    
    labels: ['22/03', '23/03', '24/03', '25/03', '26/03', '27/03', '28/03'],
    datasets: [{
      label: '# of Votes',
      data: [1,2,3,4,5,6,7,8,9,10],
      backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(255, 159, 64, 0.2)'
      ],
      borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)'
      ],
      borderWidth: 1
  }]
  });

  // IF YOU SEE THIS COMMENT: I HAVE GOOD EYESIGHT

  return (
    <div className="App">
      
      <div style={{ width: 1000 }}>
        <BarChart chartData={userData}/>
      </div>
    </div>
  );
}

export default App;
