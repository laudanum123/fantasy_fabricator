<template>
  <div class="container my-5">
    <h2 class="text-center mb-5 heading">Adventure Builder</h2>
    <form>
      <div class="form-group"></div>
      <div class="row mb-5">

        <div class="col-md-4">
          <label for="adventure-title">Adventure Title:</label>
        </div>
        <div class="col-md-8">
          <input type="text" class="form-control" id="adventure-title" v-model="adventureTitle"
            placeholder="Enter a title for your adventure (e.g. 'The Lost Temple', 'Rescue the Princess')">
        </div>
      </div>
      <div class="form-group">
        <div class="row mb-5">
          <div class="col-md-4">
            <label for="adventure-setting">Adventure Setting:</label>
          </div>
          <div class="col-md-8">
            <select class="form-control" id="adventure-setting" v-model="adventureSetting">
              <option value="medieval fantasy">Medieval Fantasy</option>
              <option value="post-apocalyptic">Post-Apocalyptic</option>
              <option value="steampunk">Steampunk</option>
              <option value="horror">Horror</option>
              <option value="superheroes">Superheroes</option>
              <option value="science fiction">Science Fiction</option>
              <option value="urban fantasy">Urban Fantasy</option>
              <option value="cyberpunk">Cyberpunk</option>
              <option value="historical">Historical</option>
              <option value="high fantasy">High Fantasy</option>
              <option value="space opera">Space Opera</option>
              <option value="time travel">Time Travel</option>
              <option value="zombie apocalypse">Zombie Apocalypse</option>
              <option value="dystopian">Dystopian</option>
              <option value="mythological">Mythological</option>
              <option value="alternate history">Alternate History</option>
              <option value="western">Western</option>
              <option value="pirates">Pirates</option>
              <option value="vampires">Vampires</option>
              <option value="werewolves">Werewolves</option>
              <option value="other">Other (please specify in the field below)</option>
            </select>
            <input type="text" class="form-control mt-2" v-if="adventureSetting === 'other'" v-model="customSetting"
              placeholder="Enter your own adventure setting">
          </div>
        </div>
      </div>
      <div class="form-group mb-5">
        <div class="row mb-5">
          <div class="col-md-4"><label for="adventure-plot">Adventure Plot:</label></div>
          <div class="col-md-8">
            <textarea class="form-control" id="adventure-plot" v-model="adventurePlot"
              placeholder="Enter a brief description of the adventure's main plot or goal (e.g. 'The players must find a way to stop an ancient evil from being unleashed', 'The players are hired to infiltrate a rival guild and steal a powerful artifact')"></textarea>
          </div>
        </div>
      </div>
      <button class="btn btn-primary" v-on:click="generateAdventure()">Generate Adventure</button>
    </form>
  </div>
  <transition name="fade">
    <div class="container my-5" v-if="adventure">
      <div class="row">
        <div class="col-md-4">
          <div class="card">
            <div class="card-header bg-secondary text-white">Title</div>
            <div class="card-body bg-light">{{ adventure.AdventureTitle }}</div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="card">
            <div class="card-header bg-secondary text-white">Hook</div>
            <div class="card-body bg-light">{{ adventure.AdventureHook }}</div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="card">
            <div class="card-header bg-secondary text-white">Plot</div>
            <div class="card-body bg-light">{{ adventure.AdventurePlot }}</div>
          </div>
        </div>
        <div class="container my-5" v-if="adventure">
          <div class="row">
            <div class="col-md-4">
              <div class="card">
                <div class="card-header bg-secondary text-white">Climax</div>
                <div class="card-body bg-light">{{ adventure.AdventureClimax }}</div>
              </div>
            </div>
            <div class="col-md-4">
              <div class="card">
                <div class="card-header bg-secondary text-white">Resolution</div>
                <div class="card-body bg-light">{{ adventure.AdventureResolution }}</div>
              </div>
            </div>
            <div class="col-md-4">
              <div class="card">
                <div class="card-header bg-secondary text-white">NPC</div>
                <div class="card-body bg-light">{{ adventure.AdventureNPCs }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>
<style>
label {
  font-weight: bold;
  text-align: right;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.heading {
  font-size: 2rem;
  font-weight: 600;
}

.card-body {
  font-size: 1.2rem;
  font-weight: 400;
}
</style>
<script>
import axios from 'axios';
const backendURL = 'http://localhost:5000';
export default {
  data() {
    return {
      adventureTitle: '',
      adventureSetting: '',
      adventurePlot: '',
      adventure: null,
    }
  },
  methods: {
    generateAdventure() {
      this.adventure = null;
      const path = `${backendURL}/generate_adventure`;
      axios.post(path, {
        adventureTitle: this.adventureTitle,
        adventureSetting: this.adventureSetting,
        adventurePlot: this.adventurePlot
      })
        .then(response => {
          console.log(response);
          this.adventure = JSON.parse(response.data[0].message.choices[0].text.replace(/[^\x20-\x7E]+/g, ''));
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
}
</script>
