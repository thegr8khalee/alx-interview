#!/usr/bin/node
const request = require('request');

// Get the Movie ID from the command-line arguments
const movieId = process.argv[2];

// Base URL of the Star Wars API
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Fetch the movie data
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parse the response body as JSON
  const data = JSON.parse(body);

  // Fetch the characters' URLs
  const characters = data.characters;

  // Fetch and print each character's name in order
  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
