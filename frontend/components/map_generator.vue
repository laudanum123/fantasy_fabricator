<template>
  <div>
    <h1>Map Generator</h1>
    
    <input type="text" v-model="mapName"/>
    <button @click="createMap()">Create Map</button>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        mapName: ''
      }
    },
    methods: {
      createMap() {
        // Send AJAX request to backend with map name
      }
    }
  }
</script>