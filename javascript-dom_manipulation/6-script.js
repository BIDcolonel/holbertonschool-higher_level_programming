fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    const characterName = data.name;
    document.getElementById('character').innerText = characterName;
  })
  .catch(error => console.log(error));
