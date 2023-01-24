<template>
  <div class="container my-5">
    <h2 class="text-center mb-5 heading">Stored Adventures</h2>
    <div>
      <vue-good-table :columns="columns" :rows="adventures" :paginate="true" :lineNumbers="true" :perPage="10"
        :search="true" :filter="filter" :sort-icon="sortIcon" class="my-table">
      </vue-good-table>
    </div>
  </div>
</template>
<style>
.my-table {
  margin-top: 50px;
  margin-left: 10px;
  margin-right: 10px;
}
</style>
<script>
import axios from 'axios'
const backendURL = 'http://localhost:5000';

export default {
  components: {
  },
  data() {
    return {
      columns: [
        {
          label: 'Title',
          field: 'AdventureTitle',
          filterable: true,
          sortable: true,
          template: '<a :href="adventure.AdventureTitle" target="_blank">{{adventure.AdventureTitle}}</a>'
        },
        {
          label: ' Hook',
          field: 'AdventureHook',
          filterable: true,
          sortable: true
        },
      ],
      adventures: [],
      filter: true,
      sortIcon: {
        is: 'fa-sort',
        up: 'fa-sort-up',
        down: 'fa-sort-down'
      }
    }
  },
  mounted() {
    const path = `${backendURL}/get_adventures_from_db`;
    axios.get(path)
      .then(response => {
        this.adventures = response.data.map(adventure => {
          return {
            'AdventureTitle': adventure.AdventureTitle,
            'AdventureHook': adventure.AdventureHook,
            'AdventureNPCs': adventure.AdventureNPCs,
            'AdventurePlot': adventure.AdventurePlot,
          }
        });
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>