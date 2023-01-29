<template>
  <div class="container my-5">
    <h2 class="text-center mb-5 heading">Stored Adventures</h2>
    <div>
      <vue-good-table v-on:selected-rows-change="selectionChanged" :columns="columns" :rows="adventures"
        :pagination-options="{ enabled: true, mode: 'records', perPage: 10 }" :search-options="{ enabled: true }"
        :select-options="{ enabled: true, selectOnCheckboxOnly: true, selectionInfoClass: 'text-center', selectionText: 'rows selected', clearSelectionText: 'clear' }"
        class="my-table">
        <template #selected-row-actions>
          <button v-if="selection.selectedRows.length == 1" class="btn btn-primary mx-1" @click="onView">View</button>
          <button class="btn btn-danger" @click="onDelete">Delete</button>
        </template>
        <template #table-row="props">
          <span v-if="props.column.field == 'after'" class="d-flex align-items-center">
            <button class="btn btn-secondary" @click="onView(props.row)">View</button>
          </span>
        </template>
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
      selection: [],
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
          label: 'Hook',
          field: 'AdventureHook',
          filterable: true,
          sortable: true
        },
        {
          label: 'Action',
          field: 'after',
          template: '',
          html: true,
          tdClass: 'align-middle'
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
    onView(params) {
      console.log(params)
      router.push({ path: '/AdventureView', query: { id: params['AdventureID'] } })
    },
    onDelete() {
      // Add code to delete the row here
    },
    selectionChanged(selectedRows) {
      console.log(selectedRows)
      this.selection = selectedRows
      console.log(this.selection.selectedRows.length)
      //console.log(this.$refs['my-table'].selectedRows)
    }
  }
}
</script>