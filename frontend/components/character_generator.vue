<template>
  <div>
    <h1>Community Support</h1>
    
    <input type="text" v-model="communityName"/>
    <button @click="createCommunity()">Create Community</button>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        communityName: ''
      }
    },
    methods: {
      createCommunity() {
        // Send AJAX request to backend with community name
      }
    }
  }
</script>