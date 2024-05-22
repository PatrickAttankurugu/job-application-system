import React, { useState } from 'react';

function JobPreferences() {
    const [query, setQuery] = useState('');
    const [location, setLocation] = useState('');
    const [jobs, setJobs] = useState([]);

    const searchJobs = async () => {
        const response = await fetch('/api/search_jobs', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query, location }),
        });
        const data = await response.json();
        setJobs(data);
    };

    return (
        <div>
            <h1>Job Preferences</h1>
            <input 
                type="text" 
                placeholder="Job Title" 
                value={query} 
                onChange={(e) => setQuery(e.target.value)} 
            />
            <input 
                type="text" 
                placeholder="Location" 
                value={location} 
                onChange={(e) => setLocation(e.target.value)} 
            />
            <button onClick={searchJobs}>Search Jobs</button>
            <ul>
                {jobs.map((job, index) => (
                    <li key={index}>
                        <h2>{job.title}</h2>
                        <p>{job.company}</p>
                        <p>{job.location}</p>
                        <p>{job.summary}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default JobPreferences;
