<template>
  <div class="container my-5">
    <div v-if="adventure" class="row justify-content-center">
      <div class="col-md-8">
        <div class="d-flex justify-content-between">
          <h2 class="text-center">{{ adventure.AdventureTitle }}</h2>
          <router-link :to="{ name: 'adventure manager' }" class="btn btn-primary">Back to
            Overview</router-link>
        </div>
        <hr>
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Adventure Hook</h4>
            <p class="card-text" v-html="adventure.AdventureHook"></p>
          </div>
        </div>
        <br>
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Adventure NPCs</h4>
            <p class="card-text" v-html="adventure.AdventureNPCs"></p>
          </div>
        </div>
        <br>
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Adventure Plot</h4>
            <p class="card-text" v-html="adventure.AdventurePlot"></p>
          </div>
        </div>
        <br>
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Adventure Climax</h4>
            <p class="card-text" v-html="adventure.AdventureClimax"></p>
          </div>
        </div>
        <br>
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Adventure Resolution</h4>
            <p class="card-text" v-html="adventure.AdventureResolution"></p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  transition: 0.3s;
}

.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
}
</style>
<script>
import axios from 'axios';
import { reactive } from 'vue';
const backendURL = 'http://localhost:5000';
export default {
  data() {
    return {
      adventure: null,
      NPCs: null
    }
  },
  methods: {
    getDb() {
      const path = `${backendURL}/get_adventures_from_db`;
      return axios.get(path, { params: { id: this.$route.query.id } })
        .then(response => {
          // console.log(response)
          this.adventure = response.data[0];
        })
        .catch(error => {
          console.log(error)
        })
    },
    getNpc() {
      const path = `${backendURL}/get_NPCs_from_db`;
      return axios.get(path, { params: { id: this.$route.query.id } })
        .then(response => {
          // console.log(response)
          this.NPCs = response.data;
        })
        .catch(error => {
          console.log(error)
        })
    },
    highlightEntities() {
      // iterate through adventure components and highlight named entities
      const adventureComponents = [
        this.adventure.AdventureHook,
        this.adventure.AdventureNPCs,
        this.adventure.AdventurePlot,
        this.adventure.AdventureClimax,
        this.adventure.AdventureResolution
      ];
      const adventure = reactive(this.adventure);
      let keys = Object.keys(adventure);
      adventureComponents.forEach((component, index) => {
        // console.log(component)
        // console.log(index)
        let highlightedText = component;
        this.NPCs.forEach((entity) => {
          const link = `<a href="/npc?id=${entity}">${entity}</a>`;
          console.log(entity)
          console.log(link)
          highlightedText = highlightedText.replace(new RegExp(entity, "gi"), link); // g: global,i: case-insensitive
          console.log(highlightedText.includes(entity))
        });
        adventure[keys[index]] = highlightedText;
      });
      this.adventure = adventure;
    }
  },
  mounted() { // add locations method to retrieve all locations from db
    this.getDb()
      .then(() => this.getNpc())
      .then(() => this.highlightEntities())
      .catch(error => {
        console.log(error)
      });
  }
}
</script>
