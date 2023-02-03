<template>
    <div class="container my-5">
      <h2 class="text-center mb-5">Character Generator</h2>
      <form>
        <div class="form-group">
          <label for="character-name">Character Name:</label>
          <input type="text" class="form-control" id="character-name" v-model="characterName"
            placeholder="Enter Character Name">
        </div>
        <div class="form-group">
          <label for="game-system">Game System:</label>
          <select class="form-control" id="game-system" v-model="selectedSystem">
            <option v-for="gameSystem in gameSystems" :key="gameSystem" :value="gameSystem">{{ gameSystem }}</option>
          </select>
        </div>
        <div class="form-group">
          <label for="custom-system">Custom System:</label>
          <input type="text" class="form-control" id="custom-system" v-model="customSystem"
            placeholder="Enter your own game system">
        </div>
        <button class="btn btn-primary" @click="generateCharacter">Generate Character</button>
      </form>
      <div class="card mt-5" v-if="character">
        <div class="card-header">
          {{ character.name }}
        </div>
        <div class="card-body">
          <h5 class="card-title">Background</h5>
          <p class="card-text">{{ character.background }}</p>
          <h5 class="card-title">Stats</h5>
          <p class="card-text">{{ character.stats }}</p>
        </div>
      </div>
    </div>
  </template>
  <script>
  export default {
    data() {
      return {
        characterName: '',
        gameSystems: ['D&D', 'Pathfinder', 'Shadowrun', 'GURPS', 'World of Darkness', 'Call of Cthulhu', 'Fate', 'Savage Worlds', 'Starfinder', 'RuneQuest', 'HeroQuest', 'Ars Magica', 'Numenera'],
        selectedSystem: 'D&D',
        customSystem: '',
        character: null
      }
    },
    methods: {
      generateCharacter() {
        this.character = {
          name: this.characterName,
          background: 'Generated Background',
          stats: 'Generated Stats'
        }
      }
    }
  }
  </script>