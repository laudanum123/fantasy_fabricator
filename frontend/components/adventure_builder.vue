<template>
  <div>
    <h1>Adventure Builder</h1>
    
    <input type="text" v-model="adventureName"/>
    <button @click="createAdventure()">Create Adventure</button>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        adventureName: ''
      }
    },
    methods: {
      createAdventure() {
        // Send AJAX request to backend with adventure name
      }
    }
  }
</script>