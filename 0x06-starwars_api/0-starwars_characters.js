#!/usr/bin/env node

const request = require('request');
const movieId = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${movieId}/`, (error, response, body) => {
  const movie = JSON.parse(body);
  const characterUrls = movie.characters;
  let completedRequests = 0;
  const characterNames = new Array(characterUrls.length);
  
  characterUrls.forEach((characterUrl, index) => {
    request(characterUrl, (error, response, body) => {
      const character = JSON.parse(body);
      characterNames[index] = character.name;
      completedRequests++;
      
      if (completedRequests === characterUrls.length) {
        characterNames.forEach(name => {
          console.log(name);
        });
      }
    });
  });
});
