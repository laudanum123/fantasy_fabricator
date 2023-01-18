<template>
  <div>
    <h1>Encounter Builder</h1>
    
    <input type="text" v-model="encounterName"/>
    <button @click="createEncounter()">Create Encounter</button>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        encounterName: ''
      }
    },
    methods: {
      createEncounter() {
        // Send AJAX request to backend with encounter name
      }
    }
  }
</script>
