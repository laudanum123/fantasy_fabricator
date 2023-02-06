<template>
  <div class="container my-5" style="width: 600px;">
    <h2 class="text-center mb-5">Character Generator</h2>
    <form>
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
        <label for="adventure-title" class="w-25"
          style="margin-right: 1rem; display: inline-block; line-height: 2.5;">Adventure Title:</label>
        <input type="text" class="form-control w-75" id="adventure-title" v-model="searchTerm"
          placeholder="Enter Adventure Title" @input="handleAdventureTitleInput" @keydown.enter="selectTitle(title)">
      </div>
      <div class="form-group d-flex my-2">
        <ul v-if="searchTerm.length > 1">
          <li v-for="title in filteredTitles.slice(0, 1)" :key="title" @click="selectTitle(title)"
            class="list-group-item list-group-item-action">{{ title }}</li>
        </ul>
      </div>
      <button class="btn btn-primary my-3" @click="generateCharacter">Generate Character</button>
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
import axios from 'axios';
const backendURL = 'http://localhost:5000';
export default {
  data() {
    return {
      characterName: '',
      gameSystems: ['D&D', 'Pathfinder', 'Shadowrun', 'GURPS', 'World of Darkness', 'Call of Cthulhu', 'Fate', 'Savage Worlds', 'Starfinder', 'RuneQuest', 'HeroQuest', 'Ars Magica', 'Numenera', 'Define other'],
      selectedSystem: 'D&D',
      customSystem: '',
      character: null,
      adventureTitles: ["Lost Mines of Phandelver",
        "Tyranny of Dragons",
        "Hoard of the Dragon Queen",
        "The Rise of Tiamat",
        "Storm King's Thunder",
        "Tomb of Annihilation",
        "Waterdeep: Dragon Heist",
        "Icewind Dale: Rime of the Frostmaiden",
        "The Wild Beyond the Witchlight"
      ],
      searchTerm: '',
      selectedTitle: ''
    }
  },
  computed: {
    filteredTitles() {
      return this.adventureTitles.filter(title => title.toLowerCase().includes(this.searchTerm.toLowerCase()))
    }
  },

  methods: {
    generateCharacter() {
      const path = `${backendURL}/generate_npc`;
      axios.post(path, {
        characterName: this.characterName,
        selectedSystem: this.selectedSystem,
        customSystem: this.customSystem,
        adventureTitle: this.selectedTitle
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
    selectTitle(title) {
      this.searchTerm = title
      this.selectedTitle = title
      this.$nextTick(() => {
        let ul = document.querySelector('ul')
        ul.remove()
      })
    }
  }
}
</script>