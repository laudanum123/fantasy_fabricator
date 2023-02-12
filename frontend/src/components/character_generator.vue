<template>
  <div class="container my-5" style="width: 600px;">
    <h2 class="text-center mb-5">Character Generator</h2>
    <form>
      <div class="form-group d-flex my-2">
        <label for="adventure-title" class="w-25"
          style="margin-right: 1rem; display: inline-block; line-height: 2.5;">Adventure Title:</label>
        <select class="form-control w-75" id="adventure-title" v-model="selectedId">
          <option value="">-- Select Adventure Title --</option>
          <option v-for="adventure in adventureTitles" :key="adventure.id" :value="adventure.id">{{ adventure.title }}
          </option>
        </select>
      </div>
      <div class="form-group d-flex my-2">
        <label for="character-name" class="w-25"
          style="margin-right: 1rem; display: inline-block; line-height: 2.5;">Character Name:</label>
        <input type="text" class="form-control w-75" id="character-name" v-model="characterName"
          placeholder="Enter Character Name">
      </div>
      <div class="form-group d-flex my-2">
        <label for="game-system" class="w-25" style="margin-right: 1rem; display: inline-block; line-height: 2.5;">Game
          System:</label>
        <select class="form-control w-75" id="game-system" v-model="selectedSystem" style="text-align: center;">
          <option v-for="gameSystem in gameSystems" :key="gameSystem" :value="gameSystem">{{ gameSystem }}</option>
        </select>
      </div>
      <div class="form-group d-flex my-2" v-if="selectedSystem === 'Define other'">
        <label for="custom-system" class="w-25"
          style="margin-right: 1rem; display: inline-block; line-height: 2.5;">Custom System:</label>
        <input type="text" class="form-control w-75" id="custom-system" v-model="customSystem"
          placeholder="Enter your own game system">
      </div>
      <div class="form-group d-flex my-2">
        <label for="game-system-version" class="w-25"
          style="margin-right: 1rem; display: inline-block; line-height: 2.5;">
          Edition:</label>
        <select class="form-control w-75" id="game-system-version" v-model="selectedSystemVersion"
          style="text-align: center;">
          <option v-for="version in gameSystemVersions" :key="version" :value="version">{{ version }}</option>
        </select>
      </div>

      <button class="btn btn-primary my-3" @click="generateCharacter">Generate Character</button>
    </form>
    <div class="card mt-5" v-if="character">
      <div class="card-header">

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
import axios from 'axios';
const backendURL = 'http://localhost:5000';
export default {
  data() {
    return {
      characterName: '',
      gameSystems: ['D&D', 'Pathfinder', 'Shadowrun', 'GURPS', 'World of Darkness', 'Call of Cthulhu', 'Fate', 'Savage Worlds', 'Starfinder', 'RuneQuest', 'HeroQuest', 'Ars Magica', 'Numenera', 'Define other'],
      selectedSystem: 'D&D',
      gameSystemVersions: [1, 2, 3, 4, 5],
      gameSystemVersionMap: {
        'D&D': [1, 2, 3, 4, 5],
        'Pathfinder': [1, 2],
        'Shadowrun': [5, 6],
        'GURPS': [4],
        'World of Darkness': ['20th', 'Revised'],
        'Call of Cthulhu': [1, 2, 3, 4, 5, 5.5, 5.6, 6, 7],
        'Fate': ["Accelerated", "Condensed", "Atomic Robo", "The Dresden Files", "Fate of Cthulhu", "Core"],
        'Savage Worlds': ['Explorer’s Edition', 'Deluxe Edition', 'Adventure Edition'],
        'Starfinder': ['Alien Archive', 'Pact Worlds', 'Armory', 'Original', 'Core Rolebook'],
        'RuneQuest': [1, 2, 3, 4, 5, 6, 'Glorantha', 'Mythras'],
        'HeroQuest': [1, 2, 'Glorantha'],
        'Ars Magica': [1, 2, 3, 4, 5],
        'Numenera': ['Discovery', 'Destiny', 'Core Rulebook']
        // Add the other systems here
      },
      selectedSystemVersion: '5',
      customSystem: '',
      character: null,
      adventureTitles: [],
      searchTerm: '',
      selectedId: ''
    }
  },
  mounted() {
    const path = `${backendURL}/get_adventures_from_db`;
    axios.get(path)
      .then(response => {
        this.adventureTitles = response.data.map(adventure => {
          return {
            'id': adventure.id,
            'title': adventure.AdventureTitle,
          }
        });
        console.log(this.adventureTitles)
      })
      .catch(error => {
        console.log(error)
      })
  },

  methods: {
    generateCharacter() {
      const path = `${backendURL}/generate_npc`;
      axios.post(path, {
        characterName: this.characterName,
        selectedSystem: this.selectedSystem,
        customSystem: this.customSystem,
        adventureId: this.selectedId
      })
        .then(response => {
          console.log(response);
          this.character = {
            name: this.characterName,
            background: 'Generated Background',
            stats: 'Generated Stats'
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
  },
  watch: {
    selectedSystem(newSystem) {
      this.gameSystemVersions = this.gameSystemVersionMap[newSystem];
      this.selectedSystemVersion = this.gameSystemVersions[this.gameSystemVersions.length - 1];
    }
  },
}
</script>