import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [employees, setEmployees] = useState([]); 

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/');
        setEmployees(response.data); // Update state with the fetched data
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="App">
      <h1>RR Tech Company</h1>
      <ul>
        {employees.map((employee, index) => (
          <li key={index}>
            <strong>Name:</strong> {employee.employee}, <strong>Department:</strong> {employee.department}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
