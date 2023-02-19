<template>
  <div class="container my-5">
    <h2 class="text-center mb-5 heading">Stored Adventures</h2>
    <!-- Notification template -->
    <template v-if="show">
      <div class="container my-4">
        <div class="toast-container position-absolute" :class="position">
          <div class="toast" :class="show">
            <ToastHeader :toast="toast" @hide="hideToast" />
            <ToastBody :message="toast.message" />
          </div>
        </div>
      </div>
    </template>
    <div id="message-container"></div>
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
import ToastHeader from '@/components/Notifications/ToastHeader.vue';
import ToastBody from '@/components/Notifications/ToastBody.vue';
import moment from 'moment';
import router from '@/router';
import axios from 'axios'
const backendURL = 'http://localhost:5000';

export default {
  components: {
    ToastHeader,
    ToastBody
  },
  data() {
    return {
      showToast: '',
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
      }, toast: {
        icon: '',
        title: '',
        time: '',
        message: '',
        bgColor: '',
      },
      show: '',
      position: '',
      timeout: null
    }
  },
  methods: {
    getDb() {
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
              'EntitiesExtracted': adventure.EntitiesExtracted
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
    onExtract(row_id) {
      if (!row_id.EntitiesExtracted) {
        this.successToast()
        const path = `${backendURL}/extract_entities/${row_id.AdventureID}`;
        axios.post(path)
          .catch(error => {
            console.log(error)
          })
        } else {
          this.dangerToast()
        }
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
    },
    successToast() {
      this.show = 'show';
      this.position = 'top-0 end-0';
      this.toast = {
        icon: 'fa-solid fa-check me-2',
        time: moment().fromNow(),
        title: 'success',
        bgColor: 'bg-success',
        message: 'Extraction successful, click View for results!'
      }
    },
    dangerToast() {
      this.show = 'show';
      this.position = 'top-0 end-0';
      this.toast = {
        icon: 'fa-solid fa-bolt me-2',
        time: moment().fromNow(),
        title: 'Error',
        bgColor: 'bg-danger',
        message: 'Adventure already extracted!'
      }
    },
    hideToast() {
      this.show = '';
      this.position = '';
    },
  },
  mounted() {
    this.getDb();
  },
  watch: {
    show() {
      if (this.timeout) {
        clearTimeout(this.timeout);
      }
      this.timeout = setTimeout(() => {
        this.show = '';
        this.position = '';
      }, 3000);
    }
  }
}
</script>