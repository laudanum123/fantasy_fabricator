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
        <MyCard title="Adventure Hook">
            <div v-html="adventure.AdventureHook"></div>
          </MyCard>
          <MyCard title="Adventure NPCs">
            <div v-html="adventure.AdventureNPCs"></div>
          </MyCard>
          <MyCard title="Adventure Plot">
            <div v-html="adventure.AdventurePlot"></div>
          </MyCard>
          <MyCard title="Adventure Climax">
            <div v-html="adventure.AdventureClimax"></div>
          </MyCard>
          <MyCard title="Adventure Resolution">
            <div v-html="adventure.AdventureResolution"></div>
          </MyCard>
      </div>
    </div>
  </div>
</template>
<script>
import MyCard from '../components/Cards/AdventureView Card.vue';
import axios from 'axios';
import { reactive } from 'vue';
const backendURL = 'http://localhost:5000';
export default {
  data() {
    return {
      adventure: null,
      NPCs: null,
      locations: null
    }
  },
  components: {
    MyCard
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
    getLocations() {
      const path = `${backendURL}/get_locations_from_db`;
      return axios.get(path, { params: { id: this.$route.query.id } })
        .then(response => {
          // console.log(response)
          this.locations = response.data;
        })
        .catch(error => {
          console.log(error)
        })
    },
    highlightEntities() { //TODO improve readability
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
      console.log(keys)
      adventureComponents.forEach((component, index) => {
        // console.log(component)
        // console.log(index)
        let highlightedText = component;
        this.NPCs.forEach((entity) => { // loop over NPCs
          const link = `<a href="/npc?id=${entity}">${entity}</a>`;
          // console.log(entity)
          // console.log(link)
          highlightedText = highlightedText.replace(new RegExp(entity, "gi"), link); // g: global,i: case-insensitive
          // console.log(highlightedText.includes(entity))
        });
        // this.locations.forEach((entity) => { // loop over locations #currently clashes with NPCs highlighted text
        //   const link = `<a href="/npc?id=${entity}">${entity}</a>`;
        //   console.log(entity)
        //   console.log(link)
        //   highlightedText = highlightedText.replace(new RegExp(entity, "gi"), link); // g: global,i: case-insensitive
        //   console.log(highlightedText.includes(entity))
        // });
        adventure[keys[index]] = highlightedText;
      });
      this.adventure = adventure;
    }
  },
  mounted() { // add locations method to retrieve all locations from db
    this.getDb()
      .then(() => this.getNpc())
      .then(() => this.getLocations())
      .then(() => this.highlightEntities())
      .catch(error => {
        console.log(error)
      });
  }
}
</script>