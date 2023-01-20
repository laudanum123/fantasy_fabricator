<template>
  <div class="container my-5">
    <h2 class="text-center mb-5">Map Generator</h2>
    <div class="form-group">
      <label for="map-name">Map Name:</label>
      <input type="text" class="form-control" id="map-name" v-model="mapName" placeholder="Enter Map Name">
    </div>
    <button class="btn btn-primary" @click="createMap()">Create Map</button>
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