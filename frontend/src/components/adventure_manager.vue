<template>
  <div class="container my-5">
    <h2 class="text-center mb-5 heading">Stored Adventures</h2>
    <div>
      <vue-good-table :columns="columns" :rows="adventures" :paginate="true" :perPage="10" :search="true"
        :filter="filter" :sort-icon="sortIcon" class="my-table" v-on:row-click="onRowClick">
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
import router from '@/router';
import axios from 'axios'
const backendURL = 'http://localhost:5000';

export default {
  components: {
  },
  data() {
    return {
      columns: [
        {
          label: 'ID',
          field: 'AdventureID',
          filterable: true,
          sortable: true
        },
        {
          label: 'Title',
          field: 'AdventureTitle',
          filterable: true,
          sortable: true
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
            'AdventureID': adventure.id,
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
  },
  methods: {
    onRowClick(params) {
      router.push({ path: '/AdventureView', query: { id: params.row['AdventureID'] } })
    }
  }
}
</script>