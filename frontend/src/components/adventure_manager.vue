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
            <button class="btn btn-secondary mx-1" @click="onView(props.row)">View</button>
            <button class="btn btn-secondary mx-1" @click="onExtract(props.row)">Extract</button>
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
  methods: {
    getDb(){
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
    onView(params) {
      router.push({ path: '/AdventureView', query: { id: params['AdventureID'] } })
    },
    onExtract(row_id){
      const path = `${backendURL}/extract_entities/${row_id.AdventureID}`;
    axios.post(path)
      .then(response => {
        console.log(response.data)
      })
      .catch(error => {
        console.log(error)
      })
    },
    onDelete() {
      const ids = this.selection.selectedRows.map(row => row['AdventureID']);
      const path = `${backendURL}/delete_adventures_from_db`;
      console.log(ids);
      axios.delete(path, { data: { ids: ids } })
        .then(this.getDb)
        .catch(error => {
          console.log(error);
        });
    },

    selectionChanged(selectedRows) {
      this.selection = selectedRows
    }
  },
mounted() {
    this.getDb();
  }
}
</script>