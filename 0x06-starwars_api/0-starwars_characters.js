#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const endpoint = `https://swapi-api.hbtn.io/api/films/${argv[2]}/`;
const promisifiedRequest = (api) => {
  return new Promise((resolve, reject) => {
    request(api, (err, res, body) => {
      if (!err) {
        resolve(JSON.parse(body));
      } else {
        reject(err);
      }
    });
  });
};
async function getCharacterUrls () {
  const response = await promisifiedRequest(endpoint);
  if (response) {
    return response.characters;
  }
}
async function printCharacters (characters) {
  for (const character of characters) {
    const response = await promisifiedRequest(character);
    if (response) {
      console.log(response.name);
    }
  }
}
const callAll = async () => {
  const chars = await getCharacterUrls();
  await printCharacters(chars);
};
callAll().then(() => {});
