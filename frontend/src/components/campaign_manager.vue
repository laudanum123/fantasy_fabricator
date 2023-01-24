<template>
  <div>
    <vue-good-table :columns="columns" :rows="adventures" :paginate="true" :lineNumbers="true" :perPage="10"
      :search="true" :filter="filter" :sort-icon="sortIcon">
    </vue-good-table>
  </div>
</template>

<script>
import axios from 'axios'
import VueGoodTable from 'vue-good-table'

export default {
  components: {
    VueGoodTable
  },
  data() {
    return {
      columns: [
        {
          label: 'Title',
          field: 'title',
          filterable: true,
          sortable: true
        },
        {
          label: 'Setting',
          field: 'setting',
          filterable: true,
          sortable: true
        },
        {
          label: 'Plot',
          field: 'plot',
          filterable: true,
          sortable: true
        }
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
    axios.get('/api/adventures')
      .then(response => {
        this.adventures = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>
