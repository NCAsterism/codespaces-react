import React, { useState, useEffect } from 'react';

function App() {
    const [tasks, setTasks] = useState([]);
    const [mode, setMode] = useState('work');
    const [nextTask, setNextTask] = useState(null);

    useEffect(() => {
        fetch(`/api/next_task?mode=${mode}`)
            .then(response => response.json())
            .then(data => setNextTask(data.task));
    }, [mode]);

    const handleModeChange = (event) => {
        setMode(event.target.value);
    };

    return (
        <div>
            <h1>AI Assistant</h1>
            <div>
                <label>Select Mode: </label>
                <select value={mode} onChange={handleModeChange}>
                    <option value="work">Work</option>
                    <option value="relax">Relax</option>
                    <option value="improve">Personal Improvement</option>
                </select>
            </div>
            <div>
                <h2>Next Task: {nextTask}</h2>
            </div>
        </div>
    );
}

export default App;
