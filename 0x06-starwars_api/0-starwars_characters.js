#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Invalid response:', response.statusCode);
  } else {
    const filmData = JSON.parse(body);
    const charactersUrls = filmData.characters;

    // Fetch character names
    charactersUrls.forEach(characterUrl => {
      request(characterUrl, function (error, response, body) {
        if (!error && response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    });
  }
});
