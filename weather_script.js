const fetch = require('node-fetch');

const apiKey = 'c7c51bb77d9018aa3141d03ab118a940';
const city = 'London';
const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`;

fetch(url)c7c51bb77d9018aa3141d03ab118a940

    .then(response => response.json())
    .then(data => {
        console.log(`Weather in ${city}:`);
        console.log(`Temperature: ${data.main.temp}K`);
        console.log(`Weather: ${data.weather[0].description}`);
    })
    .catch(error => console.error('Error fetching weather data:', error));